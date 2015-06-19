__author__ = 'tracyrohlin'

import re

class Minesweeper:
    def __init__(self, array):
        self.array = array
        self.board = array[1:-1]
        self.top_border = array[0]
        self.bottom_border = array[-1]
        self.test_row = array[1]
        self.locations = {}

    def find_mines(self):
        row_number = 0
        for row in self.board:
            if "*" in row:
                positions = [i for i, ltr in enumerate(row) if ltr == "*"]
                self.locations[row_number] = positions
            row_number +=1
        return self.locations

    def replace_char(self, char):
        if char == " ":
            return "1"
        elif re.match("\d", char):
            return str(int(char)+1)
        else:
            return char

    def horizontal_check(self):
        for row in self.locations.keys():
            for mine in self.locations[row]:
                try:
                    position_before = mine-1
                    self.board[row] = "{0}{1}{2}".format(self.board[row][:position_before], self.replace_char(self.board[row][position_before]), self.board[row][position_before+1:])
                    position_after = mine +1
                    self.board[row] = "{0}{1}{2}".format(self.board[row][:position_after], self.replace_char(self.board[row][position_after]), self.board[row][position_after+1:])
                except Exception as e:
                    print e

    def vertical_check(self):
        for row in self.locations.keys():
            row_before = row -1
            row_after = row +1
            for mine in self.locations[row]:
                try:
                    self.board[row_after] = "{0}{1}{2}".format(self.board[row_after][:mine], self.replace_char(self.board[row_after][mine]), self.board[row_after][mine+1:])
                except Exception as e:
                    print e
                if row !=0:
                    self.board[row_before] = "{0}{1}{2}".format(self.board[row_before][:mine], self.replace_char(self.board[row_before][mine]), self.board[row_before][mine+1:])



    def diagonal_check(self):
        for row in self.locations.keys():
            try:
                row_before = row - 1
                row_after = row + 1
                for mine in self.locations[row]:
                    position_before = mine-1
                    position_after = mine+1
                    if row_after < len(self.board): #makes sure that it doesn't try to check the row after the last row, otherwise it will through an exception
                        self.board[row_after] = "{0}{1}{2}".format(self.board[row_after][:position_before], self.replace_char(self.board[row_after][position_before]), self.board[row_after][position_before+1:])
                        self.board[row_after] = "{0}{1}{2}".format(self.board[row_after][:position_after], self.replace_char(self.board[row_after][position_after]), self.board[row_after][position_after+1:])

                    if row != 0: #makes sure that it doesn't try to check the row before zero, otherwise it will throw an exception
                        self.board[row_before] = "{0}{1}{2}".format(self.board[row_before][:position_before], self.replace_char(self.board[row_before][position_before]), self.board[row_before][position_before+1:])
                        self.board[row_before] = "{0}{1}{2}".format(self.board[row_before][:position_after], self.replace_char(self.board[row_before][position_after]), self.board[row_before][position_after+1:])
            except Exception as e:
                print e

    def print_board(self):
        surface = [self.top_border]
        for row in self.board:
            surface.append(row)
        surface.append(self.bottom_border)

        return surface



def board(array):
    m = max(len(x) for x in array[1:-1])
    surface = array[1:-1]
    borders = []
    borders.append(array[0])
    borders.append(array[-1])

    for border in borders: #checks to make sure that borders are correct
        if not re.match("\+\-+\+", border):
            raise ValueError("The border is incorrect.")

    for row in surface:
        if len(row) != m:
            raise ValueError("One of the rows is the incorrect size.")
        elif not re.match("\|[\s\*]+\|", row):
            raise ValueError("The board has an incorrect element in it.")
        else:
            pass

    boardgame = Minesweeper(array)
    boardgame.find_mines()
    boardgame.diagonal_check()
    boardgame.horizontal_check()
    boardgame.vertical_check()

    result =[]
    for row in boardgame.print_board():
        result.append(row)
    return result
