"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    board_new = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                board_new.add((i, j))
    return board_new


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] is not EMPTY:
        raise ValueError("Cell is occupied")

    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[i][j] = current_player

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if_winner = winner(board)
    if if_winner != None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_ = winner(board)

    if X == winner_:
        return 1
    elif O == winner_:
        return - 1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

def minimax_value(board):
    if terminal(board):
        return utility(board)

    current_player = player(board)

    if current_player == X:
        best_value = float('-inf')
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            best_value = min(best_value, value)
        return best_value

