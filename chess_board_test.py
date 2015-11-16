import unittest
import chess_board as cb

class TestChessBoard(unittest.TestCase):
    
    def test_initialize_board_object_number_of_pieces(self):
        b = cb.ChessBoard()
        
        expected = 32
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = 2
        for knights in [b.knights_w, b.knights_b]:
            actual = len(knights)
            self.assertEqual(expected, actual)

        expected = 1
        for queens in [b.queen_w, b.queen_b]:
            actual = len(queens)
            self.assertEqual(expected, actual)

        expected = 1
        for kings in [b.king_w, b.king_b]:
            actual = len(kings)
            self.assertEqual(expected, actual)

        expected = 8 
        actual = len(b.pawns_w)
        self.assertEqual(expected, actual)

        expected = 8 
        actual = len(b.pawns_b)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.rooks_w)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.rooks_b)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.bishops_w)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.bishops_b)
        self.assertEqual(expected, actual)

    def test_initialize_board_object_position_of_pieces(self):
        b = cb.ChessBoard()

        # black pieces
        expected = True
        for pawn in b.pawns_b:
            positions = []
            for col in range(8):
                positions.append([1, col])
            actual = pawn.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True 
        for rook in b.rooks_b:
            positions = [[0,0],[0,7]]
            actual = rook.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for knight in b.knights_b:
            positions = [[0,1],[0,6]]
            actual = knight.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for bishop in b.bishops_b:
            positions = [[0,2],[0,5]]
            actual = bishop.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for queen in b.queen_b:
            position = [0,3]
            actual = queen.coordinates == position
            self.assertEqual(expected, actual)

        expected = True
        for king in b.king_b:
            position = [0,4]
            actual = king.coordinates == position
            self.assertEqual(expected, actual)

        # white pieces
        expected = True
        for pawn in b.pawns_w:
            positions = []
            for col in range(8):
                positions.append([6, col])
            actual = pawn.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for rook in b.rooks_w:
            actual = rook.coordinates in [ [7, 0], [7,7]]
            self.assertEqual(expected, actual)

        expected = True
        for knight in b.knights_w:
            actual = knight.coordinates in [ [7, 1], [7,6]]
            self.assertEqual(expected, actual)

        expected = True
        for bishop in b.bishops_w:
            actual = bishop.coordinates in [ [7, 2], [7,5]]
            self.assertEqual(expected, actual)

        expected = True
        for queen in b.queen_w:
            actual = queen.coordinates == [7, 3]
            self.assertEqual(expected, actual)

        expected = True
        for king in b.king_w:
            actual = king.coordinates == [7, 4]
            self.assertEqual(expected, actual)

    def test_get_square_color(self):
        
        b = cb.ChessBoard()
        b.initialize_board()

        expected = 0
        actual = b.get_square_color(0, 0)
        self.assertEqual(expected, actual)

        expected = 1
        actual = b.get_square_color(1, 0)
        self.assertEqual(expected, actual)

    def test_clean_pieces(self):
        b = cb.ChessBoard()

        expected = 0
        
        b.clean_pieces()
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)


    def piece_initialization_test(self, kind, color, coordinates):

        b = cb.ChessBoard()
        ## Initialize single piece
        b.clean_pieces()
        b.initialize_single_piece(kind, color, coordinates)

        piece_to_pieces_list = {'wp':b.pawns_w,
                                'bp':b.pawns_b,
                                'wb':b.bishops_w,
                                'bb':b.bishops_b,
                                'wn':b.knights_w,
                                'bn':b.knights_b,
                                'wr':b.rooks_w,
                                'br':b.rooks_b,
                                'wk':b.king_w,
                                'bk':b.king_b,
                                'wq':b.queen_w,
                                'bq':b.queen_b}

        number_pieces_in_board = len(b.get_all_pieces())
        number_pieces_in_list = len(piece_to_pieces_list[color + kind])
        piece_coordinates = piece_to_pieces_list[color + kind][0].coordinates

        return (number_pieces_in_board, number_pieces_in_list, piece_coordinates)

    def test_initialize_single_pieces(self):
        b = cb.ChessBoard()

        pieces_kind = ['p', 'p', 'b', 'b', 'n', 'n', 'r', 'r', 'k', 'k', 'q', 'q']
        pieces_colors = ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b']
        pieces_coordinates = [[6, 0], [1, 0], [2, 5], [5, 2], [7, 2], [2, 7], [3, 5], [5,3], [3, 4], [4, 3]]

        for (kind, color, coords) in zip(pieces_kind, pieces_colors, pieces_coordinates):
            # Initialization of a single piece
            b.clean_pieces()
            (pieces_in_board, pieces_in_list, piece_coordinates) = self.piece_initialization_test(kind, color, coords)

            # Test if initialization created only 1 piece
            expected = 1
            self.assertEqual(expected, pieces_in_board)

            # Test if initialized the right piece
            expected = 1
            self.assertEqual(expected, pieces_in_list)

            # Test if piece initialized at right coordinates
            expected = coords
            self.assertEqual(expected, piece_coordinates)


    def test_white_pawn_movement_rules(self):
        b = cb.ChessBoard()

        ## Initialize white pawn on 'd2'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))

        ## Test forbidden moves
        # Test forbidden forward-diagonal moves
        expected = False
        for move in [['e','3'], ['c','3']]:
            actual = b.move_pawn_to(move[0], move[1])
            self.assertEqual(expected, actual)

        # Test forbidden lateral moves
        expected = False
        for move in [['e','2'], ['c','2']]:
            actual = b.move_pawn_to(move[0], move[1])
            self.assertEqual(expected, actual)

        # Test forbidden backwards moves
        expected = False
        for move in [['e','1'], ['c','3'], ['d', '1']]:
            actual = b.move_pawn_to(move[0], move[1])
            self.assertEqual(expected, actual)

        # Test forbidden forward move longer than 2
        expected = False
        actual = b.move_pawn_to('d', '5')
        self.assertEqual(expected, actual)

        ## Test approved moves if initial position
        # simple initial move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))

        expected = True
        actual = b.move_pawn_to('d','3')
        self.assertEqual(expected, actual)

        # double initial move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))

        expected = True
        actual = b.move_pawn_to('d','4')
        self.assertEqual(expected, actual)

        ## Test approved moves
        # simple move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '4'))

        expected = True
        actual = b.move_pawn_to('d','5')
        self.assertEqual(expected, actual)

        # double move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '4'))

        expected = False
        actual = b.move_pawn_to('d','6')
        self.assertEqual(expected, actual)

    def test_white_pawn_blocked_movement_rules(self):
        b = cb.ChessBoard()

        ## Initialize white pawn on 'd2' and black knight on 'd3'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('n', 'b', [5, 3])

        expected = False
        actual = b.move_pawn_to('d', '3')
        self.assertEqual(expected, actual)

        ## Initialize white pawn on 'd2' and black knight on 'd3'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('n', 'b', [5, 3])

        expected = False
        actual = b.move_pawn_to('d', '4')

    def test_bishop_movement_rules(self):
        b = cb.ChessBoard()
        
        ## Accepted moves : down-left, down-right, up-left, up-right
        movements = [['d', '3'], ['f', '3'], ['c', '6'], ['h', '7']]
        for move in movements:

            # Test white bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', [4, 4])
            expected = True
            actual = b.move_bishop_to(move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'b', [4, 4])
            expected = True
            actual = b.move_bishop_to(move[0],move[1], 'black')
            self.assertEqual(expected, actual)

        ## Unaccepted moves : left, right, up, down
        movements = [['d', '4'], ['f', '4'], ['e', '6'],['e', '2']]
        for move in movements:

            # Test white bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', [4, 4])
            expected = False
            actual = b.move_bishop_to(move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'b', [4, 4])
            expected = False
            actual = b.move_bishop_to(move[0],move[1], 'black')
            self.assertEqual(expected, actual)

    def test_bishop_blocked_movement_rules(self):

        b = cb.ChessBoard()

        ## test not accepted moves : down-left,down-right,up-left,up-right
        movements = [['d','3'],['f','3'],['c','6'],['h','7']]
        blocking_pieces =  [[5,3], [5,5], [3,3],[2,6]]

        for move,blocking_piece in zip(movements, blocking_pieces):

            # Test white bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', [4, 4])
            b.initialize_single_piece('p', 'b', blocking_piece)
            expected = False
            actual = b.move_bishop_to(move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'b', [4, 4])
            b.initialize_single_piece('p', 'w', blocking_piece)
            expected = False
            actual = b.move_bishop_to(move[0],move[1], 'black')
            self.assertEqual(expected, actual)


    def test_knight_movement_rules(self):
        b = cb.ChessBoard()

        ## Test forbidden moves
        movements = [['d', '3'], ['d','5'], \
                        ['c', '4'], ['e', '4'], \
                        ['c', '5'], ['e', '5'], ['c', '3'], ['e', '3']]

        # Test white knight on 'd4'
        b.clean_pieces()
        b.initialize_single_piece('n', 'w', [4, 3])

        expected = False
        for move in movements:
            actual = b.move_knight_to(move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test black knight on 'd4'
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [4, 3])

        expected = False
        for move in movements:
            actual = b.move_knight_to(move[0], move[1], 'black')
            self.assertEqual(expected, actual)

        ## Test approved moves
        movements = [['b', '5'], ['f', '5'], \
                     ['b', '3'], ['f', '3'], \
                     ['c', '6'], ['e', '6'], \
                     ['c', '2'], ['e', '2']]

        # Test white knight on 'd4'
        b.clean_pieces()

        expected = True
        for move in movements:
            b.clean_pieces()
            b.initialize_single_piece('n', 'w', [4, 3])

            actual = b.move_knight_to(move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test black knight on 'd4'
        b.clean_pieces()

        expected = True
        for move in movements:
            b.clean_pieces()
            b.initialize_single_piece('n', 'b', [4, 3])

            actual = b.move_knight_to(move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    def test_knight_blocked_movement_rules(self):
        b = cb.ChessBoard()

        ## Initialize white knight in 'b1' and white pawns in 'd2' and 'b2'
        b.clean_pieces()
        b.initialize_single_piece('n', 'w', [7, 1])
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('p', 'w', [6, 1])

        # test blocked move
        expected = False
        actual = b.move_knight_to('d', '4', 'white')
        self.assertEqual(expected, actual)

        # test approved move
        expected = True
        actual = b.move_knight_to('a', '3', 'white')
        self.assertEqual(expected, actual)

        ## Initialize black knight in 'b1' and white pawns in 'd2' and 'b2'
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [7, 1])
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('p', 'w', [6, 1])

        # test blocked move
        expected = False
        actual = b.move_knight_to('d', '4', 'black')
        self.assertEqual(expected, actual)

        # test approved move
        expected = True
        actual = b.move_knight_to('a', '3', 'black')
        self.assertEqual(expected, actual)


    def test_rook_movement_rules(self):
        b = cb.ChessBoard()

        ## Test forbidden moves
        movements = [['d', '3'], ['c', '2'], \
                     ['f','5'], ['g', '6']]

        # Test white rook on 'e4'
        b.clean_pieces()
        b.initialize_single_piece('r', 'w', [4, 4])
        expected = False
        for move in movements:
            actual = b.move_rook_to(move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test black rook on 'e4'
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', [4, 4])
        expected = False
        for move in movements:
            actual = b.move_rook_to(move[0], move[1], 'black')
            self.assertEqual(expected, actual)

        ## Test approved moves
        movements = [['f','4'], ['g', '4'], \
                     ['e','7'], ['e', '8'], \
                     ['b', '4'], \
                     ['e', '1']]

        expected = True
        for move in movements:
            # Test white rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'w', [4, 4])
            actual = b.move_rook_to(move[0], move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'b', [4, 4])
            actual = b.move_rook_to(move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    def test_white_rook_blocked_movement_rules(self):
        b = cb.ChessBoard()

        ## Blocking white pawn in 'g4' and black knight in 'e6'

        ## Test non-blocked movements
        movements = [['e', '5'], ['f', '4']]
        expected = True
        for move in movements:
            # Test white rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'w', [4, 4])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('n', 'b', [2, 4])

            actual = b.move_rook_to(move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        ## Test blocked movements
        movements = [['e', '6'], ['h', '4']]
        expected = False
        for move in movements:
            # Test white rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'w', [4, 4])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('n', 'b', [2, 4])

            actual = b.move_rook_to(move[0], move[1], 'white')
            self.assertEqual(expected, actual)


    def test_white_king_movement_rules(self):
        b = cb.ChessBoard()

        # We initialize white king in 'f5' aka [3,5]
        # accepted moves
        for move in [['e', '6'], ['f', '6'], ['g', '6'],
                     ['e', '5'], ['g','5'],
                     ['e', '4'], ['f', '4'], ['g', '4']]:

            b.clean_pieces()
            b.initialize_single_piece('k', 'w', [3, 5])
            expected = True
            actual = b.move_king_to(move[0],move[1])
            self.assertEqual(expected, actual)
        
        # unaccepted moves c8,f7,h7,h5,h3,f3,c2
        for move in [['c', '8'], ['f', '7'],['h', '7'],
                     ['a', '5'], ['h', '5'],
                     ['h', '3'], ['f', '3'], ['c', '2'],
                     ['g', '3']]:
            b.clean_pieces()
            b.initialize_single_piece('k', 'w', [3, 5])
            expected = False
            actual = b.move_king_to(move[0],move[1])
            self.assertEqual(expected, actual)

    def test_white_king_blocked_movement_rules(self):
        b = cb.ChessBoard()
        # We initialize white king in 'e3' aka [5,4]
        for move, blocking_piece in zip([['d', '4'], ['e', '4'], ['f', '4'],
                                         ['d', '3'], ['f', '3'], 
                                         ['d', '2'], ['e', '2'], ['f', '2']],
                                        [['d', '4'], ['e', '4'], ['f', '4'],
                                         ['d', '3'], ['f', '3'], 
                                         ['d', '2'], ['e', '2'], ['f', '2']]):
            b.clean_pieces()
            b.initialize_single_piece('k','w',[5,4])
            b.initialize_single_piece('k','w',
                b.transform_board_to_grid(blocking_piece[0],blocking_piece[1]))
        # accepted moves


    def test_white_queen_movement_rules(self):
        b = cb.ChessBoard()

        # Queen initialized in 'c4'
        movements = [['b', '4'], ['a', '2'], ['c', '1'], ['f', '1'], ['g', '4'], ['g', '8'], ['c', '8'], ['a', '6']]
        expected = True
        for move in movements:
            b.clean_pieces()
            b.initialize_single_piece('q', 'w', [4, 2])

            actual = b.move_queen_to(move[0], move[1])
            self.assertEqual(expected, actual)

    def test_white_queen_blocked_movement_rules(self):
        b = cb.ChessBoard()

        # Queen initialized in 'c4', white pawn initialized 'g4', black rook in 'c6' and black knight in 'f7'
        movements = [['g', '4'], ['h', '4'], ['c', '7'], ['g', '8']]

        expected = False
        for move in movements:
            b.clean_pieces()
            b.initialize_single_piece('q', 'w', [4, 2])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('r', 'b', [2, 2])
            b.initialize_single_piece('n', 'b', [1, 5])

            actual = b.move_queen_to(move[0], move[1])
            self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()





