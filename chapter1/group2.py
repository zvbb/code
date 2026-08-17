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
SVG_DIR = "material"
SUNDRY_PATH = "material/sundry/"
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
FIGURE_PATH = "material/figure/"

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


class Group2(VoiceoverScene):

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

    def _section01(self):
        with self.voiceover(text="权威的教材不在少数，为什么就选择AIMA呢？"):
            # =========================================================
            # 1. 书架
            # =========================================================

            library = SVGMobject("material/library.svg")
            library.move_to(UP * 2.2)

            self.play(
                FadeIn(library),
                run_time=1
            )

            # =========================================================
            # 2. AIMA
            # =========================================================

            aima = ImageMobject("material/aima.jpg")
            aima.set_height(3.2)

            # 书架中被选中的那本书的位置
            selected_book_pos = np.array([
                0.0,
                2.15,
                0
            ])

            # AIMA 最终停留的位置
            target_pos = DOWN * 2.0

            # ---------------------------------------------------------
            # 关键：
            #
            # 先让完整的 AIMA 位于最终位置
            # 然后围绕 selected_book_pos 缩小
            #
            # 这样缩小以后，它的“起点”就在书架中的那本书上
            # ---------------------------------------------------------

            aima.move_to(target_pos)

            aima.scale(
                0.03,
                about_point=selected_book_pos
            )

            self.add(aima)

            # =========================================================
            # 3. 从书架中的那本书“长出来”
            #
            # 同时：
            #   - 围绕 selected_book_pos 放大
            #   - 向下移动到最终位置
            # =========================================================

            self.play(
                aima.animate
                    .scale(
                        1 / 0.03,
                        about_point=selected_book_pos
                    ).move_to(target_pos),
                run_time=2,
                rate_func=smooth
            )
        self.clear()

    def _section02(self):
        with self.voiceover(text="AIMA 有一个非常重要的特点："):
            medal = SVGMobject(f"{SUNDRY_PATH}medal.svg")
            medal.move_to(ORIGIN)
            self.play(
                FadeIn(medal),
            )
        self.clear()

    def _section03(self):
        with self.voiceover(text="""它不是试图把某一个 AI 技术讲到最深，而是试图让你看到人工智能这个领域的整体。"""):
            left = SVGMobject(f"{SUNDRY_PATH}well.svg")
            right = SVGMobject(f"{SUNDRY_PATH}world-map.svg")
            vs = SVGMobject(f"{SUNDRY_PATH}vs.svg")

            left.scale(1)
            right.scale(1)
            vs.scale(0.2)

            left.move_to(LEFT * 3.2)
            right.move_to(RIGHT * 3.2)
            vs.move_to(ORIGIN)

            # 左图出现
            self.play(
                FadeIn(left, shift=RIGHT * 0.3),
                run_time=0.7
            )

            self.wait(1)

            # 左图：消失 -> 出现
            self.play(
                left.animate.set_opacity(0),
                run_time=0.5
            )
            self.play(
                left.animate.set_opacity(1),
                run_time=0.5
            )

            # VS
            self.play(
                FadeIn(vs, scale=0.5),
                run_time=0.4
            )

            self.wait(1)

            # 右图出现
            self.play(
                FadeIn(right, shift=LEFT * 0.3),
                run_time=0.7
            )

            self.wait(1)

            # 右图：消失 -> 出现
            self.play(
                right.animate.set_opacity(0),
                run_time=0.5
            )
            self.play(
                right.animate.set_opacity(1),
                run_time=0.5
            )
        self.clear()

    def _section04(self):
        with self.voiceover(text="""机器学习、深度学习、强化学习、搜索、规划、知识表示、推理、
                            自然语言处理、计算机视觉、智能体...，
                            这些看起来彼此不同的内容，在 AIMA 中被放到了同一张地图上。
                            所以，它是一本人工智能的总论教材。"""):
            # =========================
            # 中央地图
            # =========================
            map_svg = SVGMobject(f"{SUNDRY_PATH}world-map.svg")
            map_svg.scale(1)
            map_svg.move_to(ORIGIN)

            self.play(
                FadeIn(map_svg, scale=0.5),
                run_time=0.8
            )

            self.wait(0.3)

            # =========================
            # 11 个素材
            # =========================
            files = [
                f"{WORD_PATH}machine-learn.png",
                f"{WORD_PATH}deep-learn.png",
                f"{WORD_PATH}reinforcement.png",
                f"{WORD_PATH}search.png",
                f"{WORD_PATH}plan.png",
                f"{WORD_PATH}knowledge-representation.png",
                f"{WORD_PATH}inference.png",
                f"{WORD_PATH}nlp.png",
                f"{WORD_PATH}computer-vision.png",
                f"{WORD_PATH}agent.png",
                f"{MATH_PATH}dot-cross.svg",
            ]

            # =========================
            # 自动环绕地图排列
            # =========================
            radius_x = 4
            radius_y = 3
            items = []
            for i, filename in enumerate(files):

                if filename.endswith(".svg"):
                    mob = SVGMobject(
                        f"{filename}"
                    )
                    mob.scale(0.1)
                else:
                    mob = ImageMobject(
                        f"{filename}"
                    )
                    mob.scale(0.5)

                angle = TAU * i / len(files)

                x = radius_x * np.cos(angle)
                y = radius_y * np.sin(angle)

                mob.move_to([x, y, 0])

                items.append(mob)

            # =========================
            # 四周陆续出现
            # =========================
            for mob in items:
                self.play(
                    FadeIn(mob, scale=0.7),
                    run_time=0.8
                )

            self.wait(0.5)
            # =========================
            # 一个个进入地图
            # =========================
            for mob in items:

                self.play(
                    mob.animate
                    .move_to(map_svg.get_center())
                    .scale(0.1),
                    run_time=0.6
                )

                # 到达地图后消失
                self.remove(mob)
        self.clear()

    def _section05(self):
        with self.voiceover(text="当我们以后遇到一个新的 AI 问题时，AIMA 未必能够直接给出答案，"):
            # =========================
            # Question
            # =========================
            question = SVGMobject(
                f"{MATH_PATH}question.svg"
            )
            question.scale(1.5)
            question.move_to(LEFT * 3.2)

            # =========================
            # Solution
            # =========================
            solution = SVGMobject(
                f"{MATH_PATH}solution.svg"
            )
            solution.scale(1.5)
            solution.move_to(RIGHT * 3.2)

            # =========================
            # 中间箭头
            # =========================
            arrow = Arrow(
                question.get_right(),
                solution.get_left(),
                buff=0.6,
                stroke_width=5,
                color=GREY_B
            )

            # =========================
            # No
            # =========================
            no = SVGMobject(
                f"{MATH_PATH}/no.svg"
            )
            no.scale(1.7)
            no.move_to(solution)

            # =========================
            # 动画
            # =========================

            # 1. 出现问题
            self.play(
                FadeIn(question, scale=0.8),
                run_time=0.6
            )

            self.wait(2)

            # 2. 出现“答案”的预期
            self.play(
                GrowArrow(arrow),
                FadeIn(solution, scale=0.8),
                run_time=0.8
            )

            self.wait(0.5)

            # 3. 否定：AIMA 并不会直接给出这个答案
            self.play(
                FadeIn(no, scale=1.2),
                run_time=0.5
            )
        self.clear()

    def _section06(self):
        with self.voiceover(text="""但它可以帮助我们判断：
                            它属于哪一类问题？问题有哪些解决思路和方法？
                            然后，我们就能进一步找到真正深入研究这个问题的资料。"""):
            # =========================
            # Teacher
            # =========================
            teacher = SVGMobject(
                f"{FIGURE_PATH}teacher.svg"
            )
            teacher.scale(1.6)
            teacher.move_to(LEFT * 3.2)

            # =========================
            # Question 1
            # =========================
            question1 = ImageMobject(
                "chapter1/asset/question1.png"
            )
            question1.scale(1)
            question1.move_to(
                RIGHT * 3 + UP * 1.2
            )

            # =========================
            # Question 2
            # =========================
            question2 = ImageMobject(
                "chapter1/asset/question2.png"
            )
            question2.scale(1)
            question2.move_to(
                RIGHT * 3 + DOWN * 1.2
            )

            # =========================
            # 动画
            # =========================

            # 1. 老师出现
            self.play(
                FadeIn(teacher, scale=0.8),
                run_time=0.7
            )

            self.wait(0.4)

            # 2. 第一个问题出现
            self.play(
                FadeIn(question1, shift=LEFT * 0.4),
                run_time=0.6
            )

            self.wait(0.3)

            # 3. 第二个问题出现
            self.play(
                FadeIn(question2, shift=LEFT * 0.4),
                run_time=0.6
            )
        self. clear()
