import unittest
from unittest.mock import patch

from chess_mechanics import *



class TestPiece(unittest.TestCase):

    def test_get_colour(self):

        piece = Piece('white')

        self.assertEqual(piece.get_colour(), 'white')


class TestSpot(unittest.TestCase):

    def test_get_spot_colour(self):

        spot = Spot('white', Piece('black'), 0, 0)

        self.assertEqual(spot.get_spot_colour(), 'white')

    def test_get_piece_name(self):

        spot = Spot('white', Piece('black'), 0, 0)

        self.assertEqual(spot.get_piece_name(), 'Piece')

    def test_get_posn(self):

        spot = Spot('white', Piece('black'), 1, 5)

        self.assertEqual(spot.get_posn(), (1, 5))


class TestBoard(unittest.TestCase):

    def test_board_pieces(self):
        #Checks if the game's board pieces matchup with the ideal board's pieces

        ideal_board = {1: {1: Spot('White', Rook('White'), 1, 1), 2: Spot('Black', Knight('White'), 1, 2), 3: Spot('White', Bishop('White'), 1, 3),
                          4: Spot('Black', Queen('White'), 1, 4), 5: Spot('White', King('White'), 1, 5), 6: Spot('Black', Bishop('White'), 1, 6),
                          7: Spot('White', Knight('White'), 1, 7), 8:Spot('Black', Rook('White'), 1, 8)},

                      2: {1: Spot('Black', Pawn('White'), 2, 1), 2: Spot('White', Pawn('White'), 2, 2), 3: Spot('Black', Pawn('White'), 2, 3),
                          4: Spot('White', Pawn('White'), 2, 4), 5: Spot('Black', Pawn('White'), 2, 5), 6: Spot('White', Pawn('White'), 2, 6),
                          7: Spot('Black', Pawn('White'), 2, 7), 8: Spot('White', Pawn('White'), 2, 8)},

                      3: {1: Spot('White', Empty('Blank'), 3, 1), 2: Spot('Black', Empty('Blank'), 3, 2), 3: Spot('White', Empty('Blank'), 3, 3),
                          4: Spot('Black', Empty('Blank'), 3, 4), 5: Spot('White', Empty('Blank'), 3, 5), 6: Spot('Black', Empty('Blank'), 3, 6),
                          7: Spot('White', Empty('Blank'), 3, 7), 8:Spot('Black', Empty('Blank'), 3, 8)},

                      4: {1: Spot('Black', Empty('Blank'), 4, 1), 2: Spot('White', Empty('Blank'), 4, 2), 3: Spot('Black', Empty('Blank'), 4, 3),
                          4: Spot('White', Empty('Blank'), 4, 4), 5: Spot('Black', Empty('Blank'), 4, 5), 6: Spot('White', Empty('Blank'), 4, 6),
                          7: Spot('Black', Empty('Blank'), 4, 7), 8: Spot('White', Empty('Blank'), 4, 8)},

                      5: {1: Spot('White', Empty('Blank'), 5, 1), 2: Spot('Black', Empty('Blank'), 5, 2), 3: Spot('White', Empty('Blank'), 5, 3),
                          4: Spot('Black', Empty('Blank'), 5, 4), 5: Spot('White', Empty('Blank'), 5, 5), 6: Spot('Black', Empty('Blank'), 5, 6),
                          7: Spot('White', Empty('Blank'), 5, 7), 8: Spot('Black', Empty('Blank'), 5, 8)},

                      6: {1: Spot('Black', Empty('Blank'), 6, 1), 2: Spot('White', Empty('Blank'), 6, 2), 3: Spot('Black', Empty('Blank'), 6, 3),
                          4: Spot('White', Empty('Blank'), 6, 4), 5: Spot('Black', Empty('Blank'), 6, 5), 6: Spot('White', Empty('Blank'), 6, 6),
                          7: Spot('Black', Empty('Blank'), 6, 7), 8: Spot('White', Empty('Blank'), 6, 8)},

                      7: {1: Spot('White', Pawn('Black'), 7, 1), 2: Spot('Black', Pawn('Black'), 7, 2), 3: Spot('White', Pawn('Black'), 7, 3),
                          4: Spot('Black', Pawn('Black'), 7, 4), 5: Spot('White', Pawn('Black'), 7, 5), 6: Spot('Black', Pawn('Black'), 7, 6),
                          7: Spot('White', Pawn('Black'), 7, 7), 8: Spot('Black', Pawn('Black'), 7, 8)},

                      8: {1: Spot('Black', Rook('Black'), 8, 1), 2: Spot('White', Knight('Black'), 8, 2), 3: Spot('Black', Bishop('Black'), 8, 3),
                          4: Spot('White', Queen('Black'), 8, 4), 5: Spot('Black', King('Black'), 8, 5), 6: Spot('White', Bishop('Black'), 8, 6),
                          7: Spot('Black', Knight('Black'), 8, 7), 8: Spot('White', Rook('Black'), 8, 8)}}

        game = Board()      
        game_board = game.get_board()

        for row_index in range(8, 0, -1):
            for clmn_index in range(1, 9, 1):

                self.assertEqual(type(game_board[row_index][clmn_index]._piece), type(ideal_board[row_index][clmn_index]._piece))

    def test_board_spotColour(self):
        #Checks if the game's board spots share the same colour pattern as the ideal board's spots

        ideal_board = {1: {1: Spot('White', Rook('White'), 1, 1), 2: Spot('Black', Knight('White'), 1, 2), 3: Spot('White', Bishop('White'), 1, 3),
                          4: Spot('Black', Queen('White'), 1, 4), 5: Spot('White', King('White'), 1, 5), 6: Spot('Black', Bishop('White'), 1, 6),
                          7: Spot('White', Knight('White'), 1, 7), 8:Spot('Black', Rook('White'), 1, 8)},

                      2: {1: Spot('Black', Pawn('White'), 2, 1), 2: Spot('White', Pawn('White'), 2, 2), 3: Spot('Black', Pawn('White'), 2, 3),
                          4: Spot('White', Pawn('White'), 2, 4), 5: Spot('Black', Pawn('White'), 2, 5), 6: Spot('White', Pawn('White'), 2, 6),
                          7: Spot('Black', Pawn('White'), 2, 7), 8: Spot('White', Pawn('White'), 2, 8)},

                      3: {1: Spot('White', Empty('Blank'), 3, 1), 2: Spot('Black', Empty('Blank'), 3, 2), 3: Spot('White', Empty('Blank'), 3, 3),
                          4: Spot('Black', Empty('Blank'), 3, 4), 5: Spot('White', Empty('Blank'), 3, 5), 6: Spot('Black', Empty('Blank'), 3, 6),
                          7: Spot('White', Empty('Blank'), 3, 7), 8:Spot('Black', Empty('Blank'), 3, 8)},

                      4: {1: Spot('Black', Empty('Blank'), 4, 1), 2: Spot('White', Empty('Blank'), 4, 2), 3: Spot('Black', Empty('Blank'), 4, 3),
                          4: Spot('White', Empty('Blank'), 4, 4), 5: Spot('Black', Empty('Blank'), 4, 5), 6: Spot('White', Empty('Blank'), 4, 6),
                          7: Spot('Black', Empty('Blank'), 4, 7), 8: Spot('White', Empty('Blank'), 4, 8)},

                      5: {1: Spot('White', Empty('Blank'), 5, 1), 2: Spot('Black', Empty('Blank'), 5, 2), 3: Spot('White', Empty('Blank'), 5, 3),
                          4: Spot('Black', Empty('Blank'), 5, 4), 5: Spot('White', Empty('Blank'), 5, 5), 6: Spot('Black', Empty('Blank'), 5, 6),
                          7: Spot('White', Empty('Blank'), 5, 7), 8: Spot('Black', Empty('Blank'), 5, 8)},

                      6: {1: Spot('Black', Empty('Blank'), 6, 1), 2: Spot('White', Empty('Blank'), 6, 2), 3: Spot('Black', Empty('Blank'), 6, 3),
                          4: Spot('White', Empty('Blank'), 6, 4), 5: Spot('Black', Empty('Blank'), 6, 5), 6: Spot('White', Empty('Blank'), 6, 6),
                          7: Spot('Black', Empty('Blank'), 6, 7), 8: Spot('White', Empty('Blank'), 6, 8)},

                      7: {1: Spot('White', Pawn('Black'), 7, 1), 2: Spot('Black', Pawn('Black'), 7, 2), 3: Spot('White', Pawn('Black'), 7, 3),
                          4: Spot('Black', Pawn('Black'), 7, 4), 5: Spot('White', Pawn('Black'), 7, 5), 6: Spot('Black', Pawn('Black'), 7, 6),
                          7: Spot('White', Pawn('Black'), 7, 7), 8: Spot('Black', Pawn('Black'), 7, 8)},

                      8: {1: Spot('Black', Rook('Black'), 8, 1), 2: Spot('White', Knight('Black'), 8, 2), 3: Spot('Black', Bishop('Black'), 8, 3),
                          4: Spot('White', Queen('Black'), 8, 4), 5: Spot('Black', King('Black'), 8, 5), 6: Spot('White', Bishop('Black'), 8, 6),
                          7: Spot('Black', Knight('Black'), 8, 7), 8: Spot('White', Rook('Black'), 8, 8)}}

        game = Board()      
        game_board = game.get_board()

        for row_index in range(8, 0, -1):
            for clmn_index in range(1, 9, 1):

                self.assertEqual(type(game_board[row_index][clmn_index]._spotColour), type(ideal_board[row_index][clmn_index]._spotColour))

    def test_board_posn(self):
        #Checks if the game's board positions are the same as the ideal board's positions.

        ideal_board = {1: {1: Spot('White', Rook('White'), 1, 1), 2: Spot('Black', Knight('White'), 1, 2), 3: Spot('White', Bishop('White'), 1, 3),
                          4: Spot('Black', Queen('White'), 1, 4), 5: Spot('White', King('White'), 1, 5), 6: Spot('Black', Bishop('White'), 1, 6),
                          7: Spot('White', Knight('White'), 1, 7), 8:Spot('Black', Rook('White'), 1, 8)},

                      2: {1: Spot('Black', Pawn('White'), 2, 1), 2: Spot('White', Pawn('White'), 2, 2), 3: Spot('Black', Pawn('White'), 2, 3),
                          4: Spot('White', Pawn('White'), 2, 4), 5: Spot('Black', Pawn('White'), 2, 5), 6: Spot('White', Pawn('White'), 2, 6),
                          7: Spot('Black', Pawn('White'), 2, 7), 8: Spot('White', Pawn('White'), 2, 8)},

                      3: {1: Spot('White', Empty('Blank'), 3, 1), 2: Spot('Black', Empty('Blank'), 3, 2), 3: Spot('White', Empty('Blank'), 3, 3),
                          4: Spot('Black', Empty('Blank'), 3, 4), 5: Spot('White', Empty('Blank'), 3, 5), 6: Spot('Black', Empty('Blank'), 3, 6),
                          7: Spot('White', Empty('Blank'), 3, 7), 8:Spot('Black', Empty('Blank'), 3, 8)},

                      4: {1: Spot('Black', Empty('Blank'), 4, 1), 2: Spot('White', Empty('Blank'), 4, 2), 3: Spot('Black', Empty('Blank'), 4, 3),
                          4: Spot('White', Empty('Blank'), 4, 4), 5: Spot('Black', Empty('Blank'), 4, 5), 6: Spot('White', Empty('Blank'), 4, 6),
                          7: Spot('Black', Empty('Blank'), 4, 7), 8: Spot('White', Empty('Blank'), 4, 8)},

                      5: {1: Spot('White', Empty('Blank'), 5, 1), 2: Spot('Black', Empty('Blank'), 5, 2), 3: Spot('White', Empty('Blank'), 5, 3),
                          4: Spot('Black', Empty('Blank'), 5, 4), 5: Spot('White', Empty('Blank'), 5, 5), 6: Spot('Black', Empty('Blank'), 5, 6),
                          7: Spot('White', Empty('Blank'), 5, 7), 8: Spot('Black', Empty('Blank'), 5, 8)},

                      6: {1: Spot('Black', Empty('Blank'), 6, 1), 2: Spot('White', Empty('Blank'), 6, 2), 3: Spot('Black', Empty('Blank'), 6, 3),
                          4: Spot('White', Empty('Blank'), 6, 4), 5: Spot('Black', Empty('Blank'), 6, 5), 6: Spot('White', Empty('Blank'), 6, 6),
                          7: Spot('Black', Empty('Blank'), 6, 7), 8: Spot('White', Empty('Blank'), 6, 8)},

                      7: {1: Spot('White', Pawn('Black'), 7, 1), 2: Spot('Black', Pawn('Black'), 7, 2), 3: Spot('White', Pawn('Black'), 7, 3),
                          4: Spot('Black', Pawn('Black'), 7, 4), 5: Spot('White', Pawn('Black'), 7, 5), 6: Spot('Black', Pawn('Black'), 7, 6),
                          7: Spot('White', Pawn('Black'), 7, 7), 8: Spot('Black', Pawn('Black'), 7, 8)},

                      8: {1: Spot('Black', Rook('Black'), 8, 1), 2: Spot('White', Knight('Black'), 8, 2), 3: Spot('Black', Bishop('Black'), 8, 3),
                          4: Spot('White', Queen('Black'), 8, 4), 5: Spot('Black', King('Black'), 8, 5), 6: Spot('White', Bishop('Black'), 8, 6),
                          7: Spot('Black', Knight('Black'), 8, 7), 8: Spot('White', Rook('Black'), 8, 8)}}

        game = Board()      
        game_board = game.get_board()

        for row_index in range(8, 0, -1):
            for clmn_index in range(1, 9, 1):

                self.assertEqual(type(game_board[row_index][clmn_index]._posn), type(ideal_board[row_index][clmn_index]._posn))

    def test_update_board(self):
        #Testing update_board method 

        game = Board()
        game_board = game.get_board()
        
        rook_object = game_board[1][1]._piece
        game.update_board((1, 1), (3, 3), rook_object)
        #moves former rook object at (1, 1) to (3, 3)
        
        self.assertEqual(game_board[1][1].get_piece_name(), 'Empty')
        #Checks if (1, 1) now contains an object called 'Empty'

        self.assertEqual(game_board[3][3]._piece, rook_object)
        #Checks if spot rook moved to now has rook

    def test_get_spot(self):
        #Testing get_spot method 

        game = Board()
        game_board = game.get_board()

        tested_spot = game_board[1][2] #Spot at (1, 2)
        self.assertEqual(game.get_spot((1, 2)), tested_spot)

    def test_check_spot_empty(self):
        #Testing check_spot_empty() method

        game = Board()
        game_board = game.get_board()

        empty_spot = game.get_spot((3, 3))
        not_empty_spot = game_board[1][1]

        self.assertEqual(game.check_spot_empty((3, 3)), empty_spot.get_piece_name() == 'Empty')
        #Checks if empty spot is empty (returns True)

        self.assertNotEqual(game.check_spot_empty((3, 3)), not_empty_spot.get_piece_name() == 'Empty')
        #Checking if not empty is empty (returns False)

    def test_check_spots_white(self):
        #Testing check_spots() method, when passing in White as argument for piece colour

        #note: The program passes in a list of lists, which has a list of moves for every 
        #potential axis combination, i.e ([+ve y], [+ve y and +ve x], [+ve x], [-ve y and +ve x]...), 

        #The result is a single list of all possible moves

        game = Board()
        game_board = game.get_board()

        List_of_moves = [[(5, 3), (6, 3), (7 ,3), (8, 3)],           [(6, 4), (7, 5), (8, 6)],
                         [(5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],   [(4, 4), (3, 5), (2, 6), (1, 7)],
                         [(4, 3), (3, 3), (2, 3), (1, 3)],           [(4, 2), (3, 1)],
                         [(5, 2), (5, 1)],                           [(6, 2), (7, 1)]]
        
        #Format =       [[+ve y],                                    [+ve y, +ve x]
        #                [+ve x],                                    [-ve y, +ve x]
        #                [-ve y],                                    [-ve y, -ve x]
        #                [-ve x],                                    [+ve y, -ve x]

        list_after_filter = [(5, 3), (6, 3), (7 ,3),                   (6, 4), (7, 5),
                             (5, 4), (5, 5), (5, 6), (5, 7),(5, 8),    (4, 4), (3, 5),
                             (4, 3), (3, 3),                           (4, 2), (3, 1), 
                             (5, 2), (5, 1),                           (6, 2), (7, 1)]

        game_approved_moves = game.check_spots('White', List_of_moves)
        self.assertEqual(game_approved_moves, list_after_filter)




if __name__ == '__main__':
    unittest.main()
    