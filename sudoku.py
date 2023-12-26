import random
import math
import time

cols = list(range(1, 10))
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

peerMap = {}
colMap = {}
rowMap = {}
boxMap = {}

for n in range(1, 10):
    boxMap[n] = []

def printTest():
    for i in range(101):
        # time.sleep(0.01)
        print('Downloading File FooFile.txt [%d%%]\r'%i, end="")

def validateBoard(boardMap):
    if len(boardMap) != 81:
        return 'err_size'

def splitKey(key):
    row = key[:1]
    col = key[1:]

    return row, col

def setPeers(gameBoard):
    for n in gameBoard:
        peers = []
        r, c = splitKey(n)
        c = int(c)
        peers.extend(rowMap[r])
        peers.extend(colMap[c])
        for i in boxMap:
            if n in boxMap[i]:
                peers.extend(boxMap[i])
                break
        peers = list(set(peers))
        peers.sort()
        peers.remove(n)

        peerMap[n] = peers
    
def generateBoard():
    gameBoard = {}
    # box = 1
    for r in rows:
        rowSet = []
        if r == 'A' or r == 'B' or r == 'C':
            box = 1
        if r == 'D' or r == 'E' or r == 'F':
            box = 4
        if r == 'G' or r == 'H' or r == 'I':
            box = 7

        for c in cols:
            if c == 4 or c == 7:
                box = box + 1

            cell = r + str(c)
            gameBoard[cell] = 0
            boxMap[box].append(cell)
            rowSet.append(cell)

        rowMap[r] = rowSet
        
    for c in cols:
        colSet = []
        for r in rows:
            cell = r + str(c)
            colSet.append(cell)
          
        colMap[c] = colSet
    
    setPeers(gameBoard)
    return gameBoard
    
# Generate random first column and row
def seedGame(gameBoard):
    nums = list(range(1, 10))
    random.shuffle(nums)

    # Populate top left 3x3 randomly
    i = 0
    for r in range(3):
        for c in range(3):
            cell = rows[r] + str(cols[c])
            gameBoard[cell] = nums[i]
            i = i + 1

    rowNums = nums.copy()
    rowNums[3:] = random.sample(rowNums[3:], len(rowNums[3:]))
   
    # Populate first row - A
    for c in cols:
        cell = rows[0] + str(c)
        gameBoard[cell] = rowNums[c - 1]

    nums.remove(gameBoard['A1'])
    nums.remove(gameBoard['B1'])
    nums.remove(gameBoard['C1'])
    colNums = list()
    colNums.append(gameBoard['A1'])
    colNums.append(gameBoard['B1'])
    colNums.append(gameBoard['C1'])
    colNums.extend(nums)
    colNums[3:] = random.sample(colNums[3:], len(colNums[3:]))

    # Populate first column - 1
    i = 0
    for r in rows:
        cell = r + str(cols[0])
        gameBoard[cell] = colNums[i]
        i = i + 1
    
    return gameBoard

def printBoardV(gameBoard):
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

def printBoardK(gameBoard):
    rowNr = 0

    for r in rows:
        for c in cols:
            if(rowNr != 0 and rowNr % 3 == 0):
                for i in cols:
                    print(' ——', end = '')
                    if(i == 9):
                        print()
                        rowNr = 0

                    elif(i % 3 == 0):
                        print(' +', end = '')
            cell = r + str(c)
            print(' ' + cell, end = '')

            if(c == 9):
                print()
                rowNr = rowNr + 1

            elif(c % 3 == 0):
                print(' |', end = '')
        
if __name__ == "__main__":
    # printTest()
    gameBoard = seedGame(generateBoard())
    
    # for n in rowMap:
    #     print(n, ': ', rowMap[n])
    # print()
    # for n in colMap:
    #     print(n, ': ', colMap[n])
    # print()
    # for n in boxMap:
    #     print(n, ': ', boxMap[n])
    printBoardK(gameBoard)
    print()
    printBoardV(gameBoard)
    # populateBoard(gameBoard)
    # if validateBoard(gameBoard) == 'err_size':
    #     print("err_size")
    #     exit 

    # prepBoard(gameBoard)
    
