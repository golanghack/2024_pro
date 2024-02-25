#! /usr/bin/env python3

import itertools
from AbstractBoard import AbstractBoard
from create_piece import create_piece
from consts import *


class CheckersBoard(AbstractBoard):
    def __init__(self):
        self.populate_board()

    def populate_board(self):
        def black():
            return create_piece(DRAUGHT, BLACK)

        def white():
            return create_piece(DRAUGHT, WHITE)

        rows = (
            (None, black()),
            (black(), None),
            (None, black()),
            (black(), None),  # 4 black rows
            (None, None),
            (None, None),  # 2 blank rows
            (None, white()),
            (white(), None),
            (None, white()),
            (white(), None),
        )  # 4 white rows
        self.board = [
            list(itertools.islice(itertools.cycle(squares), 0, len(rows)))
            for squares in rows
        ]
