# fmt: off
import sys
from pathlib import Path
# 获取项目根目录（假设 chapter1 在项目根目录下）
project_root = Path(__file__).parent.parent  # 上一级目录
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
from custom.edg_tts import EdgeTTSService
from manim_voiceover import VoiceoverScene
from manim import *
# fmt: on

# ============================================================
# 全局视觉风格
# ============================================================

BG = WHITE
ASSET_PATH = "chapter1/asset/"
SVG_DIR = "material"
SUNDRY_PATH = "material/sundry/"
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
FIGURE_PATH = "material/figure/"
AI_PATH = "material/ai/"
BODY_PATH = "material/body/"
FACE_PATH = f"{BODY_PATH}face/"
EMOJI_PATH = "material/emoji/"


class Group4(VoiceoverScene):

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
        self._section04()
        self.next_section("05")
        self._section05()
        self.next_section("06")
        self._section06()
        self.next_section("07")
        self._section07()
        self.next_section("08")
        self._section08()
        self.next_section("09")
        self._section09()
        self.next_section("10")
        self._section10()
        self.next_section("11")
        self._section11()
        self.next_section("12")
        self._section12()
        self.next_section("13")
        self._section13()

    def _fade_out(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def _section01(self):
        chapter1 = ImageMobject(
            "chapter1/asset/chapter1.png"
        )
        self.play(
            FadeIn(chapter1, scale=0.6),
        )
        self.wait(1)
        self.clear()

    def _section02(self):
        with self.voiceover(text="在地球上，谁拥有最强的智能？"):
            # 左边：提问题的人
            person = SVGMobject(f"{MATH_PATH}question.svg")
            person.scale(2.2)
            person.move_to(LEFT * 3.2)

            # 右边：问题图片
            question = ImageMobject("chapter1/asset/question5-1.png")
            question.scale(0.6)
            question.move_to(RIGHT * 2.5)

            # 动画出现
            self.play(
                FadeIn(person, shift=RIGHT * 0.3),
                FadeIn(question, shift=LEFT * 0.3),
            )
        self.clear()

    def _section03(self):
        with self.voiceover(text="""答案没有什么悬念：就是我们人类。"""):
            self.wait(1.5)
            human = ImageMobject(f"{BODY_PATH}human.png")
            self.play(
                FadeIn(human),
            )
        self.clear()

    def _section04(self):
        with self.voiceover(text="""人类今天所创造的一切文明成果，从某种意义上说，都是人类智能的产物。"""):
            # =========================
            # 颜色
            # =========================
            TEXT_COLOR = "#333333"

            # =========================
            # 中间：人脑
            # =========================
            brain = SVGMobject(f"{BODY_PATH}brain.svg")
            brain.set_height(2.2)
            brain.move_to(ORIGIN)

            brain_label = Text(
                "人类智能",
                font_size=15,
                color=TEXT_COLOR
            )
            brain_label.next_to(
                brain,
                DOWN,
                buff=0.25
            )

            # =========================
            # 先出现人脑
            # =========================
            self.play(
                FadeIn(brain, scale=0.8),
                FadeIn(brain_label, shift=UP * 0.2),
                run_time=1
            )

            self.wait(0.5)

            # =========================
            # 四周文明成果
            # =========================
            items = [
                {
                    "file": f"{MATH_PATH}book.svg",
                    "label": "书籍",
                    "pos": UP * 3.0,
                },
                {
                    "file": f"{SUNDRY_PATH}art.svg",
                    "label": "艺术",
                    "pos": LEFT * 4.0 + UP * 1.3,
                },
                {
                    "file": f"{SUNDRY_PATH}building.svg",
                    "label": "建筑",
                    "pos": RIGHT * 4.0 + UP * 1.3,
                },
                {
                    "file": f"{SUNDRY_PATH}factory.svg",
                    "label": "工业",
                    "pos": RIGHT * 4.0 + DOWN * 1.5,
                },
                {
                    "file": f"{SUNDRY_PATH}flight.svg",
                    "label": "航天",
                    "pos": LEFT * 4.0 + DOWN * 1.5,
                },
            ]

            # =========================
            # 依次出现文明成果
            # =========================
            for item in items:

                icon = SVGMobject(item["file"])
                icon.set_height(0.5)
                icon.move_to(item["pos"])

                label = Text(
                    item["label"],
                    font_size=13,
                    color=TEXT_COLOR
                )
                label.next_to(
                    icon,
                    DOWN,
                    buff=0.18
                )

                self.play(
                    FadeIn(icon, scale=0.7),
                    FadeIn(label, shift=UP * 0.15),
                    run_time=0.7
                )

                self.wait(0.25)

            # =========================
            # 省略号 SVG
            # =========================
            dots = SVGMobject(
                f"{MATH_PATH}dot-cross.svg"
            )
            dots.set_height(0.2)
            dots.move_to(DOWN * 3.25)

            self.play(
                FadeIn(dots, scale=0.7),
                run_time=0.6
            )
        self.clear()

    def _section05(self):
        with self.voiceover(text="""那么，一个很自然的问题就出现了：我们能不能把智能本身制造出来？"""):
            # =========================
            # 颜色
            # =========================
            TEXT_COLOR = "#333333"
            ARROW_COLOR = "#888888"

            # =========================
            # 人脑
            # =========================
            brain = SVGMobject(
                f"{BODY_PATH}brain.svg"
            )
            brain.set_height(2.2)
            brain.move_to(LEFT * 3.0)

            brain_label = Text(
                "人类智能",
                font_size=30,
                color=TEXT_COLOR
            )
            brain_label.next_to(
                brain,
                DOWN,
                buff=0.25
            )

            # =========================
            # AI
            # =========================
            ai = SVGMobject(
                f"{AI_PATH}ai.svg"
            )
            ai.set_height(2.2)
            ai.move_to(RIGHT * 3.0)

            ai_label = Text(
                "人工智能",
                font_size=30,
                color=TEXT_COLOR
            )
            ai_label.next_to(
                ai,
                DOWN,
                buff=0.25
            )

            # =========================
            # 人脑 → AI 的箭头
            # =========================
            arrow = Arrow(
                brain.get_right() + RIGHT * 0.15,
                ai.get_left() + LEFT * 0.15,
                color=ARROW_COLOR,
                stroke_width=3,
                buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )

            # =========================
            # 问号
            # =========================
            question = Text(
                "?",
                font_size=70,
                weight=BOLD,
                color=BLACK
            )

            # 放在 AI 的右下方
            question.next_to(
                ai,
                DOWN + RIGHT,
                buff=0.25
            )

            # =========================
            # ① 人脑出现
            # =========================
            self.play(
                FadeIn(brain, scale=0.8),
                FadeIn(brain_label, shift=UP * 0.2),
                run_time=1
            )

            self.wait(0.5)

            # =========================
            # ② AI 出现
            # =========================
            self.play(
                FadeIn(ai, scale=0.7),
                FadeIn(ai_label, shift=UP * 0.2),
                run_time=0.8
            )

            self.wait(0.3)

            # =========================
            # ③ 人脑 → AI
            # =========================
            self.play(
                GrowArrow(arrow),
                run_time=0.8
            )

            self.wait(0.5)

            # =========================
            # ④ 问号出现
            # =========================
            self.play(
                FadeIn(question, scale=0.5),
                run_time=0.6
            )

        self.clear()

    def _section06(self):
        with self.voiceover(text="""如果我们真的制造出了一台拥有甚至超过人类智能的机器，
                            而且它不需要睡觉、不知疲倦，甚至可以被复制……"""):
            TEXT_COLOR = "#333333"

            # ==========================================
            # 1. 中间的 AI
            # ==========================================
            ai = SVGMobject(
                f"{AI_PATH}ai.svg"
            )
            ai.set_height(1.5)
            ai.move_to(ORIGIN)

            ai_label = Text(
                "人工智能",
                font_size=15,
                color=TEXT_COLOR
            )
            ai_label.next_to(
                ai,
                DOWN,
                buff=0.2
            )

            self.play(
                FadeIn(ai, scale=0.8),
                FadeIn(ai_label, shift=UP * 0.15),
                run_time=0.8
            )

            self.wait(0.5)

            # ==========================================
            # 2. AI 超过人类智能
            # ==========================================
            self.play(
                ai.animate.scale(1.25),
                ai_label.animate.scale(1.05),
                run_time=0.7
            )

            self.wait(0.4)

            # ==========================================
            # 3. 三个能力
            # ==========================================

            # -------- 不需要睡觉 --------
            moon = SVGMobject(
                f"{BODY_PATH}sleep.svg"
            )
            moon.set_height(0.5)
            moon.move_to(
                LEFT * 3.2 + UP * 1.8
            )

            moon_label = Text(
                "不需要睡觉",
                font_size=10,
                color=TEXT_COLOR
            )
            moon_label.next_to(
                moon,
                DOWN,
                buff=0.12
            )

            # -------- 不知疲倦 --------
            energy = SVGMobject(
                f"{AI_PATH}energy.svg"
            )
            energy.set_height(0.5)
            energy.move_to(
                RIGHT * 3.2 + UP * 1.8
            )

            energy_label = Text(
                "不知疲倦",
                font_size=10,
                color=TEXT_COLOR
            )
            energy_label.next_to(
                energy,
                DOWN,
                buff=0.12
            )

            # -------- 可以复制 --------
            copy_icon = SVGMobject(
                f"{AI_PATH}copy.svg"
            )
            copy_icon.set_height(0.5)
            copy_icon.move_to(
                DOWN * 2.3
            )

            copy_label = Text(
                "可以复制",
                font_size=10,
                color=TEXT_COLOR
            )
            copy_label.next_to(
                copy_icon,
                DOWN,
                buff=0.12
            )

            # 三个能力依次出现
            self.play(
                FadeIn(moon, scale=0.7),
                FadeIn(moon_label, shift=UP * 0.1),
                run_time=0.5
            )

            self.play(
                FadeIn(energy, scale=0.7),
                FadeIn(energy_label, shift=UP * 0.1),
                run_time=0.5
            )

            self.play(
                FadeIn(copy_icon, scale=0.7),
                FadeIn(copy_label, shift=UP * 0.1),
                run_time=0.5
            )

            self.wait(2)

            # ==========================================
            # 4. 收掉能力图标
            # ==========================================
            self.play(
                FadeOut(moon),
                FadeOut(moon_label),
                FadeOut(energy),
                FadeOut(energy_label),
                FadeOut(copy_icon),
                FadeOut(copy_label),
                FadeOut(ai),
                FadeOut(ai_label),
                run_time=0.6
            )

            # ==========================================
            # 5. AI 开始复制
            # ==========================================

            source_ai = SVGMobject(
                f"{AI_PATH}ai.svg"
            )
            source_ai.set_height(1.35)
            source_ai.move_to(ORIGIN)

            self.play(
                FadeIn(source_ai, scale=0.5),
                run_time=0.4
            )

            self.wait(0.3)

            # 第一批复制
            positions_1 = [
                LEFT * 2.5,
                RIGHT * 2.5,
            ]

            copies_1 = VGroup()

            for pos in positions_1:
                mob = source_ai.copy()
                mob.move_to(pos)
                copies_1.add(mob)

            self.play(
                LaggedStart(
                    *[
                        FadeIn(mob, scale=0.5)
                        for mob in copies_1
                    ],
                    lag_ratio=0.15
                ),
                run_time=0.7
            )

            # 第二批复制
            positions_2 = [
                LEFT * 4.5 + UP * 1.8,
                LEFT * 1.5 + UP * 1.8,
                RIGHT * 1.5 + UP * 1.8,
                RIGHT * 4.5 + UP * 1.8,

                LEFT * 4.5 + DOWN * 1.8,
                LEFT * 1.5 + DOWN * 1.8,
                RIGHT * 1.5 + DOWN * 1.8,
                RIGHT * 4.5 + DOWN * 1.8,
            ]

            copies_2 = VGroup()

            for pos in positions_2:
                mob = source_ai.copy()
                mob.set_height(1.0)
                mob.move_to(pos)
                copies_2.add(mob)

            self.play(
                LaggedStart(
                    *[
                        FadeIn(mob, scale=0.4)
                        for mob in copies_2
                    ],
                    lag_ratio=0.08
                ),
                run_time=1.2
            )

        self.clear()

        with self.voiceover(text="""那人类社会会发生什么？
                            但在讨论这些之前，先问大家一个问题："""):
            # ==========================================
            # 7. 巨大的问题
            # ==========================================
            question = Text(
                "?",
                font_size=90,
                weight=BOLD,
                color=BLACK
            )

            self.play(
                FadeIn(question, scale=0.5),
            )

        with self.voiceover(text="""
                            如果让你亲手设计这样一台机器，你会怎么设计？"""):
            # ==========================================
            # 2. 问号缩小并移动到上方
            # ==========================================
            self.play(
                question.animate.scale(0.55).move_to(
                    UP * 3.0
                ),
                run_time=0.7
            )

            # ==========================================
            # 3. 设计框
            # ==========================================
            frame = SVGMobject(f"{SUNDRY_PATH}blank-paper.svg")
            frame.scale(3)

            frame.move_to(DOWN * 0.4)

            self.play(
                Create(frame),
                run_time=0.7
            )

            # ==========================================
            # 4. 三个步骤
            # ==========================================
            steps = VGroup(
                Text(
                    "第一步……",
                    font="FangSong",
                    font_size=20,
                    color=TEXT_COLOR
                ),
                Text(
                    "第二步……",
                    font="FangSong",
                    font_size=20,
                    color=TEXT_COLOR
                ),
                Text(
                    "第三步……",
                    font="FangSong",
                    font_size=20,
                    color=TEXT_COLOR
                ),
            )

            steps.arrange(
                DOWN,
                buff=0.35
            )

            steps.move_to(
                frame.get_center()
            )

            # ==========================================
            # 5. 依次出现
            # ==========================================
            self.play(
                FadeIn(
                    steps[0],
                    shift=RIGHT * 0.2
                ),
                run_time=0.5
            )

            self.play(
                FadeIn(
                    steps[1],
                    shift=RIGHT * 0.2
                ),
                run_time=0.5
            )

            self.play(
                FadeIn(
                    steps[2],
                    shift=RIGHT * 0.2
                ),
                run_time=0.5
            )

        self.clear()

    def _section07(self):
        with self.voiceover(text="""
                            你可能会说：
                             让它能像人一样思考;
                             让它能像人一样行动"""):
            TEXT_COLOR = "#333333"

            # ==========================================
            # 2. 像人一样思考
            # ==========================================
            brain = SVGMobject(
                f"{BODY_PATH}brain.svg"
            )
            brain.set_height(1.5)
            brain.move_to(
                LEFT * 2.7 + UP * 0.5
            )

            thinking_label = Text(
                "像人一样思考",
                font_size=26,
                color=TEXT_COLOR
            )
            thinking_label.next_to(
                brain,
                DOWN,
                buff=0.2
            )

            self.wait(1)

            self.play(
                FadeIn(brain, scale=0.7),
                FadeIn(
                    thinking_label,
                    shift=UP * 0.15
                ),
                run_time=0.7
            )

            self.wait(1)

            # ==========================================
            # 3. 像人一样行动
            # ==========================================
            action = SVGMobject(
                f"{BODY_PATH}action.svg"
            )
            action.set_height(1.5)
            action.move_to(
                RIGHT * 2.7 + UP * 0.5
            )

            action_label = Text(
                "像人一样行动",
                font_size=26,
                color=TEXT_COLOR
            )
            action_label.next_to(
                action,
                DOWN,
                buff=0.2
            )

            self.play(
                FadeIn(action, scale=0.7),
                FadeIn(
                    action_label,
                    shift=UP * 0.15
                ),
                run_time=0.7
            )
        self.clear()

    def _section08(self):
        with self.voiceover(text="""
                            这个想法很自然，但我们先不评价它。"""
                            ):
            GREEN = "#4CAF50"
            RED = "#E53935"

            # =====================================================
            # 1. 灯泡 SVG
            # =====================================================

            bulb = SVGMobject(f"{SUNDRY_PATH}bulb.svg")
            bulb.set_height(1.5)
            bulb.move_to(ORIGIN)

            # =====================================================
            # 2. 灯泡出现
            # 对应：
            # “这个想法当然很自然。”
            # =====================================================

            self.play(
                FadeIn(
                    bulb,
                    shift=UP * 0.2,
                ),
                run_time=0.8,
            )

            self.wait(0.5)

            # =====================================================
            # 3. 对号
            # =====================================================

            check = VGroup(
                Line(
                    LEFT * 0.30 + DOWN * 0.02,
                    LEFT * 0.05 + DOWN * 0.28,
                    color=GREEN,
                    stroke_width=8,
                ),
                Line(
                    LEFT * 0.05 + DOWN * 0.28,
                    RIGHT * 0.40 + UP * 0.32,
                    color=GREEN,
                    stroke_width=8,
                ),
            )

            # =====================================================
            # 4. 叉号
            # =====================================================

            cross = VGroup(
                Line(
                    LEFT * 0.30 + DOWN * 0.30,
                    RIGHT * 0.30 + UP * 0.30,
                    color=RED,
                    stroke_width=8,
                ),
                Line(
                    LEFT * 0.30 + UP * 0.30,
                    RIGHT * 0.30 + DOWN * 0.30,
                    color=RED,
                    stroke_width=8,
                ),
            )

            # =====================================================
            # 5. 放置评价符号
            # =====================================================

            evaluation = VGroup(check, cross)

            evaluation.arrange(
                RIGHT,
                buff=0.8,
            )

            evaluation.next_to(
                bulb,
                DOWN,
                buff=0.7,
            )

            # =====================================================
            # 6. 出现评价
            # =====================================================

            self.play(
                Create(check),
                Create(cross),
                run_time=0.6,
            )

            self.wait(0.4)

            # =====================================================
            # 7. 暂不评价
            # =====================================================

            self.play(
                FadeOut(evaluation),
                run_time=0.6,
            )
        self.clear()

    def _section09(self):
        with self.voiceover(text="""
                            在人类历史上，其实存在一个非常有意思的类似案例：飞行。"""
                            ):
            self.wait(2)
            plane = SVGMobject(f"{SUNDRY_PATH}aircraft.svg")
            plane.scale(0.6)

            # 贝塞尔4个控制点：起飞爬升 -> 之后平飞，永不下降
            p0 = np.array([-8, -0.5, 0])
            p1 = np.array([-3, 1.8, 0])
            p2 = np.array([3, 2.2, 0])
            p3 = np.array([8, 2.2, 0])

            def bezier_point(t):
                """t ∈ [0,1] 返回贝塞尔点"""
                return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

            def bezier_tangent(t):
                """贝塞尔切线向量"""
                return 3 * (1 - t)**2 * (p1 - p0) + 6 * (1 - t) * t * (p2 - p1) + 3 * t**2 * (p3 - p2)

            def update_plane(mob, alpha):
                pos = bezier_point(alpha)
                mob.move_to(pos)
                tan_vec = bezier_tangent(alpha)
                angle = np.arctan2(tan_vec[1], tan_vec[0])
                mob.set_angle(angle)

            plane.move_to(bezier_point(0))
            self.add(plane)

            self.play(
                UpdateFromAlphaFunc(plane, update_plane),
                run_time=4,
                rate_func=linear
            )
        self.clear()

    def _section10(self):
        with self.voiceover(text="""
                            可上九天揽月，这一伟大成就或许能给我们一些启发！"""
                            ):
            # 深色星空背景
            bg = Rectangle(width=config.frame_width,
                           height=config.frame_height,
                           fill_color="#080c24",
                           fill_opacity=1)
            self.add(bg)

            # 星星
            stars = VGroup(*[
                Dot(
                    np.array([np.random.uniform(-7, 7),
                             np.random.uniform(-4, 4), 0]),
                    radius=np.random.uniform(0.02, 0.06), color=WHITE
                )
                for _ in range(60)
            ])
            self.add(stars)

            # 导入你的火箭svg，居中起始位置：画面底部中心
            rocket = SVGMobject(f"{ASSET_PATH}rocket.svg").scale(0.7)
            rocket.move_to(DOWN * 3)

            # 火焰作为火箭的子对象！！这样火箭移动火焰自动跟着走，不用手动更新位置
            flame = VGroup(
                Triangle(color=ORANGE, fill_opacity=0.9).scale(
                    0.35).rotate(PI),
                Triangle(color=YELLOW, fill_opacity=1).scale(0.22).rotate(PI)
            )
            flame.next_to(rocket, DOWN, buff=0.02)
            rocket.add(flame)  # 关键：把火焰加入火箭组，父子绑定

            # 火焰随机抖动
            def flame_shake(mob):
                mob.scale(np.random.uniform(0.9, 1.1))
            flame.add_updater(flame_shake)

            self.play(FadeIn(rocket), run_time=1)

            # 火箭居中向上飞行
            self.play(
                rocket.animate.move_to(UP * 2),
                rate_func=linear,
                run_time=4
            )

            flame.remove_updater(flame_shake)

            self.play(FadeOut(rocket), run_time=1)
        self.clear()

    def _section11(self):
        with self.voiceover(text="""
                            人类综合运用数学、物理学、工程学以及众多其他领域的知识，构建起一套完全区别于鸟类的飞行方式。"""
                            ):
            # ---------- 中间飞机 ----------
            plane = SVGMobject(f"{ASSET_PATH}aircraft.svg").scale(
                1).move_to(ORIGIN)

            # ---------- 外围SVG列表 ----------
            svg_list = [
                SVGMobject(f"{MATH_PATH}mathematics.svg").scale(0.3),
                SVGMobject(f"{MATH_PATH}einstein-eq.svg").scale(0.3),
                SVGMobject(f"{SUNDRY_PATH}engineering.svg").scale(0.3),
                SVGMobject(f"{MATH_PATH}dot-cross.svg").scale(0.1)
            ]

            # 环形坐标：4个素材均匀分布在半径2.8的圆周
            radius = 2.8
            angles = [0, TAU / 4, TAU * 2 / 4, TAU * 3 / 4]
            positions = [
                radius * np.array([np.cos(a), np.sin(a), 0])
                for a in angles
            ]

            for svg, pos in zip(svg_list, positions):
                svg.move_to(pos)

            # ==========动画序列==========
            # 先显示中间飞机
            self.add(plane)
            self.wait(0.5)

            # 逐个淡入周围的svg图标
            for svg in svg_list:
                self.play(FadeIn(svg), run_time=0.7)
        self.clear()

    def _section12(self):
        with self.voiceover(text="""
                            我们发现：如果目标是实现“飞行”，并不需要让机器“像鸟一样飞”。"""
                            ):
            # ==================================================
            # 第一组：飞行 —— 不需要像鸟一样飞
            # ==================================================

            # 左上角发现图标
            discover_icon = SVGMobject(
                f"{ASSET_PATH}discover.svg"
            ).scale(0.3).to_corner(UL, buff=0.4)

            # 飞机 / 鸽子
            plane = SVGMobject(
                f"{ASSET_PATH}aircraft.svg"
            ).scale(0.7).move_to([-3.2, 0, 0])

            pigeon = SVGMobject(
                f"{ASSET_PATH}pigeon.svg"
            ).scale(0.7).move_to([3.2, 0, 0])

            # like / no
            like_obj = ImageMobject(
                f"{ASSET_PATH}like.png"
            ).scale(0.7).move_to(ORIGIN)

            no_obj = SVGMobject(
                f"{MATH_PATH}no.svg"
            ).scale(0.7).move_to(like_obj.get_center())

            # --------------------------------------------------
            # 第一组动画
            # --------------------------------------------------

            self.play(
                FadeIn(discover_icon),
                run_time=0.6
            )

            self.play(
                FadeIn(plane),
                FadeIn(pigeon),
                run_time=0.8
            )

            self.play(
                FadeIn(like_obj),
                run_time=0.7
            )

            self.play(
                FadeIn(no_obj),
                run_time=0.6
            )

        with self.voiceover(text="""
                            类似地，智能是否也不意味着模仿人？"""
                            ):
            # ==================================================
            # 第一组整体缩小，成为上方“上一镜头”
            # ==================================================

            previous_group = Group(
                discover_icon,
                plane,
                pigeon,
                like_obj,
                no_obj,
            )

            self.play(
                previous_group.animate
                .scale(0.55)
                .move_to(UP * 2.3),
                run_time=0.8
            )

            # 上方卡片边框
            previous_frame = SurroundingRectangle(
                previous_group,
                buff=0.25,
                stroke_width=2,
            )

            self.play(
                Create(previous_frame),
                run_time=0.5
            )

            # ==================================================
            # 第二组：智能 —— 是否需要像人一样？
            # ==================================================

            # 左侧：机器
            machine = SVGMobject(
                f"{AI_PATH}ai.svg"
            ).scale(0.7).move_to([-3.2, -1.2, 0])

            # 右侧：人
            human = ImageMobject(
                f"{BODY_PATH}human.png"
            ).scale(0.7).move_to([3.2, -1.2, 0])

            # 中间 like
            like_obj2 = ImageMobject(
                f"{ASSET_PATH}like.png"
            ).scale(0.7).move_to([0, -1.2, 0])

            # no
            no_obj2 = SVGMobject(
                f"{MATH_PATH}no.svg"
            ).scale(0.7).move_to(like_obj2.get_center())

            # --------------------------------------------------
            # 第二组动画
            # --------------------------------------------------

            self.play(
                FadeIn(machine),
                FadeIn(human),
                run_time=0.8
            )

            self.wait(0.3)

            self.play(
                FadeIn(like_obj2),
                run_time=0.7
            )

            self.wait(0.5)

            self.play(
                FadeIn(no_obj2),
                run_time=0.6
            )
        self._fade_out()

    def _section13(self):
        with self.voiceover(text="""
                            这就引出了人工智能研究的另一种思路：rational——理性。"""
                            ):
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

        with self.voiceover(text="""
                                当然，这并不是说人类的思考和行动不理性。
                                """
                            ):
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
