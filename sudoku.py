import random
import math
import time

cols = list(range(1, 10))
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

peerMap = {}
colMap = {}
rowMap = {}
boxMap = {n: [] for n in range(1, 10)}

# got this online somewhere because I wanted to print in place
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

def possibleVals(cell):
    vals = list(range(1, 10))

    for c in peerMap[cell]:
        if gameBoard[c] in vals:
            vals.remove(gameBoard[c])
        # print(gameBoard[c])
        # pass
    random.shuffle(vals)
    print(vals)
    return vals

def peerVals(cell):
    vals = []
    for c in peerMap[cell]:
        vals.append(gameBoard[c])
    
    vals = set(vals)
    return vals

def fullBoard(gameBoard):
    for c in gameBoard:
        if gameBoard[c] == 0:
            return False

    return True

def fillBoard(gameBoard):
    nums = list(range(1, 10))
    
    for cell in gameBoard:
        if gameBoard[cell] == 0:
            random.shuffle(nums)
            for n in nums:
                if n not in peerVals(cell):
                    gameBoard[cell] = n

                    if fullBoard(gameBoard):
                        return True
                    elif fillBoard(gameBoard):
                        return True
            break


def printBoardNums(gameBoard):
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
                print("\t%c" %r, end = '')

            if(c == 9):
                print()
                rowNr = rowNr + 1

            elif(c % 3 == 0):
                print(' |', end = '')
            

def printBoardKeys(gameBoard):
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
    gameBoard = generateBoard()
    
    # for n in rowMap:
    #     print(n, ': ', rowMap[n])
    # print()
    # for n in colMap:
    #     print(n, ': ', colMap[n])
    # print()
    # for n in boxMap:
    #     print(n, ': ', boxMap[n])
    # print()
    # for n in peerMap:
    #     print(n, ': ', peerMap[n])

    printBoardKeys(gameBoard)
    print()
    fillBoard(gameBoard)
    while not fullBoard(gameBoard):
        gameBoard = generateBoard()
        fillBoard(gameBoard)

    printBoardNums(gameBoard)
    
