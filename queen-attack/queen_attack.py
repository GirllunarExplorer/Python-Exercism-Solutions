__author__ = 'tracyrohlin'

def test_board(arg1, arg2):
    test = [arg1[0], arg1[1], arg2[0], arg2[1]]
    if arg1 == arg2:
        raise ValueError("You cannot place two queens on the same space")
    for i in test:
        if i < 0 or i > 7:
            raise ValueError("The position you have given is off the board.")


def board(tuple1, tuple2):
    test_board(tuple1, tuple2)

    white_row, white_column = tuple1
    black_row, black_column = tuple2


    new_board = []
    while len(new_board)<8:
        new_board.append("_"*8)
    first_repl = list(new_board[white_row])
    first_repl[white_column] = "W"
    new_board[white_row] = "".join(first_repl)

    second_repl = list(new_board[black_row])
    second_repl[black_column] = "B"
    new_board[black_row] = "".join(second_repl)

    for row in new_board:
        print row
    return new_board

def can_attack(tuple1, tuple2):
    test_board(tuple1, tuple2)

    white_row, white_column = tuple1
    black_row, black_column = tuple2
    row_difference = black_row- white_row
    column_difference = black_column - white_column
    if white_row == black_row:
        return True
    elif white_column == black_column:
        return True
    elif abs(row_difference) == abs(column_difference):
        return True
    else: return False

can_attack((2, 3), (5, 6))