# fmt: off
from manim import *
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
AI_PATH = "material/AI/"
# fmt: on


from manim import *

class SvgLockScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.wait(2)