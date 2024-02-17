import numpy as np
from src.models.piece import *
class Board:
    def __init__(self):
        self.board = [['']*8 for _ in range(8)] 
        print('test')
        print(self.board)
        #self.init_board()
        #self.get_board_dict()
        

    def init_board(self):
        self.board[0] = [Rook(0, 0, 'b'), Knight(1, 0, 'b'), Bishop(2, 0, 'b'), Queen(3, 0, 'b'), King(4, 0, 'b'), Bishop(5, 0, 'b'), Knight(6, 0, 'b'), Rook(7, 0, 'b')]
        self.board[1] = [Pawn(0, 1, 'b'), Pawn(1, 1, 'b'), Pawn(2, 1, 'b'), Pawn(3, 1, 'b'), Pawn(4, 1, 'b'), Pawn(5, 1, 'b'), Pawn(6, 1, 'b'), Pawn(7, 1, 'b')]
        self.board[6] = [Pawn(0, 6), Pawn(1, 6), Pawn(2, 6), Pawn(3, 6), Pawn(4, 6), Pawn(5, 6), Pawn(6, 6), Pawn(7, 6)]
        self.board[7] = [Rook(0, 7), Knight(1, 7), Bishop(2, 7), Queen(3, 7), King(4, 7), Bishop(5, 7), Knight(6, 7), Rook(7, 7)]

    def print_board(self):
        for i in range(8):
            print(self.board[i])
            
    def __str__(self) -> str:
        return 'Test...'
    
    def move_piece(self, square_from, square_to):
        old_row, old_col = self.board_dict[square_from]
        piece = self.board[old_row][old_col]
        self.board[old_row][old_col] = ''
        new_row, new_col = self.board_dict[square_to]
        self.board[new_row][new_col] = piece

    def get_board_dict(self):
        self.board_dict = {}
        columns = 'abcdefgh'
        numbers = '12345678'
        for r, num in enumerate(reversed(numbers)):
            for c, col in enumerate(columns):
                self.board_dict[col + num] = (r, c)


    def get_piece(self, square):
        row, col = self.board_dict[square]
        return self.board[row][col]


    def check_pawn_moves(self):
        pass