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
board.move_piece('a2', 'a3')
# %%
