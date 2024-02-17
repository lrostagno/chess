class Piece:
    def __init__(self, color='w'):
        self.color = color

    def get_possible_moves(self):
        pass

    

class Pawn(Piece):
    def __repr__(self):
        return f'{self.color}p'

    def get_moves(self):
        

class Rook(Piece):
    def __repr__(self):
        return f'{self.color}R'

class Knight(Piece):
    def __repr__(self):
        return f'{self.color}N'

class Bishop(Piece):
    def __repr__(self):
        return f'{self.color}B'

class Queen(Piece):
    def __repr__(self):
        return f'{self.color}Q'

class King(Piece):
    def __repr__(self):
        return f'{self.color}K'
