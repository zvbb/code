from manim import *
# fmt: off
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
FIGURE_PATH = "material/figure/"
BODY_PATH = "material/body/"
# fmt: on

from manim import *


class FindMaterials(Scene):

    def construct(self):
        self.camera.background_color = WHITE

        # ==================================================
        # 1. 问题
        # ==================================================

        question = SVGMobject(
            f"{BODY_PATH}thinking-funny.svg"
        )
        question.scale(1)
        question.move_to(ORIGIN)

        self.play(
            FadeIn(question, scale=0.8),
            run_time=0.6
        )
