from manim import *


class AIMAMap(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # =========================
        # 统一样式
        # =========================
        text_color = BLACK

        def txt(content, size=36):
            return Text(
                content,
                font="Microsoft YaHei",
                font_size=size,
                color=text_color,
            )

        # =========================================================
        # 镜头 1：权威的教材不在少数，为什么选择 AIMA？
        # =========================================================

        title = txt("权威的教材不在少数", 42)
        title.to_edge(UP, buff=0.7)

        self.play(FadeIn(title))

        # 几本抽象的“教材”
        books = VGroup()

        for i in range(5):
            book = VGroup(
                Rectangle(
                    width=1.15,
                    height=2.0,
                    stroke_color=BLACK,
                    stroke_width=2,
                ),
                txt("AI", 28)
            )
            book[1].move_to(book[0].get_center())
            books.add(book)

        books.arrange(RIGHT, buff=0.35)
        books.move_to(ORIGIN + DOWN * 0.3)

        self.play(
            LaggedStart(
                *[FadeIn(book, shift=UP * 0.2) for book in books],
                lag_ratio=0.12
            )
        )

        question = txt("为什么选择 AIMA？", 38)
        question.next_to(books, DOWN, buff=0.65)

        self.play(FadeIn(question))

        self.wait(0.8)

        # 教材退开
        self.play(
            books.animate.scale(0.7).shift(LEFT * 3),
            question.animate.shift(DOWN * 0.4),
            run_time=0.8
        )

        # AIMA 出现
        aima = txt("AIMA", 64)
        aima.move_to(RIGHT * 2.3)

        self.play(
            FadeIn(aima, scale=1.3),
            run_time=0.8
        )

        self.wait(1)

        self.play(
            FadeOut(title),
            FadeOut(books),
            FadeOut(question),
            FadeOut(aima),
        )

        # =========================================================
        # 镜头 2：不是深入一个技术，而是看到整体
        # =========================================================

        aima_center = txt("AIMA", 64)
        aima_center.move_to(ORIGIN)

        self.play(FadeIn(aima_center))

        # 一个技术点
        point = Dot(radius=0.12, color=BLACK)
        point.next_to(aima_center, DOWN, buff=0.8)

        line = Line(
            aima_center.get_bottom(),
            point.get_top(),
            stroke_color=BLACK,
            stroke_width=2
        )

        label = txt("某一个 AI 技术", 30)
        label.next_to(point, DOWN, buff=0.35)

        self.play(
            FadeIn(point),
            Create(line),
            FadeIn(label)
        )

        # 深入
        depth_line = Line(
            point.get_bottom(),
            point.get_bottom() + DOWN * 1.2,
            stroke_color=BLACK,
            stroke_width=3
        )

        depth_text = txt("深入", 34)
        depth_text.next_to(depth_line, RIGHT, buff=0.25)

        self.play(
            Create(depth_line),
            FadeIn(depth_text)
        )

        self.wait(0.7)

        # 清除
        self.play(
            FadeOut(point),
            FadeOut(line),
            FadeOut(label),
            FadeOut(depth_line),
            FadeOut(depth_text),
        )

        # =========================================================
        # 从一个点扩展成整个领域
        # =========================================================

        center = Dot(radius=0.13, color=BLACK)
        center_label = txt("AI", 48)
        center_label.next_to(center, DOWN, buff=0.2)

        center_group = VGroup(center, center_label)

        self.play(
            Transform(aima_center, txt("AI", 64)),
            FadeIn(center_group)
        )

        # 周围的 AI 方向
        topics = [
            ("搜索", UP * 2.2),
            ("学习", RIGHT * 2.8 + UP * 1.2),
            ("推理", RIGHT * 3.0 + DOWN * 1.1),
            ("规划", RIGHT * 1.5 + DOWN * 2.3),
            ("知识表示", LEFT * 1.5 + DOWN * 2.3),
            ("NLP", LEFT * 3.0 + DOWN * 1.0),
            ("视觉", LEFT * 2.8 + UP * 1.2),
            ("强化学习", LEFT * 1.4 + UP * 2.3),
            ("智能体", RIGHT * 0.1 + DOWN * 2.8),
        ]

        topic_objects = VGroup()

        for name, position in topics:
            t = txt(name, 30)
            t.move_to(position)
            topic_objects.add(t)

        # 一个一个出现
        self.play(
            LaggedStart(
                *[
                    FadeIn(t, shift=(t.get_center() / 4))
                    for t in topic_objects
                ],
                lag_ratio=0.12
            ),
            run_time=2.5
        )

        self.wait(1)

        # =========================================================
        # 镜头 3：所有内容汇聚成“一张地图”
        # =========================================================

        map_box = RoundedRectangle(
            width=9.8,
            height=6.0,
            corner_radius=0.2,
            stroke_color=BLACK,
            stroke_width=2
        )

        map_title = txt("AIMA", 50)
        map_title.move_to(map_box.get_top() + DOWN * 0.55)

        subtitle = txt("人工智能的整体地图", 28)
        subtitle.next_to(map_title, DOWN, buff=0.15)

        # 地图中的内容
        map_topics = [
            "搜索",
            "学习",
            "推理",
            "规划",
            "知识表示",
            "NLP",
            "视觉",
            "强化学习",
            "智能体",
        ]

        map_topic_objects = VGroup()

        positions = [
            LEFT * 3.0 + UP * 1.2,
            LEFT * 1.0 + UP * 1.2,
            RIGHT * 1.2 + UP * 1.2,
            RIGHT * 3.0 + UP * 1.2,

            LEFT * 2.5 + DOWN * 0.3,
            LEFT * 0.5 + DOWN * 0.3,
            RIGHT * 1.4 + DOWN * 0.3,

            LEFT * 1.6 + DOWN * 1.7,
            RIGHT * 1.7 + DOWN * 1.7,
        ]

        for name, pos in zip(map_topics, positions):
            t = txt(name, 28)
            t.move_to(pos)
            map_topic_objects.add(t)

        self.play(
            FadeOut(center_group),
            FadeOut(aima_center),
            FadeOut(topic_objects),
        )

        self.play(
            Create(map_box),
            FadeIn(map_title),
            FadeIn(subtitle),
            run_time=1
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(t, scale=0.8)
                    for t in map_topic_objects
                ],
                lag_ratio=0.1
            ),
            run_time=1.8
        )

        self.wait(1.5)

        # =========================================================
        # 镜头 4：最终只留下 AIMA
        # =========================================================

        self.play(
            FadeOut(map_topic_objects),
            FadeOut(subtitle),
            map_box.animate.scale(0.75),
            map_title.animate.scale(1.25),
            run_time=1
        )

        self.wait(0.5)

        final_text = txt("把不同的 AI 内容，放到同一张地图上", 34)
        final_text.next_to(map_box, DOWN, buff=0.6)

        self.play(FadeIn(final_text))

        self.wait(2)
