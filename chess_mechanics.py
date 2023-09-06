from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, colour: str):
        #Sets up initial values for a piece

        self._colour = colour


    def get_colour(self) -> str:

        return self._colour


    @abstractmethod
    def move(self):
        #Moves piece based on what it is able to do
        pass

    """@abstractmethod
    def potential_moves(self):
        #Moves piece based on what it is able to do
        pass"""


class Pawn(Piece):


    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def potential_moves(self, old_posn: tuple, board: 'Board') -> list:

        self._moveList = []
        new_spot_row = old_posn[0] + 1
        new_spot_clmn = old_posn[1]
        new_spot = (new_spot_row, new_spot_clmn)

        if (board.check_spot_empty(new_spot) == True):
            self._moveList.append(new_spot)

        return self._moveList

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn


class Rook(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn
    
    def potential_moves(self, old_posn: tuple, board: 'Board') -> list:


        combined_list = []
        positive_y_list = []
        positive_x_list = []
        negative_y_list = []
        negative_x_list = []
        
        passing = True


        def check_in_range(old_posn: tuple, increment: int, row_or_clmn: str, positive_or_negative: str) -> bool:

            if (row_or_clmn == 'row'):

                if (positive_or_negative == 'positive'):
                
                    if (old_posn[0] + increment == 9):
                        return False
                    
                    else:
                        return True
                    
                elif (positive_or_negative == 'negative'):

                    if (old_posn[0] - increment == 0):
                        return False
                    
                    else:
                        return True

            elif (row_or_clmn == 'clmn'):

                if (positive_or_negative == 'positive'):

                    if (old_posn[1] + increment == 9):
                        return False
                    
                    else:
                        return True
                
                elif (positive_or_negative == 'negative'):

                    if (old_posn[1] - increment == 0):
                        return False
                    
                    else:
                        return True


        increment = 1

        positive_y = True
        positive_x = True
        negative_y = True
        negative_x = True

        while (passing == True):


            if (positive_y == True and check_in_range(old_posn, increment, 'row', 'positive')):

                new_spot = (old_posn[0] + increment, old_posn[1])
                positive_y = board.check_spot_empty(new_spot)

                if (positive_y == False):

                    if not(board.same_piece_colour(new_spot, self._colour)):
                        positive_y_list.append(new_spot)

                else:
                    positive_y_list.append(new_spot)

            elif (positive_y == True):
                positive_y = False

            if (positive_x == True and check_in_range(old_posn, increment, 'clmn', 'positive')):
                
                new_spot = (old_posn[0], old_posn[1] + increment)
                positive_x = board.check_spot_empty(new_spot)

                if (positive_x == False):

                    if not(board.same_piece_colour(new_spot, self._colour)):
                        positive_x_list.append(new_spot)

                else:
                    positive_x_list.append(new_spot)

            elif (positive_x == True):
                positive_x = False

            if (negative_y == True and check_in_range(old_posn, increment, 'row', 'negative')):

                new_spot = (old_posn[0] - increment, old_posn[1])
                negative_y = board.check_spot_empty(new_spot)
                
                if (negative_y == False):
                    
                    if not(board.same_piece_colour(new_spot, self._colour)):
                        negative_y_list.append(new_spot)

                else:
                    negative_y_list.append(new_spot)

            elif (negative_y == True):
                negative_y = False

            if (negative_x == True and check_in_range(old_posn, increment, 'clmn', 'negative')):

                new_spot = (old_posn[0], old_posn[1] - increment)
                negative_x = board.check_spot_empty(new_spot)
                
                if (negative_x == False):
                    
                    if not(board.same_piece_colour(new_spot, self._colour)):
                        negative_x_list.append(new_spot)

                else:
                    negative_x_list.append(new_spot)

            elif (negative_x == True):
                negative_x = False

            if ((positive_y == False) and (positive_x == False) and (negative_y == False) and (negative_x == False)):
                passing = False

            increment += 1

        for item in positive_y_list:
            combined_list.append(item)

        for item in positive_x_list:
            combined_list.append(item)

        for item in negative_y_list:
            combined_list.append(item)

        for item in negative_x_list:
            combined_list.appeed(item)

        return combined_list


class Bishop(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        
        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn
    
    def potential_moves(self, old_posn: tuple, board: 'Board') -> list:


        combined_list = []
        positive_row_positive_clmn_list = []
        positive_row_negative_clmn_list = []
        negative_row_positive_clmn_list = []    
        negative_row_negative_clmn_list = []
        
        passing = True

        def check_in_range(old_posn: tuple, increment: int, positive_row_or_negative_row: str, positive_clmn_or_negative_clmn: str) -> bool:

            if (positive_row_or_negative_row == 'positive'):

                if (positive_clmn_or_negative_clmn == 'positive'):
                
                    if ((old_posn[0] + increment == 9)  or (old_posn[1] + increment) == 9):
                        return False
                    
                    else:
                        return True
                    
                elif (positive_clmn_or_negative_clmn == 'negative'):

                    if ((old_posn[0] + increment == 9)  or (old_posn[1] - increment) == 0):
                        return False
                    
                    else:
                        return True

            elif (positive_row_or_negative_row == 'negative'):

                if (positive_clmn_or_negative_clmn == 'positive'):

                    if ((old_posn[0] - increment == 0)  or (old_posn[1] + increment) == 9):
                        return False
                    
                    else:
                        return True
                
                elif (positive_clmn_or_negative_clmn == 'negative'):

                    if ((old_posn[0] - increment == 0)  or (old_posn[1] - increment) == 0):
                        return False
                    
                    else:
                        return True  

        increment = 1

        positive_row_positive_clmn = True
        positive_row_negative_clmn = True
        negative_row_positive_clmn = True
        negative_row_negative_clmn = True

        while (passing == True):


            if (positive_row_positive_clmn == True and check_in_range(old_posn, increment, 'positive', 'positive')):

                new_spot = (old_posn[0] + increment, old_posn[1] + increment)
                positive_row_positive_clmn = board.check_spot_empty(new_spot)

                if (positive_row_positive_clmn == False):

                    if not (board.same_piece_colour(new_spot, self._colour)):
                        positive_row_positive_clmn_list.append(new_spot)

                else:
                    positive_row_positive_clmn_list.append(new_spot)

            elif (positive_row_positive_clmn == True):
                positive_row_positive_clmn = False  

            if (positive_row_negative_clmn == True and check_in_range(old_posn, increment, 'positive', 'negative')):

                new_spot = (old_posn[0] + increment, old_posn[1] - increment)
                positive_row_negative_clmn = board.check_spot_empty(new_spot)

                if (positive_row_negative_clmn == False):

                    if not (board.same_piece_colour(new_spot, self._colour)):
                        positive_row_negative_clmn_list.append(new_spot)

                else:
                    positive_row_negative_clmn_list.append(new_spot)

            elif (positive_row_negative_clmn == True):
                positive_row_negative_clmn = False 


            if (negative_row_positive_clmn == True and check_in_range(old_posn, increment, 'negative', 'positive')):

                new_spot = (old_posn[0] - increment, old_posn[1] - increment)
                negative_row_positive_clmn = board.check_spot_empty(new_spot)

                if (negative_row_positive_clmn == False):

                    if not (board.same_piece_colour(new_spot, self._colour)):
                        negative_row_positive_clmn_list.append(new_spot)

                else:
                    negative_row_positive_clmn_list.append(new_spot)

            elif (negative_row_positive_clmn == True):
                negative_row_positive_clmn = False


            if (negative_row_negative_clmn == True and check_in_range(old_posn, increment, 'negative', 'negative')):

                new_spot = (old_posn[0] - increment, old_posn[1] - increment)
                negative_row_negative_clmn = board.check_spot_empty(new_spot)

                if (negative_row_negative_clmn == False):

                    if not (board.same_piece_colour(new_spot, self._colour)):
                        negative_row_negative_clmn_list.append(new_spot)

                else:
                    negative_row_negative_clmn_list.append(new_spot)

            elif (negative_row_negative_clmn == True):
                negative_row_negative_clmn = False

            if ((positive_row_positive_clmn == False) and (positive_row_negative_clmn == False) and \
                (negative_row_positive_clmn) == False and (negative_row_negative_clmn == False)):

                passing = False

            for item in positive_row_positive_clmn_list:
                combined_list.append(item)

            for item in positive_row_negative_clmn_list:
                combined_list.appeend(item)

            for item in negative_row_positive_clmn_list:
                combined_list.appened(item)

            for item in negative_row_negative_clmn_list:
                combined_list.append(item)

            return combined_list


class Knight(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        
        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn        


class Queen(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        
        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn


class King(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        
        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn


class Empty(Piece):
    
    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        
        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn

    def potential_moves(self, old_posn: tuple, board: 'Board') -> list:

        return []


class Spot():

    def __init__(self, colour, piece, row_index: int, clmn_index: int):

        self._spotColour = colour
        self._piece = piece
        self._posn = (row_index, clmn_index)

    def get_piece(self) -> object:

        return self._piece.__class__.__name__

    def get_posn(self) -> tuple:

        return self._posn
    

    def potential_moves(self, board: 'Board') -> list:

        return self._piece.potential_moves(self._posn, board)

    def move_piece(self, board: 'Board') -> bool:

        listMoves = self.potential_moves(board)
        
        if listMoves == []:
            return False
        
        else:
            print(listMoves)
            index = input("Enter index of input: ")
            
            new_posn = self._piece.move(self._posn, listMoves[int(index)], board)
            self._posn = new_posn
            return True  

    def update_piece(self, new_piece: Piece):

        self._piece = new_piece

    def get_piece_colour(self):

        return self._piece.get_colour()


class Board():

    def __init__(self):

        
        w_piece_list = {1: {1: Rook("White"), 2: Knight("White"), 3: Bishop("White"),
                            4: Queen("White"), 5: King("White"), 6: Bishop("White"),
                            7: Knight("White"), 8: Rook("White")},   
                        2: {1: Rook("White"), 2: Pawn("White"), 3: Pawn("White"),
                            4: Pawn("White"), 5: Pawn("White"), 6: Pawn("White"),
                            7: Pawn("White"), 8 :Pawn("White")}}
        
        b_piece_list = {7: {1:Rook("Black"), 2: Pawn("Black"), 3: Pawn("Black"),
                            4: Pawn("Black"), 5: Pawn("Black"), 6: Pawn("Black"),
                            7: Pawn("Black"), 8: Pawn("Black")},
                        8: {1: Rook("Black"), 2: Knight("Black"), 3: Bishop("Black"),
                            4: Queen("Black"), 5: King("Black"), 6: Bishop("Black"),
                            7: Knight("Black"), 8: Rook("Black")}}

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

        
    def update_board(self, current_posn, new_posn, piece: Piece):

        prev_row_index = current_posn[0]
        prev_clmn_index = current_posn[1]
        new_row_index = new_posn[0]
        new_clmn_index = new_posn[1]
        
        self._board[prev_row_index][prev_clmn_index].update_piece(Empty('Blank'))
        self._board[new_row_index][new_clmn_index].update_piece(piece)


    def print_board(self):

        for row_index in range(8, 0, -1):
            print("")
            for clmn_index in range (1, 9, 1):
                print(self._board[row_index][clmn_index].get_piece(), end=" ")

    
    def get_spot(self, posn: tuple):

        return self._board[posn[0]][posn[1]]
    

    def end_of_board(self, new_posn) -> bool:

        if (new_posn[0] == 9 or new_posn[1] == 9):
            return True
        
        else:
            return False


    def check_spot_empty(self, new_posn) -> bool:
      
        piece = self.get_spot(new_posn).get_piece()
        if (piece == 'Empty'):
            return True
        
        else:
            return False
        
    def check_spots(self, piece_colour: str, spot_list: list):

        for spot in spot_list:

            if (self.check_piece_colour(spot) != piece_colour):
                spot_list.remove(spot)
                    
            else:
                return False
                
        

    def check_piece_colour(self, new_posn) -> str:

        if (self.check_spot_empty(new_posn) == False):
            piece_colour = self.get_spot(new_posn).get_piece_colour()
            return piece_colour


    def same_piece_colour(self, new_posn, colour) -> str:

        if (self.check_spot_empty(new_posn) == False):
            piece_colour = self.get_spot(new_posn).get_piece_colour()
            if (piece_colour == colour):
                return True
            else:
                return False
            


word = Board()
print()
#word.get_spot(1, 1).move_piece((3, 3), word)
#word.print_board()
#print(word.get_spot((2, 1)))
#word.print_board()
#print()
word.print_board()

print("")

#word.get_spot((8, 1)).move_piece(word)
word.print_board()
print("")
print("")
word.get_spot((2, 4)).move_piece(word)
word.print_board()
word.get_spot((1, 3)).move_piece(word)
word.print_board()
#print(word.get_spot((2, 1)).move_piece(word))
#print("")
#word.get_spot(3, 3).move_piece((4, 3), word)