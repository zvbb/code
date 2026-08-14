from custom.edg_tts import EdgeTTSService
from manim_voiceover.services.openai import OpenAIService
from kokoro_mv import KokoroService
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover import VoiceoverScene
from manim import *

# ============================================================
# 全局视觉风格
# ============================================================

BG = WHITE
TEXT = BLACK
GRAY = GREY_B
LIGHT_GRAY = GREY_C
PRIMARY = BLUE
ACCENT = ORANGE


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


class Group1(VoiceoverScene):

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
        self._section_04()

        self.next_section("05")
        self._section05()

        self.next_section("06")
        self._section06()

    def _section01(self):
        # 中央 AI
        ai = Text(
            "AI",
            font_size=100,
            weight=BOLD,
            color=PRIMARY
        )

        # 周围的知识方向
        topics = [
            ("Machine Learning", UP * 2.5),
            ("Computer Vision", LEFT * 3.2 + UP * 0.8),
            ("NLP", RIGHT * 3.2 + UP * 0.8),
            ("Reinforcement Learning", DOWN * 2.5),
            ("Robotics", LEFT * 3.2 + DOWN * 1.5),
            ("Knowledge", RIGHT * 3.2 + DOWN * 1.5),
        ]

        topic_mobs = VGroup()

        for text, pos in topics:

            mob = Text(
                text,
                font_size=28,
                color=TEXT
            )

            mob.move_to(pos)
            topic_mobs.add(mob)

        with self.voiceover(text="如果想系统地学习人工智能，那么第一个问题是：") as tracker:
            self.play(
                FadeIn(ai, scale=1.5),
            )
            # 知识方向逐渐出现
            self.play(
                LaggedStart(
                    *[
                        FadeIn(m, scale=0.7)
                        for m in topic_mobs
                    ],
                    lag_ratio=0.15
                )
            )

            # 全部消失
            self.play(
                FadeOut(topic_mobs),
                FadeOut(ai),
            )

        # 提出问题
        question = Text(
            "应该从哪里开始?",
            font_size=100,
            weight=BOLD,
            color=TEXT
        )

        with self.voiceover(text="应该从哪里开始?"):
            self.play(
                FadeIn(question, scale=0.5),
                run_time=0.8
            )

            self.play(
                question.animate.scale(1.15),
                run_time=1
            )
            self.play(FadeOut(question))

    def _section02(self):
        # 中央 AI
        ai = Text(
            "AI",
            font_size=90,
            weight=BOLD,
            color=PRIMARY
        )

        # 第一圈
        items1 = [
            ("课程", UP * 2.3),
            ("博客", LEFT * 3.0),
            ("论文", RIGHT * 3.0),
            ("视频", DOWN * 2.3),
        ]

        mobs1 = VGroup()

        for text, pos in items1:
            mob = Text(
                text,
                font_size=38,
                color=TEXT
            )

            mob.move_to(pos)
            mobs1.add(mob)
        # 第二圈
        items2 = [
            ("开源模型", UP * 3.3 + LEFT * 2.5),
            ("开源工具", UP * 3.3 + RIGHT * 2.5),
            ("RAG", LEFT * 4 + DOWN * 1),
            ("Agent", RIGHT * 4 + DOWN * 1),
            ("LLM", DOWN * 3.5 + LEFT * 2),
            ("Framework", DOWN * 3.5 + RIGHT * 2),
        ]

        mobs2 = VGroup()

        for text, pos in items2:
            mob = Text(
                text,
                font_size=28,
                color=TEXT
            )

            mob.move_to(pos)
            mobs2.add(mob)

        # 更多技术
        more = VGroup(
            Text("Transformer", font_size=25, color=GRAY),
            Text("Diffusion", font_size=25, color=GRAY),
            Text("Embedding", font_size=25, color=GRAY),
            Text("Vector DB", font_size=25, color=GRAY),
            Text("Fine-tuning", font_size=25, color=GRAY),
            Text("Multimodal", font_size=25, color=GRAY),
        )

        more.arrange_in_grid(
            rows=2,
            cols=3,
            buff=0.6
        )

        more.move_to(DOWN * 0.2)

        # 信息越来越多
        all_items = VGroup(
            ai,
            mobs1,
            mobs2,
            more
        )

        with self.voiceover(text="""今天学习 AI 的门槛已经很低了。
网上有大量的课程、博客、论文、视频，以及各种开源模型和工具。
我们很容易学会如何调用模型、搭建 RAG，甚至训练神经网络。但信息越多，也越容易陷入碎片化。"""):
            self.play(
                FadeIn(ai, scale=1.4),
                run_time=0.8
            )
            self.wait(2)

            self.play(
                LaggedStart(
                    *[
                        FadeIn(m, scale=0.7)
                        for m in mobs1
                    ],
                    lag_ratio=0.15
                ),
                run_time=1.5
            )
            self.wait(2)

            self.play(
                LaggedStart(
                    *[
                        FadeIn(m, scale=0.5)
                        for m in mobs2
                    ],
                    lag_ratio=0.1
                ),
                run_time=2
            )

            self.wait(2)

            self.play(
                LaggedStart(
                    *[
                        FadeIn(m, scale=0.5)
                        for m in more
                    ],
                    lag_ratio=0.08
                ),
                run_time=1.5
            )

            self.play(
                all_items.animate.scale(0.7),
                run_time=1
            )
        self.clear()

    def _section03(self):
        # ============================================================
        # 第一幕：脑袋 + 零散的 AI 概念
        # ============================================================

        brain = ImageMobject("img/brain.png")
        brain.scale(0.8)
        brain.move_to(ORIGIN)

        # 创建概念标签
        machine_learning = self.make_label("机器学习")
        neural_network = self.make_label("神经网络")
        deep_learning = self.make_label("深度学习")
        probability = self.make_label("概率")
        reinforcement = self.make_label("强化学习")
        transformer = self.make_label("Transformer")

        # 第一幕的位置
        machine_learning.move_to(UP * 2.6)

        neural_network.move_to(
            LEFT * 2.8 + UP * 1.2
        )

        deep_learning.move_to(
            RIGHT * 2.8 + UP * 1.2
        )

        probability.move_to(
            LEFT * 2.5 + DOWN * 1.3
        )

        reinforcement.move_to(
            RIGHT * 2.8 + DOWN * 1.3
        )

        transformer.move_to(
            DOWN * 2.5
        )

        concepts = VGroup(
            machine_learning,
            neural_network,
            deep_learning,
            probability,
            reinforcement,
            transformer,
        )

        new_tech = self.make_new_label()
        new_tech.move_to(RIGHT * 5.2)

        # 脑袋出现
        self.play(
            FadeIn(brain, scale=0.8),
            run_time=1
        )

        # 概念一个个出现
        with self.voiceover(text="""
            我们脑海中可能有许多概念和算法，却不知道它们之间的关系，
        """):
            self.play(
                LaggedStart(
                    *[
                        FadeIn(x, shift=UP * 0.2)
                        for x in concepts
                    ],
                    lag_ratio=0.15,
                ),
                run_time=2
            )
        with self.voiceover(text="""更不知道一种新技术在整个 AI 领域中处于什么位置。"""):
            self.play(
                FadeIn(new_tech, shift=RIGHT),
                run_time=0.8,
            )
        # 脑袋消失
        self.play(
            FadeOut(brain),
            FadeOut(new_tech),
            run_time=0.6
        )

        # ============================================================
        # 第二幕
        # 教材出现
        # ============================================================

        # 教材
        book = self.make_book()

        book.move_to(
            LEFT * 4.8
        )

        # ============================================================
        # 第二幕的知识结构位置
        # ============================================================

        # 最终布局：
        #
        #              概率
        #               │
        #               ↓
        #            机器学习
        #               │
        #          ┌────┴────┐
        #          ↓         ↓
        #       深度学习    强化学习
        #          │
        #          ↓
        #       神经网络
        #          │
        #          ↓
        #      Transformer

        target = {}

        target["probability"] = (
            RIGHT * 0.2 + UP * 2.8
        )

        target["machine_learning"] = (
            RIGHT * 0.2 + UP * 1.4
        )

        target["deep_learning"] = (
            LEFT * 1.2 + DOWN * 0.1
        )

        target["reinforcement"] = (
            RIGHT * 1.8 + DOWN * 0.1
        )

        target["neural_network"] = (
            LEFT * 1.2 + DOWN * 1.5
        )

        target["transformer"] = (
            LEFT * 1.2 + DOWN * 2.8
        )

        # ============================================================
        # 概念重新排列
        # ============================================================
        with self.voiceover(text="""所以，如果我们真正想理解人工智能，而不仅仅是追逐热门技术，一个重要的方法就是：
以权威教材为主线，建立知识框架。"""):
            self.play(
                FadeIn(book, shift=RIGHT),
                run_time=1
            )
            self.play(
                probability.animate.move_to(
                    target["probability"]
                ),

                machine_learning.animate.move_to(
                    target["machine_learning"]
                ),

                deep_learning.animate.move_to(
                    target["deep_learning"]
                ),

                reinforcement.animate.move_to(
                    target["reinforcement"]
                ),

                neural_network.animate.move_to(
                    target["neural_network"]
                ),

                transformer.animate.move_to(
                    target["transformer"]
                ),

                run_time=2.5,
                rate_func=smooth,
            )

            # ============================================================
            # 画知识之间的关系
            # ============================================================

            line1 = Arrow(
                probability.get_bottom(),
                machine_learning.get_top(),
                buff=0.15,
                stroke_width=2.5,
                color=GRAY,
                max_tip_length_to_length_ratio=0.15,
            )

            line2 = Arrow(
                machine_learning.get_bottom(),
                deep_learning.get_top(),
                buff=0.15,
                stroke_width=2.5,
                color=GRAY,
                max_tip_length_to_length_ratio=0.15,
            )

            line3 = Arrow(
                machine_learning.get_bottom(),
                reinforcement.get_top(),
                buff=0.15,
                stroke_width=2.5,
                color=GRAY,
                max_tip_length_to_length_ratio=0.15,
            )

            line4 = Arrow(
                deep_learning.get_bottom(),
                neural_network.get_top(),
                buff=0.15,
                stroke_width=2.5,
                color=GRAY,
                max_tip_length_to_length_ratio=0.15,
            )

            line5 = Arrow(
                neural_network.get_bottom(),
                transformer.get_top(),
                buff=0.15,
                stroke_width=2.5,
                color=GRAY,
                max_tip_length_to_length_ratio=0.15,
            )

            # 连线逐个出现
            self.play(
                Create(line1),
                run_time=0.4
            )

            self.play(
                Create(line2),
                Create(line3),
                run_time=0.6
            )

            self.play(
                Create(line4),
                run_time=0.4
            )

            self.play(
                Create(line5),
                run_time=0.4
            )
        self.clear()

    def _section_04(self):
        with self.voiceover(text="""用整体性的思维，对抗信息的碎片化。"""):
            # =========================
            # 颜色
            # =========================
            dark = "#333333"
            blue = "#4A90E2"
            light_blue = "#DCEEFF"

            # =========================
            # 创建机甲零件
            # =========================

            # 头
            head = VGroup(
                RoundedRectangle(
                    width=1.15,
                    height=0.8,
                    corner_radius=0.12,
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
                Circle(
                    radius=0.09,
                    color=blue,
                    fill_opacity=1,
                ).shift(LEFT * 0.22),
                Circle(
                    radius=0.09,
                    color=blue,
                    fill_opacity=1,
                ).shift(RIGHT * 0.22),
            )

            # 身体
            body = VGroup(
                Polygon(
                    [-0.75, 0.75, 0],
                    [0.75, 0.75, 0],
                    [0.6, -0.75, 0],
                    [-0.6, -0.75, 0],
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
                Line(
                    LEFT * 0.4,
                    RIGHT * 0.4,
                    color=blue,
                    stroke_width=5,
                ),
            )

            # 肩膀
            left_shoulder = Circle(
                radius=0.22,
                color=dark,
                fill_color=light_blue,
                fill_opacity=1,
                stroke_width=4,
            )

            right_shoulder = Circle(
                radius=0.22,
                color=dark,
                fill_color=light_blue,
                fill_opacity=1,
                stroke_width=4,
            )

            # 左臂
            left_arm = VGroup(
                RoundedRectangle(
                    width=0.42,
                    height=1.15,
                    corner_radius=0.08,
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
                Circle(
                    radius=0.16,
                    color=dark,
                    fill_color=WHITE,
                    fill_opacity=1,
                    stroke_width=3,
                ),
            )

            # 右臂
            right_arm = VGroup(
                RoundedRectangle(
                    width=0.42,
                    height=1.15,
                    corner_radius=0.08,
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
                Circle(
                    radius=0.16,
                    color=dark,
                    fill_color=WHITE,
                    fill_opacity=1,
                    stroke_width=3,
                ),
            )

            # 左腿
            left_leg = VGroup(
                RoundedRectangle(
                    width=0.48,
                    height=1.25,
                    corner_radius=0.08,
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
                Polygon(
                    [-0.3, -0.55, 0],
                    [0.3, -0.55, 0],
                    [0.42, -0.95, 0],
                    [-0.42, -0.95, 0],
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
            )

            # 右腿
            right_leg = VGroup(
                RoundedRectangle(
                    width=0.48,
                    height=1.25,
                    corner_radius=0.08,
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
                Polygon(
                    [-0.3, -0.55, 0],
                    [0.3, -0.55, 0],
                    [0.42, -0.95, 0],
                    [-0.42, -0.95, 0],
                    stroke_color=dark,
                    stroke_width=4,
                    fill_color=light_blue,
                    fill_opacity=1,
                ),
            )

            # =========================
            # 统一缩放
            # =========================

            for part in [
                head,
                body,
                left_arm,
                right_arm,
                left_leg,
                right_leg,
            ]:
                part.scale(0.9)

            # =========================
            # 中央最终位置
            # =========================

            center = ORIGIN

            head_target = center + UP * 2.15
            body_target = center + UP * 0.55

            left_shoulder_target = center + LEFT * 1.05 + UP * 1.15
            right_shoulder_target = center + RIGHT * 1.05 + UP * 1.15

            left_arm_target = center + LEFT * 1.35 + UP * 0.25
            right_arm_target = center + RIGHT * 1.35 + UP * 0.25

            left_leg_target = center + LEFT * 0.42 + DOWN * 1.0
            right_leg_target = center + RIGHT * 0.42 + DOWN * 1.0

            # =========================
            # 初始：零件散落在整个画面
            # =========================

            head.move_to(LEFT * 4.5 + UP * 2.5)
            head.rotate(-PI / 5)

            body.move_to(RIGHT * 4.3 + DOWN * 1.5)
            body.rotate(PI / 7)

            left_shoulder.move_to(LEFT * 2.2 + DOWN * 2.5)

            right_shoulder.move_to(RIGHT * 3.8 + UP * 2.3)

            left_arm.move_to(LEFT * 4.5 + UP * 0.2)
            left_arm.rotate(PI / 3)

            right_arm.move_to(RIGHT * 4.5 + DOWN * 0.5)
            right_arm.rotate(-PI / 3)

            left_leg.move_to(LEFT * 1.8 + DOWN * 3.0)
            left_leg.rotate(-PI / 5)

            right_leg.move_to(RIGHT * 1.8 + UP * 2.8)
            right_leg.rotate(PI / 4)

            parts = VGroup(
                head,
                body,
                left_shoulder,
                right_shoulder,
                left_arm,
                right_arm,
                left_leg,
                right_leg,
            )

            # =========================
            # 第一阶段：碎片出现
            # =========================

            self.play(
                LaggedStart(
                    *[
                        FadeIn(part, shift=UP * 0.15)
                        for part in parts
                    ],
                    lag_ratio=0.08,
                ),
                run_time=1.2,
            )

            self.wait(0.5)

            # =========================
            # 第二阶段：
            # 所有碎片向中央汇聚
            # =========================

            self.play(
                head.animate
                    .move_to(head_target)
                    .rotate(PI / 5),

                body.animate
                    .move_to(body_target)
                    .rotate(-PI / 7),

                left_shoulder.animate
                    .move_to(left_shoulder_target),

                right_shoulder.animate
                    .move_to(right_shoulder_target),

                left_arm.animate
                    .move_to(left_arm_target)
                    .rotate(-PI / 3),

                right_arm.animate
                    .move_to(right_arm_target)
                    .rotate(PI / 3),

                left_leg.animate
                    .move_to(left_leg_target)
                    .rotate(PI / 5),

                right_leg.animate
                    .move_to(right_leg_target)
                    .rotate(-PI / 4),

                run_time=2.2,
                rate_func=smooth,
            )

            self.wait(0.5)

            # =========================
            # 第三阶段：
            # 整体轻微强调
            # =========================

            robot = VGroup(
                head,
                body,
                left_shoulder,
                right_shoulder,
                left_arm,
                right_arm,
                left_leg,
                right_leg,
            )

            self.play(
                robot.animate.scale(1.05),
                run_time=0.3,
            )

            self.play(
                robot.animate.scale(1 / 1.05),
                run_time=0.3,
            )

            self.wait(1)
        self.clear()

    def _section05(self):
        with self.voiceover(text="当然，这种学习方式的代价也很明显：那就是学习速度比较慢!"):
            DARK = "#333333"
            ROAD = "#E5E5E5"
            SKIN = "#F2C6A0"
            CLOTH = "#DCEEFF"
            GRAY = "#777777"

            # =====================================================
            # 1. 道路
            #
            # 从左下方延伸到右上方
            # 越往右上越窄
            # =====================================================

            road = Polygon(
                LEFT * 5.0 + DOWN * 2.8,
                LEFT * 3.7 + DOWN * 2.8,

                RIGHT * 4.5 + UP * 2.4,
                RIGHT * 5.0 + UP * 2.4,

                stroke_color=ROAD,
                stroke_width=2,
                fill_color=ROAD,
                fill_opacity=1,
            )

            # 道路左边缘
            left_edge = Line(
                LEFT * 5.0 + DOWN * 2.8,
                RIGHT * 4.5 + UP * 2.4,
                color=DARK,
                stroke_width=3,
            )

            # 道路右边缘
            right_edge = Line(
                LEFT * 3.7 + DOWN * 2.8,
                RIGHT * 5.0 + UP * 2.4,
                color=DARK,
                stroke_width=3,
            )

            # =====================================================
            # 道路中心虚线
            # =====================================================

            center_marks = VGroup()

            for start, end in [
                (LEFT * 4.0 + DOWN * 2.8,
                 LEFT * 3.0 + DOWN * 2.2),

                (LEFT * 2.4 + DOWN * 1.9,
                 LEFT * 1.8 + DOWN * 1.5),

                (LEFT * 1.2 + DOWN * 1.2,
                 LEFT * 0.8 + DOWN * 0.9),

                (LEFT * 0.3 + DOWN * 0.65,
                 LEFT * 0.05 + DOWN * 0.45),

                (RIGHT * 0.35 + DOWN * 0.15,
                 RIGHT * 0.48 + UP * 0.05),
            ]:
                center_marks.add(
                    Line(
                        start,
                        end,
                        color=WHITE,
                        stroke_width=5,
                    )
                )

            road_group = VGroup(
                road,
                left_edge,
                right_edge,
                center_marks,
            )

            # =====================================================
            # 2. 老人
            # =====================================================

            # -----------------------------------------------------
            # 身体
            # -----------------------------------------------------

            body = RoundedRectangle(
                width=0.65,
                height=0.95,
                corner_radius=0.10,
                stroke_color=DARK,
                stroke_width=3,
                fill_color=CLOTH,
                fill_opacity=1,
            )

            # 驼背
            body.rotate(-PI / 14)

            # -----------------------------------------------------
            # 头
            # -----------------------------------------------------

            head = Circle(
                radius=0.30,
                stroke_color=DARK,
                stroke_width=3,
                fill_color=SKIN,
                fill_opacity=1,
            )

            head.move_to(
                body.get_top()
                + UP * 0.28
                + RIGHT * 0.05
            )

            # -----------------------------------------------------
            # 白头发
            # -----------------------------------------------------

            hair = Arc(
                radius=0.25,
                start_angle=0,
                angle=PI,
                color=GRAY,
                stroke_width=5,
            )

            hair.move_to(
                head.get_center() + UP * 0.04
            )

            # -----------------------------------------------------
            # 眼睛
            # -----------------------------------------------------

            eye = Dot(
                head.get_center()
                + RIGHT * 0.14
                + UP * 0.05,
                radius=0.025,
                color=DARK,
            )

            # -----------------------------------------------------
            # 鼻子
            # -----------------------------------------------------

            nose = Line(
                head.get_center()
                + RIGHT * 0.22
                + UP * 0.01,

                head.get_center()
                + RIGHT * 0.30,

                color=DARK,
                stroke_width=2,
            )

            face = VGroup(
                head,
                hair,
                eye,
                nose,
            )

            # =====================================================
            # 3. 手臂
            # =====================================================

            back_arm = Line(
                body.get_left() + UP * 0.25,
                body.get_left()
                + LEFT * 0.18
                + DOWN * 0.30,
                color=DARK,
                stroke_width=5,
            )

            front_arm = Line(
                body.get_right() + UP * 0.25,
                body.get_right()
                + RIGHT * 0.22
                + DOWN * 0.25,
                color=DARK,
                stroke_width=5,
            )

            # =====================================================
            # 4. 腿
            # =====================================================

            back_leg = Line(
                body.get_bottom() + LEFT * 0.12,
                body.get_bottom()
                + LEFT * 0.20
                + DOWN * 0.65,
                color=DARK,
                stroke_width=6,
            )

            front_leg = Line(
                body.get_bottom() + RIGHT * 0.12,
                body.get_bottom()
                + RIGHT * 0.22
                + DOWN * 0.65,
                color=DARK,
                stroke_width=6,
            )

            # =====================================================
            # 5. 拐杖
            # =====================================================

            cane_stick = Line(
                front_arm.get_end()
                + RIGHT * 0.05,

                front_arm.get_end()
                + RIGHT * 0.18
                + DOWN * 0.95,

                color=GRAY,
                stroke_width=4,
            )

            cane_handle = Arc(
                radius=0.10,
                start_angle=PI / 2,
                angle=PI,
                color=GRAY,
                stroke_width=4,
            )

            cane_handle.move_to(
                cane_stick.get_start()
                + UP * 0.01
            )

            cane = VGroup(
                cane_stick,
                cane_handle,
            )

            # =====================================================
            # 6. 老人整体
            # =====================================================

            old_man = VGroup(
                face,
                body,
                back_arm,
                front_arm,
                back_leg,
                front_leg,
                cane,
            )

            old_man.scale(0.8)

            # 放在道路左下方
            old_man.move_to(
                LEFT * 2.8
                + DOWN * 1.6
            )

            # =====================================================
            # 7. 道路出现
            # =====================================================

            self.play(
                FadeIn(road_group),
            )

            # =====================================================
            # 8. 老人出现
            # =====================================================

            self.play(
                FadeIn(old_man),
            )

            # =====================================================
            # 9. 第一步
            # =====================================================

            self.play(
                front_leg.animate.rotate(
                    -PI / 8,
                    about_point=front_leg.get_start(),
                ),

                back_leg.animate.rotate(
                    PI / 12,
                    about_point=back_leg.get_start(),
                ),
                rate_func=smooth,
            )

            # 沿道路方向：右上
            self.play(
                old_man.animate.shift(
                    RIGHT * 0.45 + UP * 0.25
                ),

                run_time=2.0,
                rate_func=smooth,
            )

            self.play(
                front_leg.animate.rotate(
                    PI / 8,
                    about_point=front_leg.get_start(),
                ),

                back_leg.animate.rotate(
                    -PI / 12,
                    about_point=back_leg.get_start(),
                ),

                run_time=1.2,
                rate_func=smooth,
            )

            self.wait(0.6)

            # =====================================================
            # 10. 第二步
            # =====================================================

            self.play(
                back_leg.animate.rotate(
                    -PI / 8,
                    about_point=back_leg.get_start(),
                ),

                front_leg.animate.rotate(
                    PI / 12,
                    about_point=front_leg.get_start(),
                ),

                run_time=1.5,
                rate_func=smooth,
            )

            self.play(
                old_man.animate.shift(
                    RIGHT * 0.45 + UP * 0.25
                ),

                run_time=2.0,
                rate_func=smooth,
            )

            self.play(
                back_leg.animate.rotate(
                    PI / 8,
                    about_point=back_leg.get_start(),
                ),

                front_leg.animate.rotate(
                    -PI / 12,
                    about_point=front_leg.get_start(),
                ),

                run_time=1.2,
                rate_func=smooth,
            )
        self.clear()

    def _section06(self):
        DARK = "#333333"
        BLUE = "#4A90E2"
        GRAY = "#888888"

        # =========================================================
        # 1. 长期的理解能力 > 学习速度
        # =========================================================

        long_term = Text(
            "长期的理解能力",
            font="Microsoft YaHei",
            font_size=52,
            color=DARK,
        )

        greater = Text(
            ">",
            font="Arial",
            font_size=68,
            color=BLUE,
            weight=BOLD,
        )

        speed = Text(
            "学习速度",
            font="Microsoft YaHei",
            font_size=52,
            color=GRAY,
        )

        comparison = VGroup(
            long_term,
            greater,
            speed,
        ).arrange(
            RIGHT,
            buff=0.45,
        )

        comparison.move_to(ORIGIN)

        with self.voiceover(text="""我们牺牲短期的学习速度，换取长期的理解能力。"""):
            # 出现
            self.play(
                FadeIn(long_term, shift=UP * 0.2),
                FadeIn(speed, shift=DOWN * 0.2),
                run_time=0.8,
            )

            self.play(
                FadeIn(greater, scale=0.6),
                run_time=0.5,
            )

            self.wait(0.8)

            # 强调长期理解能力
            self.play(
                long_term.animate.scale(1.12),
                speed.animate.scale(0.90),
                run_time=0.5,
            )

            self.wait(1)

            # 淡出
            self.play(
                FadeOut(comparison),
                run_time=0.6,
            )

        # =========================================================
        # 2. 以不变应万变
        #
        # 只显示文字，不加任何图形
        # =========================================================

        unchanging = Text(
            "以不变应万变",
            font="Microsoft YaHei",
            font_size=68,
            color=DARK,
        )
        unchanging.move_to(ORIGIN)
        with self.voiceover(text="""而 AI 尤其适合这种学习方式——具体的模型和技术会不断变化，
                            但背后的问题、思想和方法却具有更强的稳定性。"""):
            self.play(
                FadeIn(unchanging, scale=0.7),
                run_time=0.8,
            )

            self.wait(1.5)

            # 轻微强调
            self.play(
                unchanging.animate.scale(1.08),
                run_time=0.35,
            )

            self.play(
                unchanging.animate.scale(1 / 1.08),
                run_time=0.35,
            )

            self.wait(0.8)

            self.play(
                FadeOut(unchanging),
                run_time=0.6,
            )
        # =========================================================
        # 3. 慢 = 快
        # =========================================================

        slow = Text(
            "慢",
            font="Microsoft YaHei",
            font_size=82,
            color=GRAY,
        )

        equal = Text(
            "=",
            font="Arial",
            font_size=72,
            color=DARK,
            weight=BOLD,
        )

        fast = Text(
            "快",
            font="Microsoft YaHei",
            font_size=82,
            color=BLUE,
        )

        slow_fast = VGroup(
            slow,
            equal,
            fast,
        ).arrange(
            RIGHT,
            buff=0.5,
        )

        slow_fast.move_to(ORIGIN)

        with self.voiceover(text="""有时候，慢就是快。"""):
            self.play(
                FadeIn(slow),
                run_time=0.5,
            )

            self.play(
                FadeIn(equal, scale=0.5),
                run_time=0.4,
            )

            self.play(
                FadeIn(fast),
                run_time=0.5,
            )

            # 强调等号
            self.play(
                equal.animate.scale(1.25),
                run_time=0.35,
            )

            self.play(
                equal.animate.scale(1 / 1.25),
                run_time=0.35,
            )

            self.play(
                FadeOut(slow_fast),
                run_time=0.6,
            )

        # =========================================================
        # 4. AIMA 封面
        #
        # 将 AIMA_cover.png 放到当前 py 文件同目录
        # =========================================================

        cover = ImageMobject("img/aima.jpg")

        # 根据实际封面比例调整
        cover.height = 5.6

        cover.move_to(ORIGIN)

        # 初始透明
        cover.set_opacity(0)
        with self.voiceover(text="""所以，这个系列将以经典教材《Artificial Intelligence: A Modern Approach》，
                            也就是我们通常所说的AIMA，作为第一本书。"""):
            self.play(
                cover.animate.set_opacity(1),
                run_time=1.2,
            )

    def make_label(self, text):
        text_obj = Text(
            text,
            font="FangSong",
            font_size=28,
            color=BLACK,
        )
        return text_obj

    def make_new_label(self):

        new_tech = Text(
            "新技术",
            font="KaiTi",
            font_size=36,
            color=BLACK,
        )

        box = RoundedRectangle(
            width=new_tech.width + 0.6,
            height=new_tech.height + 0.35,
            corner_radius=0.15,
            stroke_width=4,
            color=RED,
            fill_color=WHITE,
            fill_opacity=1,
        )

        box.move_to(new_tech)

        return VGroup(box, new_tech)

    # ================================================================
    # 创建教材
    # ================================================================

    def make_book(self):

        cover = RoundedRectangle(
            width=2.0,
            height=3.0,
            corner_radius=0.12,
            stroke_width=3,
            color=BLACK,
            fill_color=WHITE,
            fill_opacity=1,
        )

        title = Text(
            "人工智能",
            font="FangSong",
            font_size=28,
            color=BLACK,
        )

        subtitle = Text(
            "权威教材",
            font="FangSong",
            font_size=20,
            color=GRAY,
        )

        title.move_to(
            cover.get_center() + UP * 0.35
        )

        subtitle.move_to(
            cover.get_center() + DOWN * 0.35
        )

        return VGroup(
            cover,
            title,
            subtitle
        )
