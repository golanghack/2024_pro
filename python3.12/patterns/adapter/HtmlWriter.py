#! /usr/bin/env python3

import sys
from html import escape


class HtmlWriter:
    def __init__(self, file: str = sys.stdout) -> None:
        self.file = file

    def header(self) -> None:
        self.file.write("<!Doctype html>\n<html>\n")

    def title(self, title: str) -> None:
        self.file.write(f"<head><title>{escape(title)}</title></head>")

    def start_body(self) -> None:
        self.file.write("<body>\n")

    def body(self, text: str) -> None:
        self.file.write(f"<p>{escape(text)}</p>\n")

    def end_body(self) -> None:
        self.file.write("</body>\n")

    def footer(self):
        self.file.write("</html>\n")
