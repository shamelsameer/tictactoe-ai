import math
import copy

X = "X"
O = "O"
EMPTY = 0


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count = 0
    for x in board:
        for y in x:
            if y == EMPTY:
                count+=1
    if count%2==1:
        return X
    else:
        return O


def actions(board):
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i,j))
    return acts


def result(board, action):
    if action in actions(board):
        (i, j) = action
        current_player = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = current_player
        return new_board
    else:
        raise Exception


def winner(board):
    xs = 0
    ys = 0
    xother=0
    oother =0
    for row in board:
        xs = row.count(X)
        ys = row.count(O)
        if xs == 3:
            return X
        if ys == 3:
            return O
    for x in range(3):
        xother = 0
        oother =0
        for y in range(3):
            if board[y][x]==X:
                xother+=1
            if board[y][x]==O:
                oother+=1
        if xother ==3:
            return X
        if oother ==3:
            return O
    if (board[0][0]== X and board[1][1]==X and board[2][2] ==X):
        return X
    if (board[0][2]==X and board[1][1]==X and board[2][0]==X):
        return X
    if (board[0][0]== O and board[1][1]==O and board[2][2] ==O):
        return O
    if (board[0][2]==O and board[1][1]==O and board[2][0]==O):
        return O
    return None

def terminal(board):
    if winner(board)==X or winner(board)==O:
        return True
    for x in range(3):
        for y in range(3):
            if board[x][y]==EMPTY:
                return False
    return True
    


def utility(board):
    if winner(board)==X:
        return 1
    if winner(board)==O:
        return -1
    else:
        return 0
    
    


def minimax(board):
    if terminal(board):
        return None
    return helper(board)
                


def helper(board):
    smallaction = None
    largeaction = None
    smallest = 5000
    largest = -5000
    new_board = None
    for x in actions(board):
        new_board = result(board,x)
        if player(board)==X:
            if minO(new_board)>largest:
                largeaction = x
                largest=minO(new_board)
        if player(board)==O:
            if maxX(new_board)<smallest:
                smallaction = x
                smallest = maxX(new_board)
    if player(board)==X:
        return largeaction
    else:
        return smallaction


def maxX(board):
    largevalue = -1000
    if terminal(board):
        return utility(board)
    for x in actions(board):
        new_board = result(board,x)
        largevalue = max(largevalue, minO(new_board))
    return largevalue

def minO(board):
    smallvalue = 1000
    if terminal(board):
        return utility(board)
    for x in actions(board):
        new_board = result(board,x)
        smallvalue = min(smallvalue, maxX(new_board))
    return smallvalue
