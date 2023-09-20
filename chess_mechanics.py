class Piece():

    def __init__(self, colour: str):
        #Sets up initial values for a piece

        self._colour = colour


    def get_colour(self) -> str:

        return self._colour


    def move(self, old_posn: tuple, new_posn: tuple, board: 'Board') -> tuple:

        board.update_board(old_posn, new_posn, self)
        old_posn = new_posn
        return old_posn

    """@abstractmethod
    def potential_moves(self):
        #Moves piece based on what it is able to do
        pass"""


class Pawn(Piece):


    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)
        self._moveList = []

    def get_colour(self) -> str:

        return self._colour

    def potential_moves(self, old_posn: tuple) -> list:

        if (self._colour == "White"):
            self._moveList.append((old_posn[0] + 1, old_posn[1]))

        else:
            self._moveList.append((old_posn[0] + -1, old_posn[1]))

        #Put list in a list to work with check_spots function in board class
        return [self._moveList]


class Rook(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)
    
    def potential_moves(self, old_posn: tuple) -> list:

        
        potential_move_list = []
        increment_list = [1, -1]
        y, x = old_posn[0], old_posn[1]
        axis_point_list = [x, y]


        for axis in axis_point_list:
            initial_axis = axis 

            for increment in increment_list:
                sublist = []
                axis += increment

                while (axis < 9 and axis > 0):

                    if initial_axis == x:
                        sublist.append((y, axis))

                    elif initial_axis == y:
                        sublist.append((axis, x))

                    axis += increment

                potential_move_list.append(sublist)
                axis = initial_axis

        return potential_move_list        
                            

class Bishop(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def potential_moves(self, old_posn) -> list:

        increment_list = [1, -1]
        y, x = old_posn[0], old_posn[1]
        potential_move_list = []

        for increment_y in increment_list:
            for increment_x in increment_list:

                sublist = []
                new_spot = (y + increment_y, x + increment_x)

                while (new_spot[0] < 9 and new_spot[0] > 0 and
                       new_spot[1] < 9 and new_spot[1] > 0):
                    
                    sublist.append(new_spot)
                    new_spot = (new_spot[0] + increment_y, \
                                new_spot[1] + increment_x)
            
                potential_move_list.append(sublist)

        return potential_move_list


class Knight(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour) 
    
        
    def potential_moves(self, old_posn: tuple) -> list:

        long_increment_list = [2, -2]
        short_increment_list = [1, -1]
        increment_cycle_list = [long_increment_list, short_increment_list]
        list_index = 1
        potential_move_list = []

        for index in range(2): 

            #increment_y is long_increment_list in first loop, then short_increment_list in second loop
            for increment_y in increment_cycle_list[index - 1]:

                for increment_x in increment_cycle_list[index]:

                    sublist = []
                    new_spot = (old_posn[0] + increment_y, old_posn[1] + increment_x)
                    if (new_spot[0] < 9 and new_spot[0] > 0 and new_spot[1] < 9 and new_spot[1] > 0):
                        sublist.append(new_spot)

                    potential_move_list.append(sublist)

        return potential_move_list


class Queen(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def potential_moves(self, old_spot: tuple):


        potential_move_list = []
        increment_list = [1, -1]
        y, x = old_spot[0], old_spot[1]
        axis_point_list = [x, y]


        for axis in axis_point_list:
            initial_axis = axis 

            for increment in increment_list:
                sublist = []
                axis += increment

                while (axis < 9 and axis > 0):

                    if initial_axis == x:
                        sublist.append((y, axis))

                    elif initial_axis == y:
                        sublist.append((axis, x))

                    axis += increment

                potential_move_list.append(sublist)
                axis = initial_axis

        y, x = old_spot[0], old_spot[1]

        for increment_y in increment_list:
            for increment_x in increment_list:

                sublist = []
                new_spot = (y + increment_y, x + increment_x)

                while (new_spot[0] < 9 and new_spot[0] > 0 and
                       new_spot[1] < 9 and new_spot[1] > 0):
                    
                    sublist.append(new_spot)
                    new_spot = (new_spot[0] + increment_y, \
                                new_spot[1] + increment_x)
            
                potential_move_list.append(sublist)

        return potential_move_list


class King(Piece):

    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def potential_moves(self, old_spot: tuple) -> list: 

        potential_moves_list = []
        iterator_list = [0, 1, -1]

        for i in range(3):
            for j in range(3):

                new_spot = (old_spot[0] + iterator_list[i], old_spot[1] + iterator_list[j])

                if (new_spot != old_spot and new_spot[0] != 9 and \
                    new_spot[1] != 9 and new_spot[0] != 0 and new_spot[1] != 0):

                    sublist = []
                    sublist.append(new_spot)
                    potential_moves_list.append(sublist)

        return potential_moves_list


class Empty(Piece):
    
    def __init__(self, colour: str):
        #Initializes pawn class using Piece constructor

        super().__init__(colour)

    def potential_moves(self, old_posn: tuple) -> list:

        return []


class Spot():

    def __init__(self, colour, piece, row_index: int, clmn_index: int):

        self._spotColour = colour
        self._piece = piece
        self._posn = (row_index, clmn_index)

    def get_spot_colour(self) -> str:

        return self._spotColour

    def get_piece_name(self) -> object:

        return self._piece.__class__.__name__

    def get_posn(self) -> tuple:

        return self._posn

    def potential_moves(self, board: 'Board') -> list:

        return self._piece.potential_moves(self._posn)

    def move_piece(self, board: 'Board') -> bool:

        potential_moves = self.potential_moves(board)
        colour = self.get_piece_colour()
        move_list = board.check_spots(colour, potential_moves)
        
        if move_list == []:
            return False
        
        else:
            print(move_list)
            index = input("Enter index of input: ")
            
            
            old_spot = self._piece.move(self._posn, move_list[int(index)], board)
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
                        2: {1: Pawn("White"), 2: Pawn("White"), 3: Pawn("White"),
                            4: Pawn("White"), 5: Pawn("White"), 6: Pawn("White"),
                            7: Pawn("White"), 8 :Pawn("White")}}
        
        b_piece_list = {7: {1: Pawn("Black"), 2: Pawn("Black"), 3: Pawn("Black"),
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

    def get_board(self):

        return self._board

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
            for clmn_index in range(1, 9, 1):
                print("%10s" %self._board[row_index][clmn_index].get_piece_name(), end=" ")

        print("")

    def get_spot(self, posn: tuple):

        return self._board[posn[0]][posn[1]]

    def check_spot_empty(self, new_posn) -> bool:
      
        piece = self.get_spot(new_posn).get_piece_name()
        if (piece == 'Empty'):
            return True
        
        else:
            return False

    def check_spots(self, piece_colour: str, spot_list: list):

        #Check if list has anything in it, if not return
        #Check if spot is empty
        # -> Pass if it is, continue iterating
        #If Not
        # -> Check if spot has piece with same colour
        # -> -> Pass if it is, stop iterating through list
        # -> -> if it is not stop iterating through list and dont add piece 

        available_moves = []


        for list in spot_list:

            if len(list) == 0:
                pass
                
            else:

                list_end = False
                list_index = 0
                list_len = len(list)
                
                while (list_end == False):
                    current_spot = list[list_index]

                    #Case 1: spot is empty, continue iterating
                    if self.check_spot_empty(current_spot) == True:
                        available_moves.append(current_spot)

                    #Case 2: spot is taken by piece of same colour, stop iterating, don't add to list
                    elif self.check_piece_colour(current_spot) == piece_colour:
                        list_end = True

                    #Case 3: Spot is taken by piece of different colour, add to list, stop iterating
                    else:
                        available_moves.append(current_spot)
                        list_end = True

                    list_index += 1

                    #Check if end of list
                    if list_len == list_index:
                        list_end = True

        return available_moves

    def check_piece_colour(self, new_posn) -> str:

        if (self.check_spot_empty(new_posn) == False):
            piece_colour = self.get_spot(new_posn).get_piece_colour()
            return piece_colour


word = Board()

board = word.get_board()

#print(type(board[1]))

'''
#Knight test
word.get_spot((1, 2)).move_piece(word)
word.print_board()
word.get_spot((3, 3)).move_piece(word)
word.print_board()
'''

'''
#Bishop test
word.get_spot((2, 4)).move_piece(word)
word.print_board()
word.get_spot((1, 3)).move_piece(word)
word.print_board()
word.get_spot((2, 4)).move_piece(word)
word.print_board()
'''

'''
#Black Pawn and rook test
word.get_spot((7, 1)).move_piece(word)
word.print_board()
word.get_spot((8, 1)).move_piece(word)
word.print_board()
print("")
print(word.get_spot((7, 1)).get_piece())
word.get_spot((7, 1)).move_piece(word)
word.print_board()
'''

'''
#Queen Test
word.get_spot((2, 4)).move_piece(word)
word.print_board()
word.get_spot((1, 4)).move_piece(word)
word.print_board()
word.get_spot((2, 4)).move_piece(word)
word.print_board()
word.get_spot((4, 6)).move_piece(word)
'''

'''
#King Test
word.get_spot((2, 5)).move_piece(word)
word.print_board()
word.get_spot((1, 5)).move_piece(word)
word.print_board()
word.get_spot((2, 5)).move_piece(word)
word.print_board()
'''