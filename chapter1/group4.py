# fmt: off
import sys
from pathlib import Path
# 获取项目根目录（假设 chapter1 在项目根目录下）
project_root = Path(__file__).parent.parent  # 上一级目录
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
from custom.edg_tts import EdgeTTSService
from manim_voiceover import VoiceoverScene
from manim import *
# fmt: on

# ============================================================
# 全局视觉风格
# ============================================================

BG = WHITE
SVG_DIR = "material"
SUNDRY_PATH = "material/sundry/"
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
FIGURE_PATH = "material/figure/"
AI_PATH = "material/ai/"
BODY_PATH = "material/body/"
FACE_PATH = f"{BODY_PATH}face/"
EMOJI_PATH = "material/emoji/"


class Group4(VoiceoverScene):

    def construct(self):

        self.camera.background_color = BG
        self.set_speech_service(
            EdgeTTSService()
        )

        self._section01()
        self.next_section("02")
        self._section02()
        self.next_section("03")
        self._section03()
        self.next_section("04")
        self._section04()
        self.next_section("05")
        self._section05()
        self.next_section("06")
        self._section06()
        # self.next_section("07")
        # self._section07()
        # self.next_section("08")
        # self._section08()

    def _section01(self):
        with self.voiceover(text="现在我们开始学习AIMA。"):
            preface = SVGMobject(
                "chapter1/asset/action.svg"
            )

            preface.set_height(3.8)
            preface.move_to(ORIGIN)
            self.play(
                FadeIn(preface, scale=0.8),
            )

        self.clear()

    def _section02(self):
        with self.voiceover(text="先看一下 AIMA 序言中对书籍的标题的阐明:"):
            preface = SVGMobject(
                "chapter1/asset/preface.svg"
            )

            preface.set_height(3.8)
            preface.move_to(ORIGIN)
            self.play(
                FadeIn(preface, scale=0.8),
            )
        self.clear()

    def _section03(self):
        with self.voiceover(text="""主标题Artificial Intelligence: 
                            表明会探索AI的全部领域，但只能浅尝辄止。"""):
            # ==========================================
            # 第一条
            # ==========================================

            bullet1 = Text(
                "•",
                font="Arial",
                font_size=36,
                color=BLACK,
            )

            title1 = Text(
                "Artificial Intelligence:",
                font="Arial",
                font_size=34,
                weight=BOLD,
                color=BLACK,
            )

            desc1 = Text(
                "会探索 AI 的全部领域，但只能浅尝辄止。",
                font="FangSong",
                font_size=29,
                color=BLACK,
            )
            bullet1.move_to(LEFT * 5.7 + UP * 1.8)

            title1.next_to(
                bullet1,
                RIGHT,
                buff=0.2,
            )

            desc1.next_to(
                title1,
                DOWN,
                aligned_edge=LEFT,
                buff=0.18,
            )
            # ==========================================
            # 第一条
            # ==========================================

            self.play(
                FadeIn(bullet1),
                FadeIn(title1, shift=RIGHT * 0.15),
                run_time=0.5,
            )

            self.play(
                FadeIn(desc1, shift=UP * 0.15),
                run_time=0.5,
            )
        with self.voiceover(text="""副标题 A Modern Approach: 
                            表示将以现代的角度把所有的AI知识放到一个框架内，
                            使用当今流行的思想和术语对早期研究进行重新表述。"""):
            # ==========================================
            # 第二条
            # ==========================================

            bullet2 = Text(
                "•",
                font="Arial",
                font_size=36,
                color=BLACK,
            )

            title2 = Text(
                "A Modern Approach:",
                font="Arial",
                font_size=34,
                weight=BOLD,
                color=BLACK,
            )

            desc2 = Text(
                "以现代的角度把所有的 AI 知识放到一个框架内，",
                font="FangSong",
                font_size=29,
                color=BLACK,
            )

            desc3 = Text(
                "使用当今流行的思想和术语对早期研究进行重新表述。",
                font="FangSong",
                font_size=29,
                color=BLACK,
            )

            # ==========================================
            # 布局
            # ==========================================
            bullet2.move_to(
                LEFT * 5.7 + DOWN * 0.2
            )

            title2.next_to(
                bullet2,
                RIGHT,
                buff=0.2,
            )

            desc2.next_to(
                title2,
                DOWN,
                aligned_edge=LEFT,
                buff=0.18,
            )

            desc3.next_to(
                desc2,
                DOWN,
                aligned_edge=LEFT,
                buff=0.12,
            )

            # ==========================================
            # 第二条
            # ==========================================

            self.play(
                FadeIn(bullet2),
                FadeIn(title2, shift=RIGHT * 0.15),
                run_time=0.5,
            )

            self.play(
                FadeIn(desc2, shift=UP * 0.15),
                FadeIn(desc3, shift=UP * 0.15),
                run_time=0.6,
            )
        self.clear()

    def _section04(self):
        with self.voiceover(text="""然后，是对第三版(2010版)和第四版(2020版)两个版本的比较，"""):
            compare = ImageMobject(
                "chapter1/asset/compare.png"
            )
            self.play(
                FadeIn(compare, scale=0.8),
            )
        self.play(
            FadeOut(compare),
        )

        with self.voiceover(text="""因为我们不会看两个版本，故这一点对我们来说不是重点。"""):
            # ==========================================
            # 切换到“评书的”
            # ==========================================
            whatever = SVGMobject(f"{FACE_PATH}whatever.svg")
            self.play(
                FadeIn(whatever),
            )
        self.clear()

    def _section05(self):
        with self.voiceover(text="""另外说明全书的统一主题是“智能体”这一概念，"""):
            title = ImageMobject("chapter1/asset/title.png")
            title.scale(0.8)
            self.play(FadeIn(title))
        self.clear()

        with self.voiceover(text="""考虑到在没有明确定义“智能体”的情况下，"""):
            difine = SVGMobject(f"{MATH_PATH}einstein-eq.svg")
            self.play(FadeIn(difine))
        self.clear()

        with self.voiceover(text="""序言中的进一步讨论很容易陷入空转，因此这部分内容我有意略过了。"""):
            turn = SVGMobject("chapter1/asset/turn.svg")
            self.play(FadeIn(turn))
        self.clear()

    def _section06(self):
        with self.voiceover(text="""这本书的配套在线资源，并非对所有读者完全开放。"""):
            # 加载SVG，把你的web.svg、lock.svg放到 assets 文件夹
            web_svg = SVGMobject("chapter1/asset/online-source.svg").scale(2)
            lock_svg = SVGMobject("chapter1/asset/lock.svg").scale(0.8)

            # 锁初始位置：右侧外面
            lock_svg.move_to(RIGHT * 4)

            # 1、网页出现
            self.play(FadeIn(web_svg))
            self.wait(0.5)

            # 设置锁的目标位置：移动到网页上方居中
            lock_svg.generate_target()
            lock_svg.target.move_to(web_svg.get_center())

            # 2、锁移动到网页上
            self.play(MoveToTarget(lock_svg), run_time=1.2)
            self.wait(1)

            # 可选：锁落下后轻微变暗，表现锁住
            self.play(lock_svg.animate.set_opacity(0.8))
        self.clear()

        with self.voiceover(text="""没有权限的同学们，可以在github中找到习题和书中的代码实现。"""):
            github = SVGMobject("material/github.svg").scale(0.8)
            self.play(FadeIn(github))
        self.clear()
