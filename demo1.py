from manim import *
# fmt: off
MATH_PATH = "material/math/"
WORD_PATH = "material/word/"
SUNDRY_PATH = "material/sundry/"
FIGURE_PATH = "material/figure/"
BODY_PATH = "material/body/"
# fmt: on

from manim import *


class AIMA(Scene):

    def construct(self):
        self.camera.background_color = WHITE

        self.section_thick_book()

    def section_thick_book(self):

        book_path = f"{MATH_PATH}book-close.svg"

        book_count = 6
        books = VGroup()

        # ==================================================
        # 创建第一本书
        # ==================================================

        first_book = SVGMobject(book_path)
        first_book.set_width(1.5)

        books.add(first_book)

        # 获取 SVG 的真实高度
        book_height = first_book.height

        # ==================================================
        # 创建后面的书
        # ==================================================

        for i in range(1, book_count):

            book = SVGMobject(book_path)
            book.set_width(1.5)

            book.move_to(
                first_book.get_center()
                + UP * (i * book_height)
            )

            books.add(book)

        # ==================================================
        # 整体居中
        # ==================================================

        books.move_to(LEFT * 2.0)

        # ==================================================
        # 一本一本从上面掉下来
        # ==================================================

        for book in books:

            final_pos = book.get_center()

            book.move_to(
                final_pos + UP * 2
            )

            self.play(
                book.animate.move_to(final_pos),
                rate_func=rush_into,
                run_time=0.35
            )

        # ==================================================
        # 1000+ 页
        # ==================================================

        pages = Text(
            "1000+ 页",
            font="FangSong",
            font_size=72,
            weight=BOLD,
            color=BLACK,
        )

        pages.move_to(RIGHT * 3.2)

        self.play(
            FadeIn(pages, scale=0.8),
            run_time=0.5
        )

        self.wait(1.5)

        # ==================================================
        # 进入“砍掉多少”
        # ==================================================

        self.play(
            FadeOut(pages),
            run_time=0.3
        )

        # ==================================================
        # 砍掉 80%
        # ==================================================

        text_80 = Text(
            "砍掉 80%？",
            font="FangSong",
            font_size=64,
            weight=BOLD,
            color=BLACK,
        )

        text_80.move_to(RIGHT * 3.2)

        self.play(
            FadeIn(text_80, scale=0.8),
            run_time=0.4
        )

        self.wait(0.5)

        # 保留 1 本
        # 其余书向下消失
        self.play(
            *[
                FadeOut(
                    book,
                    shift=DOWN * 0.4
                )
                for book in books[1:]
            ],
            run_time=0.8
        )

        self.wait(0.8)

        # ==================================================
        # 有点武断……
        # ==================================================

        warning = Text(
            "有点武断……",
            font="FangSong",
            font_size=42,
            color=BLACK,
        )

        warning.next_to(
            text_80,
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(warning),
            run_time=0.4
        )

        self.wait(1)

        # ==================================================
        # 恢复 6 本书
        # ==================================================

        self.play(
            *[
                FadeIn(
                    book,
                    shift=UP * 0.4
                )
                for book in books[1:]
            ],
            run_time=0.8
        )

        self.play(
            FadeOut(text_80),
            FadeOut(warning),
            run_time=0.3
        )

        self.wait(0.5)

        # ==================================================
        # 砍掉一半
        # ==================================================

        text_50 = Text(
            "砍掉一半？",
            font="FangSong",
            font_size=64,
            weight=BOLD,
            color=BLACK,
        )

        text_50.move_to(RIGHT * 3.2)

        self.play(
            FadeIn(text_50, scale=0.8),
            run_time=0.4
        )

        self.wait(0.5)

        # 6 本 -> 3 本
        self.play(
            *[
                FadeOut(
                    book,
                    shift=DOWN * 0.4
                )
                for book in books[3:]
            ],
            run_time=0.8
        )

        self.wait(1)

        # ==================================================
        # 感觉还是有点少
        # ==================================================

        self.play(
            FadeOut(text_50),
            run_time=0.3
        )

        final_text = Text(
            "感觉还是有点少。",
            font="FangSong",
            font_size=52,
            weight=BOLD,
            color=BLACK,
        )

        final_text.move_to(RIGHT * 3.0)

        self.play(
            FadeIn(
                final_text,
                scale=0.9
            ),
            run_time=0.5
        )

        self.wait(1.5)