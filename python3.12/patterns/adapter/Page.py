#! /usr/bin/env python3
from typing import Callable
from Renderer import Renderer


class Page:

    """This class implemanted a methods for draw page and render page"""

    def __init__(self, title: str, renderer: Callable) -> None:
        if not isinstance(renderer, Renderer):
            raise TypeError(
                f"Expected object if type Renderer, got -> {type(renderer).__name__}"
            )
        self.title = title
        self.renderer = renderer
        self.paragraphs = []

    def add_paragraph(self, paragraph: str) -> None:
        self.paragraphs.append(paragraph)

    def render(self) -> None:
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()
