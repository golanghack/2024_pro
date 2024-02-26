#! /usr/bin/nev python3

from main import get_prefix, hello


def test_get_prefix():
    got = get_prefix("Spanish")
    want = "Hola, "
    assert got == want


def test_get_prefix_empty():
    got = get_prefix("")
    want = "Hello, "
    assert got == want


def test_hello():
    got = hello("Boris", "Russian")
    want = "Привет, Boris"
    assert got == want


def test_hello_default():
    got = hello("", "")
    want = "Hello, World"
    assert got == want
