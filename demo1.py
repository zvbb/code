from manim import *
# fmt: off
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
FIGURE_PATH = "material/figure/"
BODY_PATH = "material/body/"
# fmt: on


from manim import *

class ThousandYearDreamOfFlight(Scene):
    def construct(self):
        # ========== 第一部分：千年飞天梦 古代星空 ==========
        sky_bg = Rectangle(width=config.frame_width, height=config.frame_height, fill_color="#0b102b", fill_opacity=1)
        self.add(sky_bg)

        # 生成满天星星
        stars = VGroup()
        for _ in range(80):
            star = Dot(
                np.array([
                    np.random.uniform(-7,7),
                    np.random.uniform(-4,4),
                    0
                ]),
                radius=np.random.uniform(0.02,0.06),
                color=WHITE
            )
            stars.add(star)
        self.add(stars)

        title_1 = Text("千年飞天梦", font_size=48, color=GOLD).to_edge(UP, buff=0.6)
        self.play(Write(title_1), run_time=2)
        self.wait(1)

        # 古人仰望：简单小人剪影【修复缩进】
        ancient_figure = VGroup(
            Line([0,-1,0],[0,-2.2,0], stroke_width=4),
            Line([0,-1,0],[-0.6,-1.4,0], stroke_width=4),
            Line([0,-1,0],[0.6,-1.4,0], stroke_width=4),
            Line([0,-2.2,0],[-0.4,-3,0], stroke_width=4),
            Line([0,-2.2,0],[0.4,-3,0], stroke_width=4),
        ).set_color(GREY_B)
        ancient_figure.shift(DOWN*0.5)

        # 仰望的视线指向天空
        sight_line = DashedLine(ancient_figure.get_top(), [0, 2.5,0], color=YELLOW, stroke_opacity=0.4)

        self.play(FadeIn(ancient_figure), Create(sight_line), run_time=1.5)
        self.wait(1)

        # 古代飞天意象：风筝、古代火箭示意
        kite = VGroup(
            Polygon([-0.8,0,0],[0,1,0],[0.8,0,0],[0,-0.4,0], color="#ddbb77", fill_opacity=0.7),
            Line([0,-0.4,0],[0,-1.2,0], color="#ddbb77")
        ).scale(0.6).shift(LEFT*3 + UP*1)

        ancient_fire_arrow = VGroup(
            Triangle(color=RED, fill_opacity=0.8).scale(0.2).rotate(PI),
            Rectangle(width=0.12, height=0.8, color=GREY, fill_opacity=0.7)
        ).arrange(UP, buff=-0.1).shift(RIGHT*3 + UP*1.2)

        self.play(FadeIn(kite), FadeIn(ancient_fire_arrow), run_time=1.2)
        self.wait(1.5)

        # ========== 转场：时间流转，画面淡出 ==========
        self.play(
            FadeOut(ancient_figure),
            FadeOut(sight_line),
            FadeOut(kite),
            FadeOut(ancient_fire_arrow),
            FadeOut(title_1),
            run_time=2
        )

        # ========== 第二部分：今日上九天 火箭发射 ==========
        title_2 = Text("今日上九天", font_size=48, color=GOLD).to_edge(UP, buff=0.6)
        self.play(Write(title_2), run_time=2)

        # 火箭绘制
        rocket_body = Rectangle(width=0.4, height=2.2, color=WHITE, fill_opacity=0.9)
        rocket_head = Triangle(color=RED, fill_opacity=1).scale(0.35).rotate(0).next_to(rocket_body, UP, buff=-0.22)
        rocket_wing1 = Polygon([-0.2, -0.8,0],[-0.6,-1.4,0],[-0.2,-1.4,0], color="#ee4444", fill_opacity=0.9).next_to(rocket_body, DOWN, buff=0)
        rocket_wing2 = Polygon([0.2, -0.8,0],[0.6,-1.4,0],[0.2,-1.4,0], color="#ee4444", fill_opacity=0.9).next_to(rocket_body, DOWN, buff=0)
        rocket_flame = VGroup(
            Triangle(color=ORANGE, fill_opacity=0.9).scale(0.4).rotate(PI).next_to(rocket_body, DOWN, buff=-0.3),
            Triangle(color=YELLOW, fill_opacity=1).scale(0.25).rotate(PI).next_to(rocket_body, DOWN, buff=-0.15)
        )

        rocket = VGroup(rocket_head, rocket_body, rocket_wing1, rocket_wing2, rocket_flame).scale(0.8).shift(DOWN*3)
        self.play(FadeIn(rocket), run_time=1)

        # 火焰抖动更新器
        def flame_updater(mob):
            mob.scale(np.random.uniform(0.92,1.08))
        rocket_flame.add_updater(flame_updater)

        self.play(
            rocket.animate.shift(UP*7),
            rate_func=linear,
            run_time=4
        )
        rocket_flame.remove_updater(flame_updater)
        self.wait(1)

        # 切换深邃太空背景
        space_bg = Rectangle(width=config.frame_width, height=config.frame_height, fill_color="#040418", fill_opacity=1)
        self.add(space_bg, stars)

        # 火箭飘在太空
        self.play(rocket.animate.scale(0.4).shift(UP*1+RIGHT*2), run_time=1.2)
        self.wait(1)

        # ========== 第三部分：人类伟大成就的启发 结尾升华 ==========
        self.play(FadeOut(title_2), run_time=1)

        text_main = Text("人类这一伟大成或许能给我们一些启发！", font_size=36, color=WHITE).shift(DOWN*1.2)
        sub_text = Text("心怀梦想，不惧征途，终可奔赴星辰大海", font_size=28, color="#ffdd77").shift(DOWN*2.2)

        self.play(Write(text_main), run_time=2.5)
        self.wait(1)
        self.play(Write(sub_text), run_time=2)
        self.wait(3)

        # 全部淡出收尾
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)