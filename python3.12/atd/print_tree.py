#! /usr/bin/env python3


def print_tree(tree):
    """Printing tree elements"""
    print(tree.data)
    for child in tree.children:
        print_tree(child)
