import numpy as np
import math
import random

class Othello:
    # Class constants
    # Black disc, white disc and empty square
    BLACK, WHITE, EMPTY = 1, -1, 0


    def __init__(self):
        self.board = np.full((8, 8), self.EMPTY)
        self.board[3][3] = self.BLACK
        self.board[4][4] = self.BLACK
        self.board[3][4] = self.WHITE
        self.board[4][3] = self.WHITE
        self.flip_discs = []


    @property
    def black_discs(self):
        discs = 0
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == self.BLACK:
                    discs += 1
        return discs

    @property
    def white_discs(self):
        discs = 0
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == self.WHITE:
                    discs += 1
        return discs
