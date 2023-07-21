from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, colour: str):
        #Sets up initial values for a piece

        self._colour = colour


    def get_position(self) -> tuple:
        #Returns current position of piece on board

        return self._position
    

    def get_colour(self) -> str:

        return self._colour
    
    
    @abstractmethod
    def move(self):
        #Moves piece based on what it is able to do
        pass


class Pawn(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position


class Rook(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position


class Bishop(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position


class Knight(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position        


class Queen(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position


class King(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position


class Empty(Piece):
    
    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, row_index: int, clmn_index: int, board: 'Board'):

        new_position = (row_index, clmn_index)
        board.update_board(self._position, new_position, self)
        self._position = new_position


class Spot():

    def __init__(self, colour, piece, row_index: int, clmn_index: int):

        self._spotColour = colour
        self._piece = piece
        self._position = (row_index, clmn_index)

    def get_piece(self) -> object:

        return self._piece.__class__.__name__
    
    def get_position(self) -> tuple:

        return self._position
    
    def move_piece(self, row_index: int, clmn_index: int, board: 'Board'):

        self._piece().move(row_index, clmn_index, board)



class Board():

    def __init__(self):

        
        w_piece_list = {1:{1: Rook("White"), 2: Knight("White"), 3: Bishop("White"), 4: Queen("White"),
                    5: King("White"), 6: Bishop("White"), 7: Knight("White"), 8: Rook("White")},
                    2: {1: Pawn("White"), 2: Pawn("White"), 3: Pawn("White"), 4: Queen("White"),
                    5: Pawn("White"), 6: Pawn("White"), 7: Pawn("White"), 8 :Pawn("White")}}
        
        b_piece_list = {7:{1:Pawn("Black"), 2: Pawn("Black"), 3: Pawn("Black"), 4: Pawn("Black"),
                    5: Pawn("Black"), 6: Pawn("Black"), 7: Pawn("Black"), 8: Pawn("Black")},
                    8: {1: Rook("Black"), 2: Knight("Black"), 3: Bishop("Black"), 4: Queen("Black"),
                    5: King("Black"), 6: Bishop("Black"), 7: Knight("Black"), 8: Rook("Black")}}

        self._board = {}

        for row_index in range(1, 9):
            self._board[row_index] = {}

            for clmn_index in range(1, 9):

                if ((row_index % 2 == 0) & (clmn_index % 2 == 0)) or ((row_index % 2 == 1) & (clmn_index % 2 == 1)):

                    if (row_index <= 2):
                        self._board[row_index][clmn_index] = Spot("White", w_piece_list[row_index][clmn_index], row_index, clmn_index)

                    elif (row_index >= 7):
                        self._board[row_index][clmn_index] = Spot("White", b_piece_list[row_index][clmn_index], row_index, clmn_index)

                    else:
                        self._board[row_index][clmn_index] = Spot("White", Empty('Blank'), row_index, clmn_index)
                

                if ((row_index % 2 == 0) & (clmn_index % 2 == 1)) or ((row_index % 2 == 1) & (clmn_index % 2 == 0)):
                    
                    if (row_index <= 2):
                        self._board[row_index][clmn_index] = Spot("Black", w_piece_list[row_index][clmn_index], row_index, clmn_index)

                    elif (row_index >= 7):
                        self._board[row_index][clmn_index] = Spot("Black", b_piece_list[row_index][clmn_index], row_index, clmn_index)

                    else:
                        self._board[row_index][clmn_index] = Spot("Black", Empty('Blank'), row_index, clmn_index)

        
    def update_board(self, current_position, new_position, piece_type: Piece):

        prev_row_index = current_position[0]
        prev_clmn_index = current_position[1]
        new_row_index = new_position[0]
        new_clmn_index = new_position[1]
        
        old_spot_colour = self._board[prev_row_index][prev_clmn_index].get_colour()
        new_spot_colour = self._board[new_row_index][new_clmn_index].get_colour()

        self._board[prev_clmn_index][prev_row_index] = Spot(old_spot_colour, None)
        self._board[new_clmn_index][new_row_index] = Spot(new_spot_colour, piece_type)


    def print_board(self):

        for row_index in range(8, 0, -1):
            print("")
            for clmn_index in range (1, 9, 1):
                print(self._board[row_index][clmn_index].get_piece(), end=" ")

    
    def get_spot(self, row_index, clmn_index):

        return self._board[row_index][clmn_index]



word = Board()
word.get_spot(2, 3).move_piece(2, 4, word)
word.print_board()