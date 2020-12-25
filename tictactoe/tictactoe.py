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
    if board == [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]:
        return X
    
    X_count = 0
    O_count = 0

    for i in range(3):
        for j in range(3):
            currentVar = board[i][j]
            if currentVar == X:
                X_count += 1
            if currentVar == O:
                O_count += 1

    if terminal(board) == False:
        if X_count > O_count:
            return O
        else:
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) == True:
        return EMPTY
    possible_actions = [[0, 0], [0, 0], [0, 0], 
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    current_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions[current_count][0] = i
                possible_actions[current_count][1] = j   
                current_count+=1

    return possible_actions 

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action
    act = [i,j]
    if terminal(board):
        raise ValueError("Game over.")
    elif act not in actions(board):
        raise ValueError("Invalid action.")
    else:
        p = player(board)
        result_board = copy.deepcopy(board)
        (i, j) = action
        result_board[i][j] = p

    return result_board

def winner(board):
    """
    Returns the winner of the game EMPTY if there isn't any
    """
    for i in range(3): 
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
                
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0])and board[0][2] != EMPTY:
        return board[0][2]
    return EMPTY

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True
    else:
        return False          

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner1 = winner(board)
    if winner1 == EMPTY:
        return 0
    elif winner1 == X:
        return 1
    elif winner1 == O:
        return -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return EMPTY
    currentPlayer = player(board)
    
    if moveToWin(board,currentPlayer) != EMPTY:
        return moveToWin(board,currentPlayer) 
    else:
        opponent = X
        if currentPlayer == X:
            opponent = "O"
        if moveToWin(board, opponent) != EMPTY:
            return moveToWin(board, opponent)
        else:
            if board[1][1] == EMPTY:
                return [1,1]
            if board[1][1] == currentPlayer and board[0][2] == EMPTY:
                return [0,2]
            if board[1][1] == currentPlayer and board[0][0] == EMPTY:
                return [0,0]
            if board[1][1] == currentPlayer and board[2][0] == EMPTY:
                return [2,0]
            if board[1][1] == currentPlayer and board[2][2] == EMPTY:
                return [2,2]
            if board[0][0] == EMPTY:
                return [0][0]
            if board[0][2] == EMPTY:
                return [0,2]
            if board[2][0] == EMPTY:
                return [2,0]
            if board[2][2] == EMPTY:
                return [2,2]
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        return [i,j]

def moveToWin(board, player):
    """
    Returns the move to play for the player to win 
    If there isn't amy returns EMPTY
    """

    for i in range(3): 
        one = board[i][0]
        two = board[i][1] 
        three = board[i][2]
        
        if one == two and one != EMPTY and three == EMPTY and one == player:
            return [i,2] 
        if two == three and two != EMPTY and one == EMPTY and two == player:
            return[i,0]
        if one == three and one != EMPTY and two == EMPTY and three == player:
            return[i,1]
        one = board[0][i]
        two = board[1][i] 
        three = board[2][i]
        if one == two and one != EMPTY and three == EMPTY and one == player:
            return[2,i] 
        if two == three and two != EMPTY and one == EMPTY and two == player:
            return[0,i]
        if one == three and one != EMPTY and two == EMPTY and one == player:
            return[1,i]

    one = board[0][0]
    two = board[1][1] 
    three = board[2][2]
    if one == two and one != EMPTY and three == EMPTY and one == player:
        return[2,2] 
    if two == three and two != EMPTY and one == EMPTY and two == player:
        return[0,0]
    if one == three and one != EMPTY and two == EMPTY and one == player:
        return[1,1]

    one = board[0][2]
    three = board[2][0]
    if one == two and one != EMPTY and three == EMPTY and one == player:
        return[2,0] 
    if two == three and two != EMPTY and one == EMPTY and two == player:
        return[0,2]
    if one == three and one != EMPTY and two == EMPTY and one == player:
        return[1,1]

    return EMPTY