import asyncio
from pathlib import Path
from manim import logger
from manim_voiceover._typing import VoiceoverData
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import PathLike, SpeechService, initialize_speech_service, path_to_string

try:
    import edge_tts
except ImportError:
    logger.error(
        'Missing packages. Run `pip install edge-tts` to use EdgeTTSService.')


class EdgeTTSService(SpeechService):
    """SpeechService class for Microsoft Edge's Text-to-Speech API.
    This is a wrapper for the edge_tts library.
    See the `edge_tts documentation <https://github.com/rany2/edge-tts>`__
    for more information.
    """

    def __init__(
        self,
        voice: str = "zh-CN-XiaoxiaoNeural",
        rate: int = 0,
        pitch: int = 0,
        volume: int = 0,
        **kwargs
    ) -> None:
        """
        Args:
            voice (str, optional): Voice to use for the speech.
                See `edge_tts --list-voices` for all available options.
                Defaults to "zh-CN-XiaoxiaoNeural" (Chinese female).
            rate (int, optional): Speaking rate. Range: -50 to +50. Defaults to 0.
            pitch (int, optional): Speaking pitch. Range: -50 to +50. Defaults to 0.
            volume (int, optional): Speaking volume. Range: -50 to +50. Defaults to 0.
        """
        # 检查是否安装了 edge-tts
        try:
            import edge_tts
        except ImportError:
            raise ImportError(
                "Missing package. Run `pip install edge-tts` to use EdgeTTSService."
            )

        initialize_speech_service(self, kwargs)
        self.voice = voice
        self.rate = rate
        self.pitch = pitch
        self.volume = volume

    def _build_ssml(self, text: str) -> str:
        """构建 SSML 格式的文本，用于控制语速、音调等"""
        # 将 -50 到 50 的速率转换为 edge-tts 的格式
        # 默认速率 1.0，范围 0.5 - 2.0
        rate_percent = self.rate
        if rate_percent < -50:
            rate_percent = -50
        if rate_percent > 50:
            rate_percent = 50

        # edge-tts 的速率格式: +10%, -20%
        if rate_percent >= 0:
            rate_str = f"+{rate_percent}%"
        else:
            rate_str = f"{rate_percent}%"

        # 音调格式类似
        if self.pitch >= 0:
            pitch_str = f"+{self.pitch}%"
        else:
            pitch_str = f"{self.pitch}%"

        # 音量格式
        if self.volume >= 0:
            volume_str = f"+{self.volume}%"
        else:
            volume_str = f"{self.volume}%"

        return f"""<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="zh-CN">
            <voice name="{self.voice}">
                <prosody rate="{rate_str}" pitch="{pitch_str}" volume="{volume_str}">
                    {text}
                </prosody>
            </voice>
        </speak>"""

    def _run_async(self, coro):
        """在同步上下文中运行异步代码"""
        try:
            # 尝试获取当前事件循环
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # 如果没有运行中的循环，创建一个新的
            return asyncio.run(coro)
        else:
            # 如果有运行中的循环，使用 run_until_complete
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, coro)
                return future.result()

    def generate_from_text(
        self,
        text: str,
        cache_dir: PathLike | None = None,
        path: PathLike | None = None,
        **kwargs,
    ) -> VoiceoverData:
        """生成语音"""
        if cache_dir is None:
            cache_dir = self.cache_dir

        # 去除书签标记
        input_text = remove_bookmarks(text)

        # 构建输入数据用于缓存
        input_data = {
            "input_text": input_text,
            "service": "edge_tts",
            "voice": self.voice,
            "rate": self.rate,
            "pitch": self.pitch,
            "volume": self.volume,
        }

        # 检查缓存
        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        # 确定音频路径
        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = path_to_string(path)

        # 构建 SSML
        # ssml_text = self._build_ssml(input_text)
        ssml_text = input_text

        # 生成音频
        try:
            # 创建 Communicate 对象
            communicate = edge_tts.Communicate(ssml_text, voice=self.voice)

            # 保存音频文件
            full_path = Path(cache_dir) / audio_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            # 异步保存
            self._run_async(communicate.save(str(full_path)))

        except Exception as e:
            logger.error(f"Edge TTS 生成失败: {e}")
            raise Exception(
                f"Edge TTS 生成失败。请检查网络连接。错误详情: {e}"
            )

        # 返回结果
        json_dict: VoiceoverData = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

        return json_dict
