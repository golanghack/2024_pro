#! /usr/bin/env python3


from consts import *


def create_piece(kind, color):
    color = "White" if color == WHITE else "Black"
    name = {
        DRAUGHT: "Draught",
        PAWN: "ChessPawn",
        ROOK: "ChessRook",
        KNIGHT: "ChessKnight",
        BISHOP: "ChessBishop",
        KING: "ChessKing",
        QUEEN: "ChessQueen",
    }[kind]
    return globals()[color + name]()
