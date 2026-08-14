from manim import *


class AIResources(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # =========================
        # 1. 中央的 AI
        # =========================
        ai = Text(
            "AI",
            font_size=96,
            color=BLACK,
        )

        self.play(
            FadeIn(ai, scale=0.5),
            run_time=0.8,
        )

        self.wait(0.5)

        # =========================
        # 2. 周围的资源
        # =========================
        resources = [
            ("📚", "课程", UP * 2.7 + LEFT * 3.5),
            ("📝", "博客", LEFT * 5 + UP * 0.5),
            ("📄", "论文", RIGHT * 4.5 + UP * 1.5),
            ("▶", "视频", RIGHT * 5 + DOWN * 1.0),
            ("🤖", "开源模型", LEFT * 3.8 + DOWN * 2.5),
            ("🔧", "工具", RIGHT * 1.5 + DOWN * 2.8),
            ("💻", "开源项目", DOWN * 3.5),
        ]

        icons = VGroup()
        labels = VGroup()

        # =========================
        # 3. 一个一个出现
        # =========================
        for icon_text, label_text, position in resources:

            icon = Text(
                icon_text,
                font_size=48,
            )

            label = Text(
                label_text,
                font_size=28,
            )

            group = VGroup(icon, label)
            group.arrange(DOWN, buff=0.15)
            group.move_to(position)

            icons.add(icon)
            labels.add(label)

            # 从 AI 附近飞到最终位置
            group.move_to(ai.get_center())

            self.play(
                FadeIn(group, scale=0.3),
                group.animate.move_to(position),
                run_time=0.6,
            )

        self.wait(1)

        # =========================
        # 4. 中央 AI 淡出
        # =========================
        self.play(
            FadeOut(ai),
            run_time=1,
        )

        self.wait(2)