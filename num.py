#Create an empty board

#paint to screen

#Initizalize a boolean variable
    #repeat = True

#While repeat = True:
    #ask user for row, column
    #place in on board
    #print board
    #get x's by rowns and col.
    #If any element in an array = 3 then user wins
    #get computer row, col = r
        #while board [r,c] == 'x' or 'o'
            #get row and col again
    #put it on board
    #paint board
    #get row and col count for computer for o's
    #if ant element = 3  then computer wins
        #repeat = False



        #use rand for computers row and col if already taken do random again


import numpy as np
import random

board = np.array([['','',''],['','',''],['','','']])
print(board)
'''
count_row = np.count_nonzero(myarray == 'X', axis = 1)
print(count_row)

count_row = np.count_nonzero(myarray == 'X', axis = 1)
print(count_col)
'''
repeat = True
num = 3

while repeat == True:
    row = input("row number:")
    col = input("col number:")
    r = int(row)
    c = int(col)

    board[r,c] = 'X'
    print(board)
    count_row = np.count_nonzero(board == 'X', axis = 1)
    count_col = np.count_nonzero(board == 'X', axis = 0)
    if num in count_row:
        print('You Won!!')
        repeat = False
        break
    else:
        if num in count_col:
            print('You Won!!')
            repeat = False
            break
    
    r = random.randrange(0,3)
    c = random.randrange(0,3)
    while board[r,c] == 'X' or board[r,c] == 'O':
        r = random.randrange(0,3)
        c = random.randrange(0,3)
    board[r,c] = 'O'
    print(board)
    comp_row = np.count_nonzero(board == 'O', axis = 1)
    print(comp_row)
    comp_col = np.count_nonzero(board == 'O', axis = 0)
    print(comp_col)
    if num in comp_row:
        print('You lose!!')
        repeat == False
    else:
        if num in comp_col:
            print('You lose!')
            repeat = False