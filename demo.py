# fmt: off
from manim import *
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
AI_PATH = "material/AI/"
# fmt: on


from manim import *


class AIMAKnowledgePath(Scene):

    def construct(self):
        self.camera.background_color = WHITE

        # ==================================================
        # ① 遇到问题
        # ==================================================

        question = SVGMobject(
            f"{MATH_PATH}question.svg"
        )
        question.scale(0.6)

        question_label = Text(
            "遇到问题",
            font_size=15,
            color=BLACK
        )
        question_label.next_to(
            question,
            DOWN,
            buff=0.25
        )

        question_group = VGroup(
            question,
            question_label
        )

        # ==================================================
        # ② 理解问题属于什么类型
        # ==================================================

        ml = SVGMobject(
            f"{AI_PATH}machine-learning.svg"
        )
        ml.scale(0.6)

        ml_label = Text(
            "机器学习问题",
            font_size=15,
            color=BLACK
        )
        ml_label.next_to(
            ml,
            DOWN,
            buff=0.25
        )

        ml_group = VGroup(
            ml,
            ml_label
        )

        # ==================================================
        # ③ 在 AI 知识地图中定位
        # ==================================================

        ai_map = SVGMobject(
            f"{SUNDRY_PATH}world-map.svg"
        )
        ai_map.scale(0.6)

        map_label = Text(
            "AI 知识地图",
            font_size=15,
            color=BLACK
        )
        map_label.next_to(
            ai_map,
            DOWN,
            buff=0.25
        )

        map_group = VGroup(
            ai_map,
            map_label
        )

        # ==================================================
        # ④ 对应领域的专门资料
        # ==================================================

        textbook = SVGMobject(
            "material/textbook.svg"
        )
        textbook.scale(0.2)

        textbook_label = Text(
            "教材",
            font_size=10,
            color=BLACK
        )
        textbook_label.next_to(
            textbook,
            DOWN,
            buff=0.18
        )

        textbook_group = VGroup(
            textbook,
            textbook_label
        )

        paper = SVGMobject(
            "material/paper.svg"
        )
        paper.scale(0.2)

        paper_label = Text(
            "论文",
            font_size=10,
            color=BLACK
        )
        paper_label.next_to(
            paper,
            DOWN,
            buff=0.18
        )

        paper_group = VGroup(
            paper,
            paper_label
        )

        course = SVGMobject(
            "material/lecture.svg"
        )
        course.scale(0.2)

        course_label = Text(
            "课程",
            font_size=10,
            color=BLACK
        )
        course_label.next_to(
            course,
            DOWN,
            buff=0.18
        )

        course_group = VGroup(
            course,
            course_label
        )

        # ==================================================
        # 位置
        # ==================================================

        question_group.move_to(LEFT * 5)

        ml_group.move_to(LEFT * 1.7)

        map_group.move_to(RIGHT * 1.8)

        textbook_group.move_to(
            RIGHT * 5.1 + UP * 1.5
        )

        paper_group.move_to(
            RIGHT * 5.1
        )

        course_group.move_to(
            RIGHT * 5.1 + DOWN * 1.5
        )

        # ==================================================
        # 箭头
        # ==================================================

        arrow1 = Arrow(
            question_group.get_right(),
            ml_group.get_left(),
            buff=0.35,
            stroke_width=4,
            color=GREY_B
        )

        arrow2 = Arrow(
            ml_group.get_right(),
            map_group.get_left(),
            buff=0.35,
            stroke_width=4,
            color=GREY_B
        )

        # 地图 → 三种资料
        arrow3 = Arrow(
            map_group.get_right(),
            textbook_group.get_left(),
            buff=0.35,
            stroke_width=4,
            color=GREY_B
        )

        arrow4 = Arrow(
            map_group.get_right(),
            paper_group.get_left(),
            buff=0.35,
            stroke_width=4,
            color=GREY_B
        )

        arrow5 = Arrow(
            map_group.get_right(),
            course_group.get_left(),
            buff=0.35,
            stroke_width=4,
            color=GREY_B
        )

        # ==================================================
        # 动画
        # ==================================================

        # --------------------------------------------------
        # ① 遇到问题
        # --------------------------------------------------

        self.play(
            FadeIn(question_group, scale=0.8),
            run_time=0.7
        )

        self.wait(0.4)

        # --------------------------------------------------
        # ② 理解问题属于什么类型
        # --------------------------------------------------

        self.play(
            GrowArrow(arrow1),
            FadeIn(ml_group, scale=0.8),
            run_time=0.8
        )

        self.wait(0.5)

        # --------------------------------------------------
        # ③ 在 AI 知识地图中定位
        # --------------------------------------------------

        self.play(
            GrowArrow(arrow2),
            FadeIn(map_group, scale=0.8),
            run_time=0.8
        )

        self.wait(0.5)

        # --------------------------------------------------
        # ④ 寻找对应领域的专门资料
        # --------------------------------------------------

        self.play(
            GrowArrow(arrow3),
            FadeIn(textbook_group, shift=LEFT * 0.3),
            run_time=0.5
        )

        self.play(
            GrowArrow(arrow4),
            FadeIn(paper_group, shift=LEFT * 0.3),
            run_time=0.5
        )

        self.play(
            GrowArrow(arrow5),
            FadeIn(course_group, shift=LEFT * 0.3),
            run_time=0.5
        )

        self.wait(1.5)