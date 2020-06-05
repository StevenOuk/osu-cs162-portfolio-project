# Author: Steven Ouk
# Date: 06/05/2020
# Description: Write a class named GessGame for playing an abstract board game called Gess.


class GessGame:
    """
    Description: Represents an abstract board game called Gess.
    Responsibilities:
    1a) Keep track of the current game state.
    1b) This is done by keeping track of the number of rings of both players.
    Exception: If a player decides to resign, the other player will be the winner, which will override the
    current game state.
    2) Allows the current player to resign. No communication with other classes necessary.
    3) Allows the current player to make a move from one spot of the board to another.
    4) Initialize the initial board state using a list of lists with "B" to represent a black stone and
    "W" to represent a white stone. Include a display method to print the current board state in an
    organized manner to allow for testing and debugging.
    We will probably not need to communicate with other classes.
    """
    def __init__(self):
        """
        Sets the initial game state to "UNFINISHED".
        Sets the current player to "BLACK" as Black is the first player to move.
        Sets the initial board state to the given state in the GessGame Description.
        I plan on keeping track of the number of rings separately in the Ring class, so I currently don't have
        the rings set as a data member, but subject to change if need be.
        """
        self._game_state = "UNFINISHED"
        self._player = "BLACK"
        self._board = [["|-|"]*20 for n in range(20)]       # Sets up a 20x20 empty board.
        # Sets up the initial board state with player O representing white.
        self._board[1][2] = self._board[1][4] = self._board[1][6] = self._board[1][7] = self._board[1][8] = \
            self._board[1][9] = self._board[1][10] = self._board[1][11] = self._board[1][12] = self._board[1][13] = \
            self._board[1][15] = self._board[1][17] = self._board[2][1] = self._board[2][2] = self._board[2][3] = \
            self._board[2][5] = self._board[2][7] = self._board[2][8] = self._board[2][9] = self._board[2][10] = \
            self._board[2][12] = self._board[2][14] = self._board[2][16] = self._board[2][17] = self._board[2][18] = \
            self._board[3][2] = self._board[3][4] = self._board[3][6] = self._board[3][7] = self._board[3][8] = \
            self._board[3][9] = self._board[3][10] = self._board[3][11] = self._board[3][12] = self._board[3][13] = \
            self._board[3][15] = self._board[3][17] = self._board[6][2] = self._board[6][5] = self._board[6][8] = \
            self._board[6][11] = self._board[6][14] = self._board[6][17] = "|O|"

        # Sets up the initial board state with player X representing black.
        self._board[13][2] = self._board[13][5] = self._board[13][8] = self._board[13][11] = self._board[13][14] = \
            self._board[13][17] = self._board[16][2] = self._board[16][4] = self._board[16][6] = self._board[16][7] = \
            self._board[16][8] = self._board[16][9] = self._board[16][10] = self._board[16][11] = \
            self._board[16][12] = self._board[16][13] = self._board[16][15] = self._board[16][17] = \
            self._board[17][1] = self._board[17][2] = self._board[17][3] = self._board[17][5] = self._board[17][7] = \
            self._board[17][8] = self._board[17][9] = self._board[17][10] = self._board[17][12] = \
            self._board[17][14]= self._board[17][16] = self._board[17][17] = self._board[17][18] = \
            self._board[18][2] = self._board[18][4] = self._board[18][6] = self._board[18][7] = self._board[18][8] = \
            self._board[18][9] = self._board[18][10] = self._board[18][11] = self._board[18][12] = \
            self._board[18][13] = self._board[18][15] = self._board[18][17] = "|X|"

    def get_game_state(self):
        """
        Returns the current game state.
        :param: None
        :return: self._game_state
        """
        return self._game_state

    def get_player(self):
        """
        Returns the current player.
        :param: None
        :return: self._player
        """
        return self._player

    def get_board(self):
        """
        Returns the current board state.
        :return: self._board
        """
        return self._board

    def display_board(self):
        """
        Will display the current board state. Useful for testing and debugging code.
        :param: None
        :return: Prints the current board state.
        """
        for row in self._board:
            print(*row)

    def resign_game(self):
        """
        Allows the current player to concede the game by:
        Determines who the current player is, then change the game state so that the other player has won.
        :param: None
        :return: None
        """
        if self._game_state == "UNFINISHED":
            if self._player == "BLACK":
                self._game_state = "WHITE_WON"
            elif self._player == "WHITE":
                self._game_state = "BLACK_WON"
            else:
                return False

    def make_move(self, first, second):
        """
        Represents a move from the "first" parameter to the "second" parameter.
        The two parameters are strings that represent the center square of the piece being moved and the desired
        new location of the center square.
        :param first: The center square of the piece being moved, such as "b6".
        :param second: The center square of the new location piece, such as "e9".
        :return: Returns False if the move is not legal or if the game is already won.
        Otherwise, make the indicated move, remove any captured stones, update the game state if necessary,
        then return True
        """
        # Convert the input strings to squares on self._board, i.e. [row, column].
        center1 = self.convert_string(first)
        center2 = self.convert_string(second)

        # Makes sure the inputs are different locations.
        if first == second:
            print("Same spot!")
            return False

        # Make sure inputs are in boundaries.
        if self.check_boundaries(center1) is False:
            print("First center invalid")
            return False
        if self.check_boundaries(center2) is False:
            print("Second center invalid")
            return False

        # Piece to be moved.
        piece = self.return_piece(center1)

        # Is piece superpiece?
        if "super" in self.check_movement(piece):
            print("super")
            super = True
        if "super" not in self.check_movement(piece):
            print("not super")
            super = False

        # Check to make sure the game is not already over.
        if self.get_game_state() != "UNFINISHED":
            print("Game is already over!")
            return False

        # Checks if the first parameter is a valid piece by the player.
        if self.get_player() == "BLACK":
            if self.is_black_piece(center1) is False:
                print("Cannot move piece as black player")
                return False
        if self.get_player() == "WHITE":
            if self.is_white_piece(center1) is False:
                print("Cannot move piece as white player")
                return False

        # Check direction and number of spaces.
        if self.calculates_direction(center1, center2) is False:
            return False

        # Check available movement of the moving piece.
        if self.calculates_direction(center1, center2) not in self.check_movement(piece):
            print("that piece cannot move in that direction")
            return False

        # Remove first piece.
        self.remove_piece(center1)

        # Check if path is clear.
        if self.is_path_clear(center1, center2, super) is False:
            self.add_piece(piece, center1)      # Adds back the removed piece if False.
            print("Path is not clear")
            return False

        # Replace second location with first piece footprint.
        self.add_piece(piece, center2)

        # Remove stones on the outside rows and columns.
        self._board[0] = self._board[19] = ["|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|",
                                            "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|", "|-|"]
        for row in self._board:
            row[0] = row[19] = "|-|"

        # Check rings.
        if self.check_black_rings() is False:   # If no more black rings
            self._game_state = "WHITE_WON"
        if self.check_white_rings() is False:   # If no more white rings
            self._game_state = "BLACK_WON"
        # Change players.
        if self.get_game_state() == "UNFINISHED":
            if self.get_player() == "BLACK":
                self._player = "WHITE"
            elif self.get_player() == "WHITE":
                self._player = "BLACK"
        return True

    def convert_string(self, string):
        """
        Converts a specific square on the Gess Board game, which is an input, to the square on self._board.
        :param string: A square that is being inputted by the user, such as "o18".
        :return: Returns the square on self._board that the input represents, for example "|O|"
        """
        # Use Dictionaries to convert the given row or column to self._board.
        convert_columns = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
            "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19
        }
        convert_rows = {
            '20': 0, '19': 1, '18': 2, '17': 3, '16': 4, '15': 5, '14': 6, '13': 7, '12': 8, '11': 9, '10': 10, '9': 11,
            '8': 12, '7': 13, '6': 14, '5': 15, '4': 16, '3': 17, '2': 18, '1': 19
        }
        chars = []
        for char in string:
            chars.append(char)
        if len(chars) == 2:
            row = convert_rows[chars[1]]
            column = convert_columns[chars[0]]
        if len(chars) == 3:
            row = convert_rows[chars[1] + chars[2]]
            column = convert_columns[chars[0]]
        return [row, column]

    def check_boundaries(self, center):
        """
        Makes sure the center is in the specified boundaries.
        :param center: The center of a piece, given as [row, column]
        :return: Returns True if in boundaries, else returns False.
        """
        if center[0] < 1 or center[0] > 18 or center[1] < 1 or center[1] > 18:
            return False
        return True

    def return_piece(self, center):
        """
        After converting a string to a location on self._board, use this to convert that location to a 3x3 piece.
        :param center: A list [row, column] taken from method: convert_string
        :return: Returns the 3x3 piece with the location being the center square.
        """
        # Center of this piece would be self._board[center[0]][center[1]]
        row = center[0]
        col = center[1]
        piece = [[self._board[row-1][col-1], self._board[row-1][col], self._board[row-1][col+1]],
                 [self._board[row][col-1], self._board[row][col], self._board[row][col+1]],
                 [self._board[row+1][col-1], self._board[row+1][col], self._board[row+1][col+1]]]
        return piece

    def print_piece(self, string):
        """
        Will print an easy to see display of the 3x3 piece of a given center. Mainly used for testing purposes.
        :param string: Takes an input string, such as 'o18'.
        :return: None.
        """
        center = self.convert_string(string)
        piece = self.return_piece(center)
        for row in piece:
            print(*row)

    def is_black_piece(self, center):
        """
        If player is black, use this method to make sure the piece is black territory.
        :param center: Given as a list of [row, column]
        :return: Returns True if piece is playable by black, else return False.
        """
        piece = self.return_piece(center)
        for row in piece:
            for sq in row:
                if sq == "|O|":     # Check for any white pieces in footprint.
                    return False
        # If piece is empty.
        if piece == [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
            return False
        # If the surrounding squares are empty (which means the player can't move).
        if piece == [["|-|", "|-|", "|-|"], ["|-|", "|X|", "|-|"], ["|-|", "|-|", "|-|"]]:
            return False
        return True

    def is_white_piece(self, center):
        """
        If player is white, use this method to make sure the piece is white territory.
        :param center: Given as a list of [row, column]
        :return: Returns True if piece is playable by white, else return False.
        """
        piece = self.return_piece(center)
        for row in piece:
            for sq in row:
                if sq == "|X|":     # Check for any white pieces in footprint.
                    return False
        # If piece is empty.
        if piece == [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
            return False
        # If the surrounding squares are empty (which means the player can't move).
        if piece == [["|-|", "|-|", "|-|"], ["|-|", "|O|", "|-|"], ["|-|", "|-|", "|-|"]]:
            return False
        return True

    def remove_piece(self, center):
        """
        Removes all stones in the 3x3 footprint of a given center.
        :param center: Center square: Given as [row, column].
        :return: No Return Value.
        """
        row = center[0]
        col = center[1]
        self._board[row-1][col-1] = self._board[row-1][col] = self._board[row-1][col+1] = \
            self._board[row][col-1] = self._board[row][col] = self._board[row][col+1] = \
            self._board[row+1][col-1] = self._board[row+1][col] = self._board[row+1][col+1] = "|-|"

    def add_piece(self, piece, center):
        """
        Takes a 3x3 footprint of a piece and adds that footprint to a given center location.
        :param piece: 3x3 piece, given as a list of lists.
        :param center: Center of piece: Given as [row, column]
        :return: No Return Value.
        """
        row = center[0]
        col = center[1]
        self._board[row - 1][col - 1] = piece[0][0]
        self._board[row - 1][col] = piece[0][1]
        self._board[row - 1][col + 1] = piece[0][2]
        self._board[row][col - 1] = piece[1][0]
        self._board[row][col] = piece[1][1]
        self._board[row][col + 1] = piece[1][2]
        self._board[row + 1][col - 1] = piece[2][0]
        self._board[row + 1][col] = piece[2][1]
        self._board[row + 1][col + 1] = piece[2][2]

    def check_movement(self, piece):
        """
        Checks the movement availability of a given piece.
        :param piece: A 3x3 footprint of a piece.
        :return: Returns a list of movable directions by the piece
        """
        movements = []
        if piece[0][0] != "|-|":    # If not empty
            movements.append("NW")
        if piece[0][1] != "|-|":
            movements.append("N")
        if piece[0][2] != "|-|":
            movements.append("NE")
        if piece[1][0] != "|-|":
            movements.append("W")
        if piece[1][2] != "|-|":
            movements.append("E")
        if piece[2][0] != "|-|":
            movements.append("SW")
        if piece[2][1] != "|-|":
            movements.append("S")
        if piece[2][2] != "|-|":
            movements.append("SE")
        if piece[1][1] != "|-|":
            movements.append("super")
        return movements

    def calculates_direction(self, center1, center2):
        """
        Takes a couple locations on the board and returns the direction from center1 to center2 as a string.
        :param center1: First location on board, given as [row, column]
        :param center2: Second location on board, given as [row, column]
        :return: Returns False if not straight line, else Return the direction as a string.
        """
        # If row is the same, move horizontal.
        if center1[0] == center2[0]:
            # If center2 column is greater than center1 column, piece goes east.
            if center2[1] > center1[1]:
                return "E"
            else:   # Else, piece goes west.
                return "W"

        # If column is the same, move vertical.
        if center1[1] == center2[1]:
            # If center2 row is greater than center1 row, piece goes south.
            if center2[0] > center1[0]:
                return "S"
            else:   # Else, piece goes north.
                return "N"

        # If distance between rows and columns, are the same, move diagonal.
        if center2[0] - center1[0] == center2[1] - center1[1]:
            # If center2 is greater than center1, piece goes southeast.
            if center2[0] - center1[0] > 0:
                return "SE"
            else:   # Else, piece goes northwest.
                return "NW"
        if center2[0] - center1[0] == -(center2[1] - center1[1]):
            # If center2 row is greater than center1 row, piece goes southwest.
            if center2[0] - center1[0] > 0:
                return "SW"
            else:   # Else, piece goes northeast.
                return "NE"
        return False

    def is_path_clear(self, center1, center2, super):
        """
        Checks every space between the locations to make sure every 3x3 footprint is empty.
        :param center1: First location on board, given as [row, column]
        :param center2: Second location on board, given as [row, column]
        :param super: Helps determine if the moving piece can move over 3 spaces.
        :return: Returns True if path is clear. Else, Returns False.
        """
        if self.calculates_direction(center1, center2) == "N":
            spaces = center1[0] - center2[0]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([(center1[0] - x), center1[1]]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        if self.calculates_direction(center1, center2) == "S":
            spaces = center2[0] - center1[0]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([(center1[0] + x), center1[1]]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        if self.calculates_direction(center1, center2) == "W":
            spaces = center1[1] - center2[1]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([(center1[0]), center1[1] - x]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    print("you cannot go west")
                    return False
        if self.calculates_direction(center1, center2) == "E":
            spaces = center2[1] - center1[1]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([center1[0], center1[1] + x]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        if self.calculates_direction(center1, center2) == "SE":
            spaces = center2[0] - center1[0]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([center1[0] + x, center1[1] + x]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        if self.calculates_direction(center1, center2) == "NW":
            spaces = center1[0] - center2[0]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([center1[0] - x, center1[1] - x]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        if self.calculates_direction(center1, center2) == "NE":
            spaces = center1[0] - center2[0]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([center1[0] - x, center1[1] + x]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        if self.calculates_direction(center1, center2) == "SW":
            spaces = center2[0] - center1[0]
            if super is False:
                if spaces > 3:
                    return False
            for x in range(1, spaces):
                if self.return_piece([center1[0] + x, center1[1] - x]) != \
                        [["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"], ["|-|", "|-|", "|-|"]]:
                    return False
        return True

    def check_black_rings(self):
        """
        Scans the Gess board for any rings held by the black player.
        Should not need any parameters.
        :return: Returns True if a black ring is found, returns False if no black ring is found.
        """
        black_rings = 0
        for x in range(1, 19):
            for y in range(1, 19):
                piece = self.return_piece([x, y])
                if piece == [["|X|", "|X|", "|X|"], ["|X|", "|-|", "|X|"], ["|X|", "|X|", "|X|"]]:
                    black_rings += 1
        if black_rings > 0:
            return True
        return False

    def check_white_rings(self):
        """
        Scans the Gess board for any rings held by the black player.
        Should not need any parameters.
        :return: Returns True if a white ring is found, returns False if no white ring is found.
        """
        white_rings = 0
        for x in range(1,19):
            for y in range(1,19):
                piece = self.return_piece([x,y])
                if piece == [["|O|", "|O|", "|O|"], ["|O|", "|-|", "|O|"], ["|O|", "|O|", "|O|"]]:
                    white_rings += 1
        if white_rings > 0:
            return True
        return False


# game = GessGame()
# game.remove_piece(game.convert_string('i7'))
# game.make_move('i3', 'i13')
# game.display_board()
# game.make_move('i18', 'i15')
# game.display_board()
# print(game.get_game_state())

