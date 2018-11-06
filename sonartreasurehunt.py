#Sonar Treasure Hunt

import random
import sys
import math

def getNewBoard():
    #Create a new 60x15 board data structure
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            #Using different characters
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    #Create a string variable of the line with 1, 2, 3, 4, 5
    tensDigitsLine = '    ' # Initial space for numbers starting in down the left
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)
    print(tensDigitsLine)
    print('    ' + ('0123456789' * 6))
    print()
    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        #single digit numbers need to be padded with an extra space
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))
    #Printing the numbers at the bottom
    print()
    print('    ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    #Create a list of chest data structure (two-item lists of x, y int coordinates)
    chests = []
    while len(chests) < numChests:
        newChest =[random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14
















def main():
    drawBoard(getNewBoard())
    print(getRandomChests(5))
    pass

if __name__ == '__main__':
    main()
