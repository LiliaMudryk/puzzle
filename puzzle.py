"""
This module checks if board is correct and ready for game.
"""
def check_rows(board):
    """
    Returns False if there are two identical numbers in row and True otherwise
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    True
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     5 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    False
    """
    uniqueness = True
    for i,row in enumerate(board):
        if i not in (0, len(board) - 1):
            for j,number in enumerate(row):
                if j > row.index(number) and number not in("*", " "):
                    uniqueness = False
                    break

    return uniqueness

def empty_columns(board):
    """Returns list of "" with length equal to length of expected column.
    >>> empty_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    ['', '', '', '', '', '', '', '', '']
    """
    columns = []
    while len(columns)!= len(board[0]):
        columns.append("")
    return columns


def fill_columns(columns,board):
    """Returns list of columns of the board.
    >>> fill_columns(['', '', '', '', '', '', '', '', ''],\
["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82', '*1       ',\
 '  31 82  ', '****93 2*', '****   **', '****5 ***', '**** ****']
    """
    for i in range(len(columns)):
        for row in board:
            columns[i]+=row[i]
    return columns


def check_columns(board):
    """
    Returns False if there are two identical numbers in row and True otherwise
    >>> check_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    True
    >>> check_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     5 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    True
    """
    columns_empt = empty_columns(board)
    columns = fill_columns(columns_empt,board)
    uniqueness = check_rows(columns)
    return uniqueness

def check_color(board):
    """
    Returns False if there are two identical numbers in one color and True otherwise.
    >>> check_color(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    True
    >>> check_color(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_color(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     5 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    False
    """
    columns_empt = empty_columns(board)
    columns = fill_columns(columns_empt,board)
    colors = []
    for i in range(len(columns)):
        color = columns[i][:-(i+1)] + board[-(i+1)][i:]
        colors.append(color)
    uniqueness = check_rows(colors)
    return uniqueness


def validate_board(board):
    """
    Returns True if board is correct and ready for game and False otherwise.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     5 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"])
    False
    """
    rows_uniqueness = check_rows(board)
    columns_uniqueness = check_columns(board)
    colors_uniqueness = check_color(board)
    return rows_uniqueness and colors_uniqueness and columns_uniqueness
