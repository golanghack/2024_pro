#! /usr/bin/env python3

from HtmlWriter import HtmlWriter


class HtmlRenderer:
    def __init__(self, htmlWriter) -> None:
        self.htmlWriter = htmlWriter

    def header(self, title: str) -> None:
        self.htmlWriter.header()
        self.htmlWriter.title(title)
        self.htmlWriter.start_body()

    def paragraph(self, text: str) -> None:
        self.htmlWriter.body(text)

    def footer(self) -> None:
        self.htmlWriter.end_body()
        self.htmlWriter.footer()
