#! /usr/bin/env python3

from consts import *
from AbstractBoard import AbstractBoard
from create_piece import create_piece


class ChessBoard(AbstractBoard):
    def __init__(self):
        super().__init__(8, 8)

    def populate_board(self):
        for row, color in ((0, BLACK), (7, WHITE)):
            for columns, kind in (
                ((0, 7), ROOK),
                ((1, 6), KNIGHT),
                ((2, 5), BISHOP),
                ((3,), QUEEN),
                ((4,), KING),
            ):
                for column in columns:
                    self.board[row][column] = create_piece(kind, color)
        for column in range(8):
            for row, color in ((1, BLACK), (6, WHITE)):
                self.board[row][column] = create_piece(PAWN, color)
