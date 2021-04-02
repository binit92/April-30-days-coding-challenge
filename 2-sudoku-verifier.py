import random
from time import sleep

def get_empty_board():
    return [[0,0,0,0,0,0,0,0,0] * 9] *9

# invalid board
def get_invalid_board():
    return [
    [0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

# 0 represents empty
def get_valid_board():
    return [
    [0,0,0,2,6,9,7,8,1],
    [6,8,2,5,7,1,4,9,3],
    [1,9,7,8,3,4,5,6,2],
    [8,2,6,1,0,5,3,4,0],
    [3,7,4,6,8,2,9,1,5],
    [0,5,0,0,4,3,6,2,8],
    [5,1,9,3,2,6,8,7,4],
    [2,0,8,9,0,7,1,3,6],
    [7,6,3,4,1,8,2,5,9]
    ]


def get_solved_board():
    return [
    [4,3,5,2,6,9,7,8,1],
    [6,8,2,5,7,1,4,9,3],
    [1,9,7,8,3,4,5,6,2],
    [8,2,6,1,9,5,3,4,7],
    [3,7,4,6,8,2,9,1,5],
    [9,5,1,7,4,3,6,2,8],
    [5,1,9,3,2,6,8,7,4],
    [2,4,8,9,5,7,1,3,6],
    [7,6,3,4,1,8,2,5,9]
    ]


def check_empty(board):
    for val in board:
        for char in val:
            if char != 0:
                return  False
    return True

def check_valid(board):
    if isRowCorrect(board) and isColumCorrect(board) and isRoomCorrect(board) and not isFilled(board):
        return True
    return False

def check_solved(board):
    if isRowCorrect(board) and isColumCorrect(board) and isRoomCorrect(board) and isFilled(board):
        return True
    return False

def check_invalid(board):
    if not isRowCorrect(board):
        return True
    if not isColumCorrect(board):
        return True
    if not isRoomCorrect(board):
        return True
    return False

def isRowCorrect(board):
    for val in board:
        temp = val
        # remove all instances of 0
        temp = [i for i in temp if i != 0]

        #print(temp)
        if len(temp) != len(set(temp)):
            #print("row-incorrect")
            return False
    #print("row-correct")
    return True

def isColumCorrect(board):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(board[j][i])
        # remove all instances of 0
        temp = [i for i in temp if i != 0]

        if len(temp) != len(set(temp)):
            return False
    return True

def isRoomCorrect(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp = []

            for k in range(3):
                for l in range(3):
                    temp.append(board[i+k][j+l])


            #print(temp)
            # remove all instances of 0
            temp = [i for i in temp if i != 0]

            if len(temp) != len(set(temp)):
                return False
    return True


def isFilled(board):
    for val in board:
        for char in val:
            if char == 0:
                return  False
    return True



def checkAll(board):

    if check_empty(board):
        return "EMPTY"
    elif check_invalid(board):
        return "INVALID"
    elif check_valid(board):
        return "VALID"
    elif check_solved(board):
        return "SOLVED"



if __name__ == '__main__':
    empty_board = get_empty_board()
    invalid_board = get_invalid_board()
    valid_board = get_valid_board()
    solved_board = get_solved_board()


    print(checkAll(empty_board))
    print(checkAll(invalid_board))
    print(checkAll(valid_board))
    print(checkAll(solved_board))
