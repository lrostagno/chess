# %%
%load_ext autoreload
%autoreload 2
# %%
from src.models.board import Board
# %%
board = Board()
# %%
board.board
# %%
piece = board.get_piece('e2')
# %%
board
# %%
board.board
# %%
inverted_chess_board = board.board[::-1]
# %%
inverted_chess_board
# %%
