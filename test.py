# %%
%load_ext autoreload
%autoreload 2
# %%
class Board:
    def __init__(self):
        self.board = [''] * 64
        self.cols_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.rows_dict = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    def __repr__(self):
        return '\n'.join([str(self.board[i:i+8]) for i in range(0, 64, 8)])
    
    def _get_square_idx(self, square):
        col, row = square[0], square[1]
        return self.rows_dict[row] * 8 + self.cols_dict[col]
    
    def move_piece(self, old_square, new_square):
        if old_square == new_square:
            return
        old_idx = self._get_square_idx(old_square)
        new_idx = self._get_square_idx(new_square)
        piece = self.board[old_idx]
        if piece == '':
            print('No piece to move...')
            return
        self.board[new_idx] = piece
        self.board[old_idx] = ''

    def set_piece(self, square, piece):
        idx = self._get_square_idx(square)
        self.board[idx] = piece

    def get_possible_moves(self, square):
        col, row = square[0], square[1]
        if row == '2':
            return [self._get_square_idx(square) - 8, self._get_square_idx(square) - 16]
        else:
            return [self._get_square_idx(square) - 8]

    def show_possible_moves(self, square):
        if self.board[self._get_square_idx(square)] == '':
            print('No piece to move...')
            return
        board = self.board.copy()
        possible_moves = self.get_possible_moves(square)
        for move in possible_moves:
            board[move] = '*'
        
        print('\n'.join([str(board[i:i+8]) for i in range(0, 64, 8)]))
# %%
board = Board()
board.set_piece('a1', 'wP')
board.move_piece('a1', 'a2')
# %%
board
# %%
board.show_possible_moves('a4')
# %%
board.move_piece('a2', 'a4')
# %%
board
# %%
a = board.get_possible_moves('a4')
# %%
a
# %%
