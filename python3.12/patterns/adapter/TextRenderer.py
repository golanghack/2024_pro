#! /usr/bin/env pytnon3

import sys
import textwrap


class TextRenderer:
    def __init__(self, width: int = 80, file: str = sys.stdout) -> None:
        self.width = width
        self.file = file
        self.previous = False

    def header(self, title: str) -> None:
        self.file.write(
            "{0:^{2}}\n{1:^{2}}\n".format(title, "=" * len(title), self.width)
        )

    def paragraph(self, text: str) -> None:
        if self.previous:
            self.file.write("\n")
        self.file.write(textwrap.fill(text, self.width))
        self.file.write("\n")
        self.previous = True

    def footer(self):
        pass
