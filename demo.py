# fmt: off
import numpy as np
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover import VoiceoverScene
from manim import *
MATH_PATH = "material/math/"
ASSET_PATH = "chapter1/asset/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
AI_PATH = "material/AI/"
BODY_PATH = "material/body/"
# fmt: on


from manim import *


class Rational(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ==================================================
        # 镜头 1：rational —— 理性
        # ==================================================

        rational = Text(
            "rational",
            font_size=82,
            weight=BOLD,
            color=BLACK,
        )

        self.play(
            Write(rational),
            run_time=1.0,
        )

        self.wait(0.5)

        reason = Text(
            "理性",
            font_size=52,
            color=BLACK,
        )

        reason.next_to(
            rational,
            DOWN,
            buff=0.3,
        )

        self.play(
            FadeIn(reason),
            run_time=0.6,
        )

        self.wait(1.5)

        # ==================================================
        # 镜头 2：澄清“理性”并不意味着人类不理性
        # ==================================================

        # rational + 理性整体上移
        rational_group = VGroup(
            rational,
            reason,
        )

        self.play(
            rational_group
            .animate
            .scale(0.6)
            .shift(UP * 3),
            run_time=0.6,
        )

        # --------------------------------------------------
        # 人类 SVG
        # --------------------------------------------------

        human = ImageMobject(
            f"{BODY_PATH}human.png"
        ).scale(0.4)

        human.move_to(DOWN * 0.25)

        self.play(
            FadeIn(human),
            run_time=0.7,
        )

        # --------------------------------------------------
        # “思考”与“行动”
        # --------------------------------------------------

        thinking = Text(
            "思考",
            font_size=38,
            color=BLACK,
        )

        acting = Text(
            "行动",
            font_size=38,
            color=BLACK,
        )

        thinking.move_to(
            LEFT * 2.0 + DOWN * 1.35
        )

        acting.move_to(
            RIGHT * 2.0 + DOWN * 1.35
        )

        # 两条连接线
        thinking_line = Line(
            human.get_bottom(),
            thinking.get_top(),
            stroke_width=2,
        )

        acting_line = Line(
            human.get_bottom(),
            acting.get_top(),
            stroke_width=2,
        )

        self.play(
            Create(thinking_line),
            Create(acting_line),
            run_time=0.5,
        )

        self.play(
            FadeIn(thinking),
            FadeIn(acting),
            run_time=0.5,
        )

        self.wait(0.5)

        # --------------------------------------------------
        # 两个 ✓
        # --------------------------------------------------

        thinking_check = Text(
            "✓",
            font_size=42,
            color=BLACK,
        )

        acting_check = Text(
            "✓",
            font_size=42,
            color=BLACK,
        )

        thinking_check.next_to(
            thinking,
            LEFT,
            buff=0.25,
        )

        acting_check.next_to(
            acting,
            RIGHT,
            buff=0.25,
        )

        self.play(
            FadeIn(thinking_check),
            FadeIn(acting_check),
            run_time=0.5,
        )

        self.wait(2)