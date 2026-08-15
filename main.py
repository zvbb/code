from manim import *


class FragmentationVsHolism(Scene):
    def construct(self):
        # ========== 左侧：电脑零件（碎片化） ==========
        cpu = SVGMobject("material/computer/cpu.svg").scale(0.7)
        gpu = SVGMobject("material/computer/gpu.svg").scale(0.7)
        mainboard = SVGMobject("material/computer/mainboard.svg").scale(0.7)
        keyboard = SVGMobject("material/computer/keyboard.svg").scale(0.7)
        mouse = SVGMobject("material/computer/mouse.svg").scale(0.7)

        # 排列成两列散落感
        parts = VGroup(
            cpu.shift(LEFT * 3.5 + UP * 2.2),
            gpu.shift(LEFT * 3.5 + UP * 0.8),
            mainboard.shift(LEFT * 3.5 + DOWN * 0.6),
            keyboard.shift(LEFT * 1.8 + UP * 1.5),
            mouse.shift(LEFT * 1.8 + UP * 0.1)
        )

        parts_label = Text("碎片化", font_size=32, color=BLUE).next_to(
            parts, DOWN, buff=0.6)

        # ========== 右侧：完整电脑（整体性） ==========
        computer = SVGMobject(
            "material/computer/computer.svg").scale(0.8).shift(RIGHT * 3.5)
        computer_label = Text("整体性", font_size=32, color=GREEN).next_to(
            computer, DOWN, buff=0.6)

        # ========== 中间：VS ==========
        vs = SVGMobject("material/vs.svg")

        # ========== 播放动画 ==========
        # 全部淡入，左右同时出现
        self.play(
            FadeIn(parts, shift=UP),
            FadeIn(parts_label, shift=UP),
            FadeIn(computer, shift=DOWN),
            FadeIn(computer_label, shift=DOWN),
            FadeIn(vs, scale=0.5)
        )
        self.wait(2)

        # 左右对抗动画：交替闪烁+向外扩张
        # 左侧亮起
        self.play(
            parts.animate.set_color(YELLOW),
            parts_label.animate.set_color(YELLOW),
            parts.animate.shift(LEFT * 0.2),
            run_time=0.8
        )
        self.play(
            parts.animate.set_color(WHITE),
            parts_label.animate.set_color(BLUE),
            parts.animate.shift(RIGHT * 0.2),
            run_time=0.8
        )

        # 右侧亮起
        self.play(
            computer.animate.set_color(YELLOW),
            computer_label.animate.set_color(YELLOW),
            computer.animate.shift(RIGHT * 0.2),
            run_time=0.8
        )
        self.play(
            computer.animate.set_color(WHITE),
            computer_label.animate.set_color(GREEN),
            computer.animate.shift(LEFT * 0.2),
            run_time=0.8
        )

        # VS 放大强调
        self.play(
            vs.animate.scale(1.5),
            run_time=0.5
        )
        self.play(
            vs.animate.scale(1 / 1.5),
            run_time=0.5
        )

        self.wait(2)
