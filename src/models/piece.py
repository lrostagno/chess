class Piece:
    def __init__(self, x=0, y=0, color='w'):
        self.x = x
        self.y = y
        self.color = color

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_possible_moves(self):
        pass

    def take(self, x, y):
        self.move(x, y)

    

class Pawn(Piece):
    def __repr__(self):
        return f'{self.color}p'

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
