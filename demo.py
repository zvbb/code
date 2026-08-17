# fmt: off
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
# fmt: on

from manim import *


class AIMAQuestion(Scene):

    def construct(self):
        # =========================
        # 基本设置
        # =========================
        self.camera.background_color = WHITE

        # =========================
        # Question
        # =========================
        question = SVGMobject(
            f"{MATH_PATH}question.svg"
        )
        question.scale(1.5)
        question.move_to(LEFT * 3.2)

        # =========================
        # Solution
        # =========================
        solution = SVGMobject(
            f"{MATH_PATH}solution.svg"
        )
        solution.scale(1.5)
        solution.move_to(RIGHT * 3.2)

        # =========================
        # 中间箭头
        # =========================
        arrow = Arrow(
            question.get_right(),
            solution.get_left(),
            buff=0.6,
            stroke_width=5,
            color=GREY_B
        )

        # =========================
        # No
        # =========================
        no = SVGMobject(
            f"{MATH_PATH}/no.svg"
        )
        no.scale(1.7)
        no.move_to(solution)

        # =========================
        # 动画
        # =========================

        # 1. 出现问题
        self.play(
            FadeIn(question, scale=0.8),
            run_time=0.6
        )

        self.wait(0.3)

        # 2. 出现“答案”的预期
        self.play(
            GrowArrow(arrow),
            FadeIn(solution, scale=0.8),
            run_time=0.8
        )

        self.wait(0.5)

        # 3. 否定：AIMA 并不会直接给出这个答案
        self.play(
            FadeIn(no, scale=1.2),
            run_time=0.5
        )

        self.wait(1.5)
