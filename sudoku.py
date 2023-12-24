import random
import math
import time


cols = list(range(1, 10))
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

def printTest():
    for i in range(101):
        # time.sleep(0.01)
        print('Downloading File FooFile.txt [%d%%]\r'%i, end="")

def validateBoard(boardMap):
    if len(boardMap) != 81:
        return 'err_size'

def prepBoard(boardMap):
    for k in boardMap:
        print(boardMap[k], end = '')

def generateBoard():
    gameBoard = {}

    for r in rows:
        for c in cols:
            cell = r + str(c)
            gameBoard[cell] = 0

    return gameBoard
    
# Generate random first column and row
def seedGame(gameBoard):
    nums = list(range(1, 10))
    random.shuffle(nums)
    print(nums)

    blockMap = {}
    blockSet = {}

    i = 0
    for r in range(3):
        for c in range(3):
            cell = rows[r] + str(cols[c])
            gameBoard[cell] = nums[i]
            i = i + 1

    rowNums = nums.copy()
    rowNums[3:] = random.sample(rowNums[3:], len(rowNums[3:]))
    rowMap = {}
    rowSet = {}
    
    for c in cols:
        cell = rows[0] + str(c)
        rowSet[c] = rowNums[c - 1]
        gameBoard[cell] = rowNums[c - 1]

    rowMap[rows[0]] = rowSet
    print("rs ", rowSet)
    print("rm ", rowMap)

    nums.remove(gameBoard['A1'])
    nums.remove(gameBoard['B1'])
    nums.remove(gameBoard['C1'])
    colNums = list()
    colNums.append(gameBoard['A1'])
    colNums.append(gameBoard['B1'])
    colNums.append(gameBoard['C1'])
    colNums.extend(nums)
    colNums[3:] = random.sample(colNums[3:], len(colNums[3:]))

    colMap = {}
    colSet = {}
    i = 0
    for r in rows:
        cell = r + str(cols[0])
        colSet[r] = colNums[i]
        gameBoard[cell] = colNums[i]
        i = i + 1
    
    colMap[cols[0]] = colSet
    print("cs ", colSet)
    print("cm ", colMap)

    return gameBoard

def printBoard(gameBoard):
    rowNr = 0

    for r in rows:
        for c in cols:
            if(rowNr != 0 and rowNr % 3 == 0):
                for i in cols:
                    print(' —', end = '')
                    if(i == 9):
                        print()
                        rowNr = 0

                    elif(i % 3 == 0):
                        print(' +', end = '')
            cell = r + str(c)
            print(' ' + str(gameBoard[cell]), end = '')

            if(c == 9):
                print()
                rowNr = rowNr + 1

            elif(c % 3 == 0):
                print(' |', end = '')

if __name__ == "__main__":
    # printTest()
    gameBoard = seedGame(generateBoard())

    printBoard(gameBoard)
    # populateBoard(gameBoard)
    # if validateBoard(gameBoard) == 'err_size':
    #     print("err_size")
    #     exit 

    # prepBoard(gameBoard)
    
