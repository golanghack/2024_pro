#! /usr/bin/env python3

import sys
from Page import Page
from TextRenderer import TextRenderer
from HtmlRenderer import HtmlRenderer
from HtmlWriter import HtmlWriter
from consts import *


def main():
    paragraph_1 = MESSAGE.format("plain-text", "TextRenderer")
    paragraph_2 = """This is another short paragraph just so that we can
see two paragraphs in action."""
    title = "Plain"
    text_page = Page(title, TextRenderer(22))
    text_page.add_paragraph(paragraph_1)
    text_page.add_paragraph(paragraph_2)
    text_page.render()

    print()

    paragraph_1 = MESSAGE.format("Html", "HtmlRenderer")
    title = "Html"
    file = sys.stdout
    html_page = Page(title, HtmlRenderer(HtmlWriter(file)))
    html_page.add_paragraph(paragraph_1)
    html_page.add_paragraph(paragraph_2)
    html_page.render()

    try:
        page = Page(title, HtmlWriter())
        page.render()
        print("Error! Render wir an invalid")
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()
