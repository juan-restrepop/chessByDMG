class Piece(object):
    kind = str()
    color = str()
    coordinates = list()
    has_moved = False

    def __init__(self, kind, color, coordinate):
        self.initialize_piece(kind, color, coordinate)

    def initialize_piece(self, kind, color, coordinate):
        self.kind = kind
        self.color = color
        self.coordinates = coordinate

    def get_natural_moves(self):
        pass

class Pawn(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'p', color, coordinates)

class Rook(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'r', color, coordinates)


class Bishop(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'b', color, coordinates)

class Knight(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'n', color, coordinates)

class Queen(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'q', color, coordinates)

class King(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'k', color, coordinates)

    def get_natural_moves(self):
        line,row = self.coordinates
        nat_moves = []
        # generate all possible coordinates
        nat_moves = [[line+k,row+j] for k in [-1,0,+1] for j in [-1,0,1] if not(k==0 and j==0)]
        # filter to get valid board coordinates
        nat_moves = [ [k,j] for [k,j] in nat_moves if (k>=0 and j>=0) and (k<8 and j<8) ]
        return nat_moves

