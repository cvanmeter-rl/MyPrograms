import numpy as np
import time

generatedp1 = 0
generatedp2 = 0
player1,player2 = 'x','o'
#this function returns true if there is any moves left and if not then there is a tie and it returns false
def isMovesLeft(board):
    for row in range(5):
        for col in range(6):
            if board[row][col] == '_':
                return True
    return False
# this function returns a list of coordinates possible moves for a player
# takes a 2d array as the game state and a char indicating whose turn it currently is
def calculatePossibleMoves(board, player):
    tmp_move_list = []
    ret_move_list = []

    max_row = len(board) - 1
    max_col = len(board[0]) - 1

    # first we check each cell in the board for pieces belonging to the current player
    which_row = 0
    for row in board:
        which_col = 0
        for cell in row:
            if cell == player1 or cell == player2:
                # make sure we don't consider spaces that would be off the board
                l = r = u = d = False
                if which_row - 1 >= 0:
                    u = True
                if which_row + 1 <= max_row:
                    d = True
                if which_col - 1 >= 0:
                    l = True
                if which_col + 1 <= max_col:
                    r = True

                # check three spaces above, if not on edge
                if u == True:
                    tmp_move_list.append((which_row - 1, which_col))
                    if l == True >= 0:
                        tmp_move_list.append((which_row - 1, which_col - 1))
                    if r == True <= 5:
                        tmp_move_list.append((which_row - 1, which_col + 1))

                # check three spaces below, if not on edge
                if d == True:
                    tmp_move_list.append((which_row + 1, which_col))
                    if l == True >= 0:
                        tmp_move_list.append((which_row + 1, which_col - 1))
                    if r == True <= 5:
                        tmp_move_list.append((which_row + 1, which_col + 1))

                # check spaces to left and right
                if l == True:
                    tmp_move_list.append((which_row, which_col - 1))
                if r == True:
                    tmp_move_list.append((which_row, which_col + 1))

                # finally make sure possible move is empty space and is not already in the list
                for poss_move in tmp_move_list:
                    x = int(poss_move[0])
                    y = int(poss_move[1])

                    if poss_move not in ret_move_list and board[x][y] == "_":
                        ret_move_list.append(poss_move)
            which_col += 1
        which_row += 1
    res = np.unique(ret_move_list)
    return ret_move_list

#checks the entire board to see if either player has won, returns 1000 if player 1 won, -1000 if player 2 won and a 0 if no winner so far
def checkForWin(board):
    check = checkRowWins(board)
    if check == 1:
        return 1000
    elif check == 2:
        return -1000
    check = checkColWins(board)
    if check == 1:
        return 1000
    elif check == 2:
        return -1000
    check = checkDiagWins(board)
    if check == 1:
        return 1000
    elif check == 2:
        return -1000
    return 0
#checks if a winner is found in all the columns and returns a 0 if nobody has won, a 1 if player 1 has won, and a 2 if player 2 has won
def checkColWins(board):
    for col in range(6):
        for row in range(2):
            if(board[row][col] == 'x' and board[row+1][col] == 'x' and board[row+2][col] == 'x' and board[row+3][col] == 'x'):
                return 1
            elif(board[row][col] == 'o' and board[row+1][col] == 'o' and board[row+2][col] == 'o' and board[row+3][col] == 'o'):
                return 2
    return 0
#this function checks for a win in all rows and returns a 0 if nobody has won, a 1 if player 1 has won, and a 2 if player 2 has won
def checkRowWins(board):
    for row in range(5):
        for col in range(3):
            if(board[row][col] == 'x' and board[row][col+1] == 'x' and board[row][col+2] == 'x' and board[row][col+3] == 'x'):
                return 1
            elif(board[row][col] == 'o' and board[row][col+1] == 'o' and board[row][col+2] == 'o' and board[row][col+3] == 'o'):
                return 2
    return 0 
#checks for wins on diagonals, returns a 0 if nobody has won, a 1 if player 1 has won, and 2 if player 2 has won
def checkDiagWins(board):
    if(board[1][0] == 'x' and board[2][1] == 'x' and board[3][2] == 'x' and board[4][3] == 'x'):#checks diagonal wins for player 1
        return 1
    elif(board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x' and board[3][3] == 'x'):
        return 1
    elif(board[1][1] == 'x' and board[2][2] == 'x' and board[3][3] == 'x' and board[4][4] == 'x'):
        return 1
    elif(board[0][1] == 'x' and board[1][2] == 'x' and board[2][3] == 'x' and board[3][4] == 'x'):
        return 1
    elif(board[1][2] == 'x' and board[2][3] == 'x' and board[3][4] == 'x' and board[4][5] == 'x'):
        return 1
    elif(board[0][2] == 'x' and board[1][3] == 'x' and board[2][4] == 'x' and board[3][5] == 'x'):
        return 1
    elif(board[3][0] == 'x' and board[2][1] == 'x' and board[1][2] == 'x' and board[0][3] == 'x'):
        return 1
    elif(board[4][0] == 'x' and board[3][1] == 'x' and board[2][2] == 'x' and board[1][3] == 'x'):
        return 1
    elif(board[3][1] == 'x' and board[2][2] == 'x' and board[1][3] == 'x' and board[0][4] == 'x'):
        return 1
    elif(board[4][1] == 'x' and board[3][2] == 'x' and board[2][3] == 'x' and board[1][4] == 'x'):
        return 1
    elif(board[3][2] == 'x' and board[2][3] == 'x' and board[1][4] == 'x' and board[0][5] == 'x'):
        return 1
    elif(board[4][2] == 'x' and board[3][3] == 'x' and board[2][4] == 'x' and board[1][5] == 'x'):
        return 1
    elif(board[1][0] == 'o' and board[2][1] == 'o' and board[3][2] == 'o' and board[4][3] == 'o'):#checks diagonal wins for player 2
        return 2
    elif(board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o' and board[3][3] == 'o'):
        return 2
    elif(board[1][1] == 'o' and board[2][2] == 'o' and board[3][3] == 'o' and board[4][4] == 'o'):
        return 2
    elif(board[0][1] == 'o' and board[1][2] == 'o' and board[2][3] == 'o' and board[3][4] == 'o'):
        return 2
    elif(board[1][2] == 'o' and board[2][3] == 'o' and board[3][4] == 'o' and board[4][5] == 'o'):
        return 2
    elif(board[0][2] == 'o' and board[1][3] == 'o' and board[2][4] == 'o' and board[3][5] == 'o'):
        return 2
    elif(board[3][0] == 'o' and board[2][1] == 'o' and board[1][2] == 'o' and board[0][3] == 'o'):
        return 2
    elif(board[4][0] == 'o' and board[3][1] == 'o' and board[2][2] == 'o' and board[1][3] == 'o'):
        return 2
    elif(board[3][1] == 'o' and board[2][2] == 'o' and board[1][3] == 'o' and board[0][4] == 'o'):
        return 2
    elif(board[4][1] == 'o' and board[3][2] == 'o' and board[2][3] == 'o' and board[1][4] == 'o'):
        return 2
    elif(board[3][2] == 'o' and board[2][3] == 'o' and board[1][4] == 'o' and board[0][5] == 'o'):
        return 2
    elif(board[4][2] == 'o' and board[3][3] == 'o' and board[2][4] == 'o' and board[1][5] == 'o'):
        return 2
    else:
        return 0
#this function calculates the counts for one side open and two side open for 3-in-a-row and 2-in-a-row
#h(n) = 200*[number of two-side-open-3-in-a-row for me]
#– 80*[number of two-side-open-3-in-a-row for opponent]
#+ 150*[number of one-side-open-3-in-a-row for me]
#– 40*[number of one-side-open-3-in-a-row for opponent]
#+ 20*[number of two-side-open-2-in-a-row for me]
#– 15*[number of two-side-open-2-in-a-row for opponent]
#+ 5*[number of one-side-open-2-in-a-row for me]
#– 2*[number of one-side-open-2-in-a-row for opponent]
#where
#• “one-side-open-3-in-a-row”: there is an empty space next to one end of a 3-
#in-a-row to potentially make it 4-in-a row in the next move.
#• “two-side-open-3-in-a-row”: there are empty spaces next to both ends of a 3-
#in-a-row to potentially make it 4-in-a row in the next move.
#• “one-side-open-2-in-a-row”: there is an empty space next to one end of a 2-
#in-a-row to potentially make it 3-in-a row in the next move.
#• “two-side-open-2-in-a-row”: there are empty spaces next to both ends of a 2-
#in-a-row to potentially make it 3-in-a row in the next move.
def calculateHeuristicCounts(board,symbol):
    if symbol == 'x':
        enemySymbol = 'o'
    else:
        enemySymbol = 'x'
    oneSide3 = 0
    twoSide3 = 0
    oneSide2 = 0
    twoSide2 = 0
    #calculates open 2 heuristics for rows
    for row in range(5):
        for col in range(5):
            if board[row][col] == symbol and board[row][col+1] == symbol:
                if (col-1 >= 0 and board[row][col-1] == '_' and (col+2 <= 5 and board[row][col+2] != symbol and board[row][col+2] != '_')) or (col+2 <= 5 and board[row][col+2] == '_' and (col-1 >= 0 and board[row][col-1] != symbol and board[row][col-1] != '_')):#empty space next to one end
                    oneSide2 += 1
                elif((col-1 >= 0 and col+2 <=5) and (board[row][col-1] == '_' and board[row][col+2] == '_')):#empty space next to both ends
                    twoSide2 += 1
    #calculates open 2 heuristics for columns
    for col in range(6):
        for row in range(4):
            if board[row][col] == symbol and board[row+1][col] == symbol:
                if (row-1 >= 0 and board[row-1][col] == '_' and (row + 2 <= 4 and board[row+2][col] != symbol and board[row+2][col] != '_')) or (row+2 <= 4 and board[row+2][col] == '_' and (row-1 >= 0 and board[row-1][col] != symbol and board[row-1][col] != '_')):#empty space next to one end
                    oneSide2 += 1
                elif((row-1 >= 0 and row+2 <=4) and (board[row-1][col] == '_' and board[row+2][col] == '_')):#empty space next to both ends
                    twoSide2 += 1

    #calculates open 2 heuristics for diagonals
    #these statements find one side 2 for diagonals going in downward direction
    if(board[2][0] == symbol and board[3][1] == symbol and board[4][2] == '_'):
        oneSide2 += 1
    if(board[2][0] == '_' and board[3][1] == symbol and board[4][2] == symbol):
        oneSide2 += 1
    if(board[1][0] == symbol and board[2][1] == symbol and board[3][2] == '_'): 
        oneSide2 += 1
    if(board[2][1] == symbol and board[3][2] == symbol and board[1][0] == '_' and (board[4][3] != '_' and board[4][3] == enemySymbol)):
        oneSide2 += 1
    if(board[2][1] == symbol and board[3][2] == symbol and board[4][3] == '_' and (board[1][0] != '_' and board[1][0] == enemySymbol)):
        oneSide2 += 1
    if(board[3][2] == symbol and board[4][3] == symbol and board[2][1] == '_'):
        oneSide2 += 1
    if(board[0][0] == symbol and board[1][1] == symbol and board[2][2] == '_'):
        oneSide2 += 1
    if(board[1][1] == symbol and board[2][2] == symbol and board[0][0] == '_' and (board[3][3] != '_' and board[3][3] == enemySymbol)):
        oneSide2 += 1
    if(board[1][1] == symbol and board[2][2] == symbol and board[3][3] == '_' and (board[0][0] != '_' and board[0][0] == enemySymbol)):
        oneSide2 += 1
    if(board[2][2] == symbol and board[3][3] == symbol and board[1][1] == '_' and (board[4][4] != '_' and board[4][4] == enemySymbol)):
        oneSide2 += 1
    if(board[2][2] == symbol and board[3][3] == symbol and board[4][4] == '_' and (board[1][1] != '_' and board[1][1] == enemySymbol)):
        oneSide2 += 1
    if(board[3][3] == symbol and board[4][4] == symbol and board[2][2] == '_'):
        oneSide2 += 1
    if(board[0][1] == symbol and board[1][2] == symbol and board[2][3] == '_'):
        oneSide2 += 1
    if(board[1][2] == symbol and board[2][3] == symbol and board[0][1] == '_' and (board[3][4] != '_' and board[3][4] == enemySymbol)):
        oneSide2 += 1
    if(board[1][2] == symbol and board[2][3] == symbol and board[3][4] == '_' and (board[0][1] != '_' and board[0][1] == enemySymbol)):
        oneSide2 += 1
    if(board[2][3] == symbol and board[3][4] == symbol and board[1][2] == '_' and (board[4][5] != '_' and board[4][5] == enemySymbol)):
        oneSide2 += 1
    if(board[2][3] == symbol and board[3][4] == symbol and board[4][5] == '_' and (board[1][2] != '_' and board[1][2] == enemySymbol)):
        oneSide2 += 1
    if(board[3][4] == symbol and board[4][5] == symbol and board[2][3] == '_'):
        oneSide2 += 1
    if(board[0][2] == symbol and board[1][3] == symbol and board[2][4] == '_'):
        oneSide2 += 1
    if(board[1][3] == symbol and board[2][4] == symbol and board[0][2] == '_' and (board[3][5] != '_' and board[3][5] == enemySymbol)):
        oneSide2 += 1
    if(board[1][3] == symbol and board[2][4] == symbol and board[3][5] == '_' and (board[0][2] != '_' and board[0][2] == enemySymbol)):
        oneSide2 += 1
    if(board[2][4] == symbol and board[3][5] == symbol and board[1][3] == '_'):
        oneSide2 += 1
    if(board[0][3] == symbol and board[1][4] == symbol and board[2][5] == '_'):
        oneSide2 += 1
    if(board[1][4] == symbol and board[2][5] == symbol and board[0][3] == '_'):
        oneSide2 += 1
    #these statements find one side 2 for diagonals going in upward direction
    if(board[2][0] == symbol and board[1][1] == symbol and board[0][2] == '_'):
        oneSide2 += 1
    if(board[1][1] == symbol and board[0][2] == symbol and board[2][0] == '_'):
        oneSide2 += 1
    if(board[3][0] == symbol and board[2][1] == symbol and board[1][2] == '_'):
        oneSide2 += 1
    if(board[2][1] == symbol and board[1][2] == symbol and board[3][0] == '_' and (board[0][3] != '_' and board[0][3] == enemySymbol)):
        oneSide2 += 1
    if(board[2][1] == symbol and board[1][2] == symbol and board[0][3] == '_' and (board[3][0] != '_' and board[3][0] == enemySymbol)):
        oneSide2 += 1
    if(board[1][2] == symbol and board[0][3] == symbol and board[2][1] == '_'):
        oneSide2 += 1
    if(board[4][0] == symbol and board[3][1] == symbol and board[2][2] == '_'):
        oneSide2 += 1
    if(board[3][1] == symbol and board[2][2] == symbol and board[4][0] == '_' and (board[1][3] != '_' and board[1][3] == enemySymbol)):
        oneSide2 += 1
    if(board[3][1] == symbol and board[2][2] == symbol and board[1][3] == '_' and (board[4][0] != '_' and board[4][0] == enemySymbol)):
        oneSide2 += 1
    if(board[2][2] == symbol and board[1][3] == symbol and board[3][1] == '_' and (board[0][4] != '_' and board[0][4] == enemySymbol)):
        oneSide2 += 1
    if(board[2][2] == symbol and board[1][3] == symbol and board[0][4] == '_' and (board[3][1] != '_' and board[3][1] == enemySymbol)):
        oneSide2 += 1
    if(board[1][3] == symbol and board[0][4] == symbol and board[2][2] == '_'):
        oneSide2 += 1
    if(board[4][1] == symbol and board[3][2] == symbol and board[2][3] == '_'):
        oneSide2 += 1
    if(board[3][2] == symbol and board[2][3] == symbol and board[4][1] == '_' and (board[1][4] != '_' and board[1][4] == enemySymbol)):
        oneSide2 += 1
    if(board[3][2] == symbol and board[2][3] == symbol and board[1][4] == '_' and (board[4][1] != '_' and board[4][1] == enemySymbol)):
        oneSide2 += 1
    if(board[2][3] == symbol and board[1][4] == symbol and board[3][2] == '_' and (board[0][5] != '_' and board[0][5] == enemySymbol)):
        oneSide2 += 1
    if(board[2][3] == symbol and board[1][4] == symbol and board[0][5] == '_' and (board[3][2] != '_' and board[3][2] == enemySymbol)):
        oneSide2 += 1
    if(board[1][4] == symbol and board[0][5] == symbol and board[2][3] == '_'):
        oneSide2 += 1
    if(board[4][2] == symbol and board[3][3] == symbol and board[2][4] == '_'):
        oneSide2 += 1
    if(board[3][3] == symbol and board[2][4] == symbol and board[4][2] == '_' and (board[1][5] != '_' and board[1][5] == enemySymbol)):
        oneSide2 += 1
    if(board[3][3] == symbol and board[2][4] == symbol and board[1][5] == '_' and (board[4][2] != '_' and board[4][2] == enemySymbol)):
        oneSide2 += 1
    if(board[2][4] == symbol and board[1][5] == symbol and board[3][3] == '_'):
        oneSide2 += 1
    if(board[4][3] == symbol and board[3][4] == symbol and board[2][5] == '_'):
        oneSide2 += 1
    if(board[3][4] == symbol and board[2][5] == symbol and board[4][3] == '_'):
        oneSide2 += 1
    #these statements find two side 2 for diagonals going in downward direction
    if(board[1][0] == '_' and board[2][1] == symbol and board[3][2] == symbol and board[4][3] == '_'):
        twoSide2 += 1
    if(board[0][0] == '_' and board[1][1] == symbol and board[2][2] == symbol and board[3][3] == '_'):
        twoSide2 += 1
    if(board[1][1] == '_' and board[2][2] == symbol and board[3][3] == symbol and board[4][4] == '_'):
        twoSide2 += 1
    if(board[0][1] == '_' and board[1][2] == symbol and board[2][3] == symbol and board[3][4] == '_'):
        twoSide2 += 1
    if(board[1][2] == '_' and board[2][3] == symbol and board[3][4] == symbol and board[4][5] == '_'):
        twoSide2 += 1
    if(board[0][2] == '_' and board[1][3] == symbol and board[2][4] == symbol and board[3][5] == '_'):
        twoSide2 += 1
    #these statements find two side 2 for diagonals going in upward direction
    if(board[3][0] == '_' and board[2][1] == symbol and board[1][2] == symbol and board[0][3] == '_'):
        twoSide2 += 1
    if(board[4][0] == '_' and board[3][1] == symbol and board[2][2] == symbol and board[1][3] == '_'):
        twoSide2 += 1
    if(board[3][1] == '_' and board[2][2] == symbol and board[1][3] == symbol and board[0][4] == '_'):
        twoSide2 += 1
    if(board[4][1] == '_' and board[3][2] == symbol and board[2][3] == symbol and board[1][4] == '_'):
        twoSide2 += 1
    if(board[3][2] == '_' and board[2][3] == symbol and board[1][4] == symbol and board[0][5] == '_'):
        twoSide2 += 1
    if(board[4][2] == '_' and board[3][3] == symbol and board[2][4] == symbol and board[1][5] == '_'):
        twoSide2 += 1
    #calculates open 3 heuristics for rows
    for row in range(5):
        for col in range(4):
            if board[row][col] == symbol and board[row][col+1] == symbol and board[row][col+2] == symbol:
                if (col-1 >= 0 and board[row][col-1] == '_' and (col+3 <= 5 and board[row][col+3] != symbol and board[row][col+3] != '_')) or (col+3 <= 5 and board[row][col+3] == '_' and (col-1 >= 0 and board[row][col-1] != symbol and board[row][col-1] != '_')):#empty space next to one end
                    oneSide3 += 1
                elif((col-1 >= 0 and col+3 <=5) and (board[row][col-1] == '_' and board[row][col+3] == '_')):#empty space next to both ends
                    twoSide3 += 1
    #calculates open 3 heuristics for columns
    for col in range(6):
        for row in range(3):
            if board[row][col] == symbol and board[row+1][col] == symbol and board[row+2][col] == symbol:
                if (row-1 >= 0 and board[row-1][col] == '_' and (row+3 <= 4 and board[row+3][col] !=  symbol and board[row+3][col] != '_')) or (row+3 <= 4 and board[row+1][col] == '_' and (row-1 >= 0 and board[row-1][col] != symbol and board[row-1][col] != '_')):#empty space next to one end
                    oneSide3 += 1
                elif((row-1 >= 0 and row+3 <=4) and (board[row-1][col] == '_' and board[row+3][col] == '_')):#empty space next to both ends
                    twoSide3 += 1
    #calculates open 3 heuristics for diagonals
    #these statements find one side 3 for diagonals going in downward direction
    if(board[1][0] == symbol and board[2][1] == symbol and board[3][2] == symbol and board[4][3] == '_'):
        oneSide3 += 1
    if(board[2][1] == symbol and board[3][2] == symbol and board[4][3] == symbol and board[1][0] == '_'):
        oneSide3 += 1
    if(board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol and board[3][3] == '_'):
        oneSide3 += 1
    if(board[1][1] == symbol and board[2][2] == symbol and board[3][3] == symbol and board[0][0] == '_' and (board[4][4] != '_' and board[4][4] == enemySymbol)):
        oneSide3 += 1
    if(board[1][1] == symbol and board[2][2] == symbol and board[3][3] == symbol and board[4][4] == '_' and (board[0][0] != '_' and board[0][0] == enemySymbol)):
        oneSide3 += 1
    if(board[2][2] == symbol and board[3][3] == symbol and board[4][4] == symbol and board[1][1] == '_'):
        oneSide3 += 1
    if(board[0][1] == symbol and board[1][2] == symbol and board[2][3] == symbol and board[3][4] == '_'):
        oneSide3 += 1
    if(board[1][2] == symbol and board[2][3] == symbol and board[3][4] == symbol and board[0][1] == '_' and (board[4][5] != '_' and board[4][5] == enemySymbol)):
        oneSide3 += 1
    if(board[1][2] == symbol and board[2][3] == symbol and board[3][4] == symbol and board[4][5] == '_' and (board[0][1] != '_' and board[0][1] == enemySymbol)):
        oneSide3 += 1
    if(board[2][3] == symbol and board[3][4] == symbol and board[4][5] == symbol and board[1][2] == '_'):
        oneSide3 += 1
    if(board[0][2] == symbol and board[1][3] == symbol and board[2][4] == symbol and board[3][5] == '_'):
        oneSide3 += 1
    if(board[1][3] == symbol and board[2][4] == symbol and board[3][5] == symbol and board[0][2] == '_'):
        oneSide3 += 1
    #these statements find one side 3 for diagonals going in upward direction
    if(board[3][0] == symbol and board[2][1] == symbol and board[1][2] == symbol and board[0][3] == '_'):
        oneSide3 += 1
    if(board[2][1] == symbol and board[1][2] == symbol and board[0][3] == symbol and board[3][0] == '_'):
        oneSide3 += 1
    if(board[4][0] == symbol and board[3][1] == symbol and board[2][2] == symbol and board[1][3] == '_'):
        oneSide3 += 1
    if(board[3][1] == symbol and board[2][2] == symbol and board[1][3] == symbol and board[4][0] == '_' and (board[0][4] != '_' and board[0][4] == enemySymbol)):
        oneSide3 += 1
    if(board[3][1] == symbol and board[2][2] == symbol and board[1][3] == symbol and board[0][4] == '_' and (board[4][0] != '_' and board[4][0] == enemySymbol)):
        oneSide3 += 1
    if(board[2][2] == symbol and board[1][3] == symbol and board[0][4] == symbol and board[3][1] == '_'):
        oneSide3 += 1
    if(board[4][1] == symbol and board[3][2] == symbol and board[2][3] == symbol and board[1][4] == '_'):
        oneSide3 += 1
    if(board[3][2] == symbol and board[2][3] == symbol and board[1][4] == symbol and board[4][1] == '_' and (board[0][5] != '_' and board[0][5] == enemySymbol)):
        oneSide3 += 1
    if(board[3][2] == symbol and board[2][3] == symbol and board[1][4] == symbol and board[0][5] == '_' and (board[4][1] != '_' and board[4][1] == enemySymbol)):
        oneSide3 += 1
    if(board[2][3] == symbol and board[1][4] == symbol and board[0][5] == symbol and board[3][2] == '_'):
        oneSide3 += 1
    if(board[4][2] == symbol and board[3][3] == symbol and board[2][4] == symbol and board[1][5] == '_'):
        oneSide3 += 1
    if(board[3][3] == symbol and board[2][4] == symbol and board[1][5] == symbol and board[4][2] == '_'):
        oneSide3 += 1
    #these statements find two side 3 for diagonals going in downward direction
    if(board[0][0] == '_' and board[1][1] == symbol and board[2][2] == symbol and board[3][3] == symbol and board[4][4] == '_'):
        twoSide3 += 1
    if(board[0][1] == '_' and board[1][2] == symbol and board[2][3] == symbol and board[3][4] == symbol and board[4][5] == '_'):
        twoSide3 += 1
    #these statements find one side 3 for diagonals going in upward direction
    if(board[4][0] == '_' and board[3][1] == symbol and board[2][2] == symbol and board[1][3] == symbol and board[0][4] == '_'):
        twoSide3 += 1
    if(board[4][1] == '_' and board[3][2] == symbol and board[2][3] == symbol and board[1][4] == symbol and board[0][5] == '_'):
        twoSide3 += 1

    return twoSide3,oneSide3,twoSide2,oneSide2
#this function calculates and returns the heuristic value. This function takes symbol1 to be your symbol and symbol2 is to be the opponents symbol
def calculateHeuristicValue(symbol1,symbol2,board):

    s1TwoSide3,s1OneSide3,s1TwoSide2,s1OneSide2 = calculateHeuristicCounts(board,symbol1)
    s2TwoSide3,s2OneSide3,s2TwoSide2,s2OneSide2 = calculateHeuristicCounts(board,symbol2)
    h = (200 * s1TwoSide3) - (80 * s2TwoSide3) + (150 * s1OneSide3) - (40 * s2OneSide3) + (20 * s1TwoSide2) - (15 * s2TwoSide2) + (5 * s1OneSide2) - (2 * s2OneSide2)
    return h
#minimax function for player1
def minimaxPlayer1(board, depth, isMax):
    global generatedp1
    score = checkForWin(board)
    #if maximizer has won
    if score == 1000:
        return score - depth
    #if minimizer has won
    if score == -1000:
        return score + depth
    #if there is no more moves and no winner
    if(isMovesLeft(board) == False):
        return 0
    #here we limit the depth for player 1 because he is only looking ahead two moves
    if depth < 1:
        #maximize
        if(isMax):
            best = -10000


            moves = calculatePossibleMoves(board,player1)
            cost = {}
            #gets heuristic value for each move and sorts it based on score first and tie breaking based on column and then row increasing
            for m in moves:
                board[m[0]][m[1]] = player1
                cost.update({tuple(m):calculateHeuristicValue(player1,player2,board)})
                board[m[0]][m[1]] = '_'
            #sorts based on cost first and then breaks ties based on col num and then row num
            moves = sorted(moves,key = lambda a:(cost.get(tuple(a)),-a[1],-a[0]),reverse=True)
            #now we maximize the moves
            for m in moves:
                #make the move
                board[m[0]][m[1]] = player1
                #recursively call minimax function and choose max value
                generatedp1 += 1
                best = max(best,minimaxPlayer1(board,depth + 1,not isMax))
                #undo the move
                board[m[0]][m[1]] = "_"
            
            return best
        else:
            best = 10000

            moves = calculatePossibleMoves(board,player2)
            cost = {}
            #gets heuristic value for each move and sorts it based on score first and tie breaking based on column and then row increasing
            for m in moves:
                board[m[0]][m[1]] = player2
                cost.update({tuple(m):calculateHeuristicValue(player1,player2,board)})
                board[m[0]][m[1]] = '_'
            #sorts based on cost first and then breaks ties based on col num and then row num
            moves = sorted(moves,key = lambda a:(cost.get(tuple(a)),-a[1],-a[0]),reverse=True)
            
            #now we minimize the moves
            for m in moves:
                #make the move
                board[m[0]][m[1]] = player2
                #recursively call minimax function and choose max value
                generatedp1 += 1
                best = min(best,minimaxPlayer1(board,depth + 1,not isMax))
            
                #undo the move
                board[m[0]][m[1]] = "_"

            return best
    else:
        return score

#minimax function for player1
def minimaxPlayer2(board, depth, isMax):
    global generatedp2
    score = checkForWin(board)

    #if maximizer has won
    if (score * -1) == 1000:
        return (score * -1) - depth
    #if minimizer has won
    if (score * -1) == -1000:
        return (score * -1) + depth
    #if there is no more moves and no winner
    if(isMovesLeft(board) == False):
        return 0
    #here we limit the depth for player 1 because he is only looking ahead two moves
    if depth < 3:
        #maximize
        if(isMax):
            best = -10000

            moves = calculatePossibleMoves(board,player2)
            cost = {}
            #gets heuristic value for each move and sorts it based on score first and tie breaking based on column and then row increasing
            for m in moves:
                board[m[0]][m[1]] = player2
                cost.update({tuple(m):calculateHeuristicValue(player2,player1,board)})
                board[m[0]][m[1]] = '_'
            #sorts based on cost first and then breaks ties based on col num and then row num
            moves = sorted(moves,key = lambda a:(cost.get(tuple(a)),-a[1],-a[0]),reverse=True)

            #now we maximize the moves
            for m in moves:
                #make the move
                board[m[0]][m[1]] = player2
                #recursively call minimax function and choose max value
                generatedp2 += 1
                best = max(best,minimaxPlayer2(board,depth + 1,not isMax))
                #undo the move
                board[m[0]][m[1]] = "_"
            return best
        else:
            best = 10000

            moves = calculatePossibleMoves(board,player1)
            cost = {}
            #gets heuristic value for each move and sorts it based on score first and tie breaking based on column and then row increasing
            for m in moves:
                board[m[0]][m[1]] = player1
                cost.update({tuple(m):calculateHeuristicValue(player2,player1,board)})
                board[m[0]][m[1]] = '_'
            #sorts based on cost first and then breaks ties based on col num and then row num
            moves = sorted(moves,key = lambda a:(cost.get(tuple(a)),-a[1],-a[0]),reverse=True)

            #now we minimize the moves
            for m in moves:
                #make the move
                board[m[0]][m[1]] = player1
                #recursively call minimax function and choose max value
                generatedp2 += 1
                best = min(best,minimaxPlayer2(board,depth + 1,not isMax))
                
                #undo the move
                board[m[0]][m[1]] = "_"
            return best
    else:
        return score
#this function uses the minimax function to find the best move to play
def findMoves(board,symbol):
    bestScore = -10000
    moveChoice = (-1,-1)

    moves = calculatePossibleMoves(board,symbol)
    
    cost = {}
     #gets heuristic value for each move and sorts it based on score first and tie breaking based on column and then row increasing
    for m in moves:
        board[m[0]][m[1]] = symbol
        if symbol == player1:
            cost.update({tuple(m):calculateHeuristicValue(player1,player2,board)})
        else:
            cost.update({tuple(m):calculateHeuristicValue(player2,player1,board)})
        board[m[0]][m[1]] = '_'
    #sorts based on cost first and then breaks ties based on col num and then row num
    moves = sorted(moves,key = lambda a:(cost.get(tuple(a)),-a[1],-a[0]),reverse=True)
    
    for m in moves:
        #make the move
        board[m[0]][m[1]] = symbol
        #recursively call minimax function and choose max value
        if symbol == player1:
            currScore = minimaxPlayer1(board,0,False)
        else:
            currScore = minimaxPlayer2(board,0,False)
        #undo the move
        board[m[0]][m[1]] = "_"
        #if the current move is better than the best value then update the best value and move
        if currScore > bestScore:
            bestScore = currScore
            moveChoice = (m[0],m[1])
    return moveChoice


    
if __name__ == '__main__':
    board = [
    ['_','_','_','_','_','_'],
    ['_','_','_','_','_','_'],
    ['_','_','o','x','_','_'],
    ['_','_','_','_','_','_'],
    ['_','_','_','_','_','_']
    ]
    # h = calculateHeuristicValue('o','x',board)
    # print(h)
    # start = time.time()
    # bestMove = findMoves(board,'o')
    # print("CPU Execution Time: ",time.time()-start)
    # print("Move Made: ",bestMove)
    # board[bestMove[0]][bestMove[1]] = 'o'
    # for r in board:
    #     for c in r:
    #         print(c,end = " ")
    #     print()
    # print("generated: ",generatedp2)
    # print()
    # generatedp2 = 0

    num = 0
    score = checkForWin(board)
    while score != -1000:
        start = time.time()
        bestMove = findMoves(board,'x')
        print("CPU Execution Time: ",time.time()-start)
        print("Move Made: ",bestMove)
        board[bestMove[0]][bestMove[1]] = 'x'
        for r in board:
            for c in r:
                print(c,end = " ")
            print()
        print("generated: ",generatedp1)
        generatedp1 = 0

        score = checkForWin(board)
        if score == 1000:
            break

        start = time.time()
        bestMove = findMoves(board,'o')
        print("CPU Execution Time: ",time.time()-start)
        print("Move Made: ",bestMove)
        board[bestMove[0]][bestMove[1]] = 'o'
        for r in board:
            for c in r:
                print(c,end = " ")
            print()
        print("generated: ",generatedp2)
        generatedp2 = 0
        print() 
        num += 1

        score = checkForWin(board)
    