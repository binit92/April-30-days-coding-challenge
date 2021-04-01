import random
from time import sleep


def init_board():
    return [[0,0,0],[0,0,0],[0,0,0]]

def get_players():
    return [1,2]

def get_empty_places(board):
    ret = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                ret.append((i,j))
    return ret

def check_row_win(board, player):
    for i in range(len(board)):
        ret = True
        for j in range(len(board)):
            if board[i][j] != player:
                ret = False
                continue
        # return if True
        if ret == True:
            return ret
    return False

def check_column_win(board,player):
    for j in range(len(board)):
        ret = True
        for i in range(len(board)):
            if board[j][i] != player:
                ret = False
                continue
        # return if True
        if ret == True:
            return ret
    return False

def check_diagonal_win(board,player):
    ret = True
    for i in range(len(board)):
        if board[i][i] != player:
            ret = False
    if ret:
        return True

    ret = True
    # from 3,1 to 2,2 to 1,3
    for i in range(len(board)):
        j = len(board)-1-i
        if board[i][j] !=player:
            ret = False
    return ret

def check_winner(board,player):
    if check_row_win(board,player) or check_column_win(board,player) or check_diagonal_win(board,player):
        return player
    return 0

def get_random_valid_place(board,player):
    valid = get_empty_places(board)
    place = random.choice(valid)
    print("place",place)
    board[place[0]][place[1]] = player
    return board

def main_play():
    board = init_board()
    players = get_players()
    print(board)
    winner = 0

    while winner == 0:
        breakAll = False
        for player in players:

            # check if empty places are there ..
            empty_places = get_empty_places(board)
            if len(empty_places) < 1:
                breakAll = True
                break

            # find random move
            board = get_random_valid_place(board,player)
            print(player,board)

            # find winner
            winner = check_winner(board,player)
            if winner >0:
                break

        #print("outside")
        if breakAll:
            break

    print("winner", winner)


if __name__ == '__main__':
    main_play()
