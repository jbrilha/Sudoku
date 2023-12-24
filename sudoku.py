import random
import math

def generateBoard():
    cols = list(range(1, 10))
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    rowNr = 0

    boardMap = {}
    
    print()
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
            boardMap[cell] = math.ceil(random.random() * len(cols))
            print(' ' + cell + ' ' + str(boardMap[cell]), end = '')

            if(c == 9):
                print()
                rowNr = rowNr + 1

            elif(c % 3 == 0):
                print(' |', end = '')

    rowNr = 0
    print(math.ceil(random.random() * len(cols)))
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
            print(' ' + cell + ': ' + str(boardMap[cell]), end = '')
            # print(' ' + str(math.ceil(random.random() * len(cols))), end = '')
            if(c == 9):
                print()
                rowNr = rowNr + 1

            elif(c % 3 == 0):
                print(' |', end = '')
            

if __name__ == "__main__":
    generateBoard()

