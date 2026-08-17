from manim import *
# fmt: off
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
FIGURE_PATH = "material/figure/"
# fmt: on

from manim import *


class FindMaterials(Scene):

    def construct(self):
        self.camera.background_color = WHITE

        # ==================================================
        # 1. 问题
        # ==================================================

        question = SVGMobject(
            f"{MATH_PATH}question.svg"
        )
        question.scale(1.35)
        question.move_to(LEFT * 4)

        # ==================================================
        # 2. Machine Learning 领域 / 书籍
        # ==================================================

        ml_book = SVGMobject(
            f"{MATH_PATH}/book.svg"
        )
        ml_book.scale(1.35)
        ml_book.move_to(ORIGIN)

        ml_text = Text(
            "Machine Learning",
            font_size=32,
            color=BLACK
        )
        ml_text.next_to(
            ml_book,
            DOWN,
            buff=0.25
        )

        ml_group = VGroup(
            ml_book,
            ml_text
        )

        # ==================================================
        # 3. 深入资料
        # ==================================================

        textbook = SVGMobject(
            "assets/textbook.svg"
        )
        textbook.scale(1.0)
        textbook.move_to(
            RIGHT * 3.5 + UP * 1.6
        )

        paper = SVGMobject(
            "assets/paper.svg"
        )
        paper.scale(1.0)
        paper.move_to(
            RIGHT * 3.5
        )

        course = SVGMobject(
            "assets/course.svg"
        )
        course.scale(1.0)
        course.move_to(
            RIGHT * 3.5 + DOWN * 1.6
        )

        # ==================================================
        # 4. 两个箭头
        # ==================================================

        arrow1 = Arrow(
            question.get_right(),
            ml_book.get_left(),
            buff=0.45,
            stroke_width=4,
            color=GREY_B
        )

        arrow2 = Arrow(
            ml_group.get_right(),
            paper.get_left(),
            buff=0.5,
            stroke_width=4,
            color=GREY_B
        )

        # ==================================================
        # 动画
        # ==================================================

        # ------------------------------------------
        # 第一层：出现问题
        # ------------------------------------------

        self.play(
            FadeIn(question, scale=0.8),
            run_time=0.6
        )

        self.wait(0.3)

        # ------------------------------------------
        # 第二层：找到对应领域
        # ------------------------------------------

        self.play(
            GrowArrow(arrow1),
            FadeIn(ml_book, scale=0.8),
            run_time=0.7
        )

        self.play(
            FadeIn(ml_text),
            run_time=0.4
        )

        self.wait(0.5)

        # ------------------------------------------
        # 第三层：进一步深入资料
        # ------------------------------------------

        self.play(
            GrowArrow(arrow2),
            run_time=0.5
        )

        self.play(
            FadeIn(textbook, shift=LEFT * 0.4),
            run_time=0.5
        )

        self.play(
            FadeIn(paper, shift=LEFT * 0.4),
            run_time=0.5
        )

        self.play(
            FadeIn(course, shift=LEFT * 0.4),
            run_time=0.5
        )

        self.wait(1.5)