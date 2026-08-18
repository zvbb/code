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
EMOJI_PATH = "material/emoji/"

# ============================================================
# 01
# 如果想系统地学习人工智能，
# 第一个问题是：应该从哪里开始？
# ============================================================

# # ===== 添加这部分用于调试 =====
# if __name__ == "__main__":
#     from manim import config
#     from manim.__main__ import main  # 改这里

#     config.preview = True
#     config.quality = "low_quality"
#     # 如果你用的是高画质，改为 "high_quality"

#     # 运行你的场景
#     main(["group1.py", "Scene01"])

# ============================================================
# 02
# 今天学习 AI 的门槛已经很低了
# ============================================================


class Group3(VoiceoverScene):

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
        # self.next_section("05")
        # self._section05()
        # self.next_section("06")
        # self._section06()
        # self.next_section("07")
        # self._section07()
        # self.next_section("08")
        # self._section08()

    def _section01(self):
        with self.voiceover(text="当然，AIMA 也有一个非常现实的问题：太厚了!"):
            # =========================
            # 左侧：苦恼人物 SVG
            # =========================

            person = SVGMobject(
                f"{EMOJI_PATH}/sweat.svg"
            )

            person.set_height(3.8)
            person.move_to(LEFT * 3.0)

            # =========================
            # 右侧：太厚了
            # =========================

            text = Text(
                "太厚了",
                font="FangSong",
                font_size=90,
                weight=BOLD,
                color=BLACK,
            )

            text.move_to(RIGHT * 2.5)

            # =========================
            # 动画
            # =========================

            # 人物出现
            self.play(
                FadeIn(
                    person,
                    shift=RIGHT * 0.2
                ),
                run_time=0.6
            )

            self.wait(0.3)

            # “太厚了”出现
            self.play(
                FadeIn(
                    text,
                    scale=0.8
                ),
                run_time=0.5
            )

            # 稍微强调一下
            self.play(
                text.animate.scale(1.08),
                rate_func=there_and_back,
                run_time=0.35
            )
        self.clear()

    def _section02(self):
        books = VGroup()
        book_count = 6
        with self.voiceover(text="AIMA 全书总页数 1000+，篇幅相当长。"):
            book_path = f"{MATH_PATH}book-close.svg"

            # ==================================================
            # 创建第一本书
            # ==================================================

            first_book = SVGMobject(book_path)
            first_book.set_width(1.5)

            books.add(first_book)

            # 获取 SVG 的真实高度
            book_height = first_book.height

            # ==================================================
            # 创建后面的书
            # ==================================================

            for i in range(1, book_count):

                book = SVGMobject(book_path)
                book.set_width(1.5)

                book.move_to(
                    first_book.get_center()
                    + UP * (i * book_height)
                )

                books.add(book)

            # ==================================================
            # 整体居中
            # ==================================================

            books.move_to(LEFT * 2.0)

            # ==================================================
            # 一本一本从上面掉下来
            # ==================================================

            for book in books:

                final_pos = book.get_center()

                book.move_to(
                    final_pos + UP * 2
                )

                self.play(
                    book.animate.move_to(final_pos),
                    rate_func=rush_into,
                    run_time=0.35
                )

            # ==================================================
            # 1000+ 页
            # ==================================================

            pages = Text(
                "1000+ 页",
                font="FangSong",
                font_size=72,
                weight=BOLD,
                color=BLACK,
            )

            pages.move_to(RIGHT * 3.2)

            self.play(
                FadeIn(pages, scale=0.8),
                run_time=0.5
            )
        self.play(
            FadeOut(pages),
            run_time=0.3
        )

        with self.voiceover(text="""以我的实际阅读感受来说，废话较多，要说砍掉 8 成字数可能有些武断，"""):
            # ==================================================
            # 砍掉 80%
            # ==================================================
            self.wait(2)

            text_80 = Text(
                "砍掉 80%？",
                font="FangSong",
                font_size=64,
                weight=BOLD,
                color=BLACK,
            )

            text_80.move_to(RIGHT * 3.2)

            self.play(
                FadeIn(text_80, scale=0.8),
                run_time=0.4
            )

            self.wait(0.5)

            # 保留 1 本
            # 其余书向下消失
            self.play(
                *[
                    FadeOut(
                        book,
                        shift=DOWN * 0.4
                    )
                    for book in books[1:]
                ],
                run_time=0.8
            )

            self.wait(0.8)

            # ==================================================
            # 有点武断……
            # ==================================================

            warning = Text(
                "有点武断...",
                font="FangSong",
                font_size=42,
                color=BLACK,
            )

            warning.next_to(
                text_80,
                DOWN,
                buff=0.3
            )

            self.play(
                FadeIn(warning),
                run_time=0.4
            )

            self.wait(1)

            # ==================================================
            # 恢复 6 本书
            # ==================================================

            self.play(
                *[
                    FadeIn(
                        book,
                        shift=UP * 0.4
                    )
                    for book in books[1:]
                ],
                run_time=0.8
            )

            self.play(
                FadeOut(text_80),
                FadeOut(warning),
                run_time=0.3
            )
        with self.voiceover(text="""但只砍一半字数，都感觉砍少了。"""):
            # ==================================================
            # 砍掉一半
            # ==================================================

            text_50 = Text(
                "砍掉一半？",
                font="FangSong",
                font_size=64,
                weight=BOLD,
                color=BLACK,
            )

            text_50.move_to(RIGHT * 3.2)

            self.play(
                FadeIn(text_50, scale=0.8),
                run_time=0.4
            )

            self.wait(0.5)

            # 6 本 -> 3 本
            self.play(
                *[
                    FadeOut(
                        book,
                        shift=DOWN * 0.4
                    )
                    for book in books[3:]
                ],
                run_time=0.8
            )

            self.wait(1)

            # ==================================================
            # 感觉还是有点少
            # ==================================================

            self.play(
                FadeOut(text_50),
                run_time=0.3
            )

            final_text = Text(
                "砍少了!",
                font="FangSong",
                font_size=52,
                weight=BOLD,
                color=BLACK,
            )

            final_text.move_to(RIGHT * 3.0)

            self.play(
                FadeIn(
                    final_text,
                    scale=0.9
                ),
                run_time=0.5
            )

        self.clear()

    def _section03(self):
        with self.voiceover(text="""因此，我会对每个章节进行概述和梳理，把冗余的部分删除，
                            但不会为了追求篇幅而删掉其中的关键概念、论证和细节。"""):
            # ==================================================
            # 参数
            # ==================================================

            BLACK = "#222222"

            # ==================================================
            # 卡片函数
            # ==================================================

            def create_card(text, width=1.55, height=0.55):

                rect = RoundedRectangle(
                    corner_radius=0.08,
                    width=width,
                    height=height,
                    stroke_width=2,
                    stroke_color=BLACK,
                    fill_color=WHITE,
                    fill_opacity=1,
                )

                label = Text(
                    text,
                    font="FangSong",
                    font_size=25,
                    color=BLACK,
                )

                label.move_to(rect)

                return VGroup(rect, label)

            # ==================================================
            # 上方：大量内容卡片
            # ==================================================

            contents = [
                "概念",
                "例子",
                "论证",
                "冗余",
                "细节",
                "背景",
                "概念",
                "冗余",
                "论证",
                "补充",
            ]

            cards = VGroup(
                *[
                    create_card(text)
                    for text in contents
                ]
            )

            # 两排五列
            cards.arrange_in_grid(
                rows=2,
                cols=5,
                buff=(0.25, 0.25),
            )

            cards.move_to(
                UP * 2.8
            )

            # ==================================================
            # 卡片出现
            # ==================================================

            self.play(
                LaggedStart(
                    *[
                        FadeIn(
                            card,
                            shift=UP * 0.2
                        )
                        for card in cards
                    ],
                    lag_ratio=0.08,
                ),
                run_time=1.2
            )

            self.wait(0.5)

            # ==================================================
            # 漏斗 SVG
            # ==================================================

            funnel = SVGMobject(
                f"{SUNDRY_PATH}funnel.svg"
            )

            funnel.set_height(3.0)

            funnel.move_to(
                DOWN * 0.1
            )

            self.play(
                FadeIn(
                    funnel,
                    shift=UP * 0.3
                ),
                run_time=0.6
            )

            self.wait(0.3)

            # ==================================================
            # 下方：最终保留的卡片
            # ==================================================

            key_concept = create_card(
                "关键概念",
                width=2.2,
                height=0.65
            )

            key_argument = create_card(
                "关键论证",
                width=2.2,
                height=0.65
            )

            key_detail = create_card(
                "关键细节",
                width=2.2,
                height=0.65
            )

            result_cards = VGroup(
                key_concept,
                key_argument,
                key_detail,
            )

            result_cards.arrange(
                RIGHT,
                buff=0.3
            )

            result_cards.move_to(
                DOWN * 2.8
            )

            # ==================================================
            # 让卡片逐个进入漏斗
            # ==================================================

            # 取上方几个卡片作为“代表”
            source_cards = [
                cards[0],
                cards[2],
                cards[4],
            ]

            targets = [
                key_concept,
                key_argument,
                key_detail,
            ]

            for source, target in zip(
                source_cards,
                targets
            ):

                # 复制一个卡片
                moving_card = source.copy()

                self.add(moving_card)

                # 漏斗入口
                funnel_top = (
                    funnel.get_top()
                    + DOWN * 0.15
                )

                # 漏斗出口
                funnel_bottom = (
                    funnel.get_bottom()
                    + DOWN * 0.15
                )

                # 进入漏斗
                self.play(
                    moving_card.animate
                    .move_to(funnel_top)
                    .scale(0.65),
                    run_time=0.45
                )

                # 穿过漏斗
                self.play(
                    moving_card.animate
                    .move_to(funnel_bottom)
                    .scale(0.55),
                    run_time=0.45
                )

                # 从漏斗出来
                self.play(
                    moving_card.animate
                    .move_to(target.get_center())
                    .scale(1.6),
                    run_time=0.4
                )

                self.remove(moving_card)

                self.play(
                    FadeIn(target, scale=0.8),
                    run_time=0.25
                )

            # ==================================================
            # 冗余内容淡出
            # ==================================================

            redundant_indices = [
                1, 3, 5, 7, 9
            ]

            self.play(
                *[
                    FadeOut(
                        cards[i],
                        shift=DOWN * 0.4
                    )
                    for i in redundant_indices
                ],
                run_time=0.7
            )

        self.clear()

    def _section04(self):
        with self.voiceover(text="""你可以把我看做：帮你读 AIMA 的工具人。"""):
            # ==========================================
            # 工具人
            # ==========================================

            worker = SVGMobject(
                "chapter1/asset/tool-person.svg"
            )

            worker.set_height(2.8)
            worker.move_to(LEFT * 2.5)

            worker_text = Text(
                "帮你读 AIMA 的工具人",
                font="FangSong",
                font_size=42,
                color=BLACK,
            )

            worker_text.move_to(RIGHT * 2.5)

            self.play(
                FadeIn(worker, scale=0.8),
                FadeIn(worker_text, shift=RIGHT * 0.2),
                run_time=0.6,
            )

        with self.voiceover(text="""或者更形象一点：一个评书的。"""):
            # ==========================================
            # 切换到“评书的”
            # ==========================================

            self.play(
                FadeOut(worker),
                FadeOut(worker_text),
                run_time=0.4,
            )

            storyteller = SVGMobject(
                "chapter1/asset/pingshu.svg"
            )

            storyteller.set_height(3.0)
            storyteller.move_to(LEFT * 2.5)

            storyteller_text = Text(
                "一个评书的",
                font="FangSong",
                font_size=52,
                weight=BOLD,
                color=BLACK,
            )

            storyteller_text.move_to(RIGHT * 1.8)

            self.play(
                FadeIn(storyteller, scale=0.8),
                FadeIn(storyteller_text, shift=RIGHT * 0.2),
                run_time=0.6,
            )
        self.clear()
