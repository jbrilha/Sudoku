import math
import os
import sys
import random
import time
# import pygame
# from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GREY = (200, 200, 200)
DARK_GREY = (50, 50, 50)

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 450
CELL_SIZE = 30
BOX_SIZE = CELL_SIZE * 3
# DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)


def clear():
    os.system("clear")


cols = list(range(1, 10))
rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

peerMap = {}
colMap = {}
rowMap = {}
boxMap = {n: [] for n in range(1, 10)}


class Cell:
    def __init__(self, coords, num):
        self.coords = coords
        self.num = num


class Difficulty:
    def __init__(self, name, hints):
        self.name = name
        self.hints = hints


test = Difficulty("test", 80)
easy = Difficulty("Easy", 38)
medium = Difficulty("Medium", 30)
hard = Difficulty("Hard", 25)
expert = Difficulty("Expert", 22)
master = Difficulty("Master", 17)


# def drawBox(left, top):
#     fontSize = 40
#     font = pygame.font.SysFont(None, fontSize)
#
#     img = font.render("8", True, RED)
#
#     for i in range(3):
#         for j in range(3):
#             gridCoords = (left + j * CELL_SIZE, top + i * CELL_SIZE)
#             numCoords = (left + j * CELL_SIZE + 7, top + i * CELL_SIZE + 3)
#             dimensions = (CELL_SIZE, CELL_SIZE)
#
#             grid = pygame.Rect(gridCoords, dimensions)
#
#             pygame.draw.rect(DISPLAY, GREY, grid, 0)  # Used for the cells
#             pygame.draw.rect(DISPLAY, DARK_GREY, grid, 1)  # Used for the grid
#             DISPLAY.blit(img, numCoords)
#
#     box = pygame.Rect(
#         left,
#         top,
#         BOX_SIZE,
#         BOX_SIZE,
#     )
#     pygame.draw.rect(DISPLAY, BLACK, box, 2)


# def drawBoard():
#     # for width in range(5):
#     #     for height in range(5):
#     #         drawCells(width, height)
#     for i in range(3):  # Cols
#         for j in range(3):  # Rows
#             drawBox(
#                 i * BOX_SIZE + (WINDOW_WIDTH - BOX_SIZE * 3) / 2,
#                 j * BOX_SIZE + BOX_SIZE,
#             )


# def gameMain():
#     pygame.init()
#     pygame.display.set_caption("Sudoku - Difficulty")
#     sysfont = pygame.font.get_default_font()
#     # print('system font :', sysfont)
#
#     DISPLAY.fill(WHITE)
#
#     while True:
#         drawBoard()
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()


# got this online somewhere because I wanted to print in place
def printTest():
    for i in range(101):
        # time.sleep(0.01)
        print("Downloading File FooFile.txt [%d%%]\r" % i, end="")


def splitKey(key):
    row = key[:1]
    col = key[1:]

    return row, col


def setPeers(emptyBoard):
    for n in emptyBoard:
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
    emptyBoard = {}

    for r in rows:
        rowSet = []
        if r == "A" or r == "B" or r == "C":
            box = 1
        if r == "D" or r == "E" or r == "F":
            box = 4
        if r == "G" or r == "H" or r == "I":
            box = 7

        for c in cols:
            if c == 4 or c == 7:
                box = box + 1

            cell = r + str(c)
            emptyBoard[cell] = "·"
            boxMap[box].append(cell)
            rowSet.append(cell)

        rowMap[r] = rowSet

    for c in cols:
        colSet = []
        for r in rows:
            cell = r + str(c)
            colSet.append(cell)

        colMap[c] = colSet

    setPeers(emptyBoard)
    return emptyBoard


def peerVals(cell):
    vals = []
    for c in peerMap[cell]:
        vals.append(solutionBoard[c])

    vals = set(vals)
    return vals


def fullBoard(solutionBoard):
    for c in solutionBoard:
        if solutionBoard[c] == "·":
            return False

    return True


def fillBoard(solutionBoard):
    nums = list(range(1, 10))

    for cell in solutionBoard:
        if solutionBoard[cell] == "·":
            random.shuffle(nums)
            for n in nums:
                if n not in peerVals(cell):
                    solutionBoard[cell] = n

                    if fullBoard(solutionBoard):
                        return True
                    elif fillBoard(solutionBoard):
                        return True
            break


def clearCells(solutionBoard, difficulty):
    fullCells = list(solutionBoard.keys())
    gameBoard = solutionBoard.copy()

    while len(fullCells) > difficulty.hints:
        cell = random.choice(fullCells)
        gameBoard[cell] = "·"
        fullCells.remove(cell)

    return gameBoard


def printBoardNums():
    rowNr = 0

    for c in cols:
        print("", c, end="")
        if c == 3 or c == 6:
            print(" |", end="")

    print("\n")
    for r in rows:
        for c in cols:
            if rowNr != 0 and rowNr % 3 == 0:
                for i in cols:
                    print(" —", end="")
                    if i == 9:
                        print("\t —")
                        rowNr = 0

                    elif i % 3 == 0:
                        print(" +", end="")

            cell = r + str(c)
            print(" " + str(gameBoard[cell]), end="")

            if c == 9:
                print("\t %s" % r)
                rowNr = rowNr + 1

            elif c % 3 == 0:
                print(" |", end="")


def printBoardKeys():
    rowNr = 0

    for r in rows:
        for c in cols:
            if rowNr != 0 and rowNr % 3 == 0:
                for i in cols:
                    print(" ——", end="")
                    if i == 9:
                        print()
                        rowNr = 0

                    elif i % 3 == 0:
                        print(" +", end="")
            cell = r + str(c)
            print(" " + cell, end="")

            if c == 9:
                print()
                rowNr = rowNr + 1

            elif c % 3 == 0:
                print(" |", end="")


def startMenu():
    print("Select difficulty or press 'Q' to quit!")
    print("\t1. Easy")
    print("\t2. Medium")
    print("\t3. Hard")
    print("\t4. Expert")
    print("\t5. Master")

    inp = input()
    match inp.upper():
        case "0":
            difficulty = test
        case "1":
            difficulty = easy
        case "2":
            difficulty = medium
        case "3":
            difficulty = hard
        case "4":
            difficulty = expert
        case "5":
            difficulty = master
        case "Q":
            exit()

    clear()
    return difficulty


def debug(board):
    clear()
    print("board")
    for n in board:
        print(n + ":", board[n], end=' | ')
    input()
    clear()
    print("rowMap")
    for n in rowMap:
        print(n, ": ", rowMap[n])
    input()
    clear()
    print("colMap")
    for n in colMap:
        print(n, ": ", colMap[n])
    input()
    clear()
    print("boxMap")
    for n in boxMap:
        print(n, ": ", boxMap[n])
    input()
    clear()
    print("peerMap")
    for n in peerMap:
        print(n, ": ", peerMap[n])
    input()
    clear()
    # printBoardNums(clearCells(solutionBoard, easy))
    # input()
    # printBoardNums(clearCells(solutionBoard, medium))
    # input()
    # printBoardNums(clearCells(solutionBoard, hard))
    # input()
    # printBoardNums(clearCells(solutionBoard, expert))
    # input()
    # printBoardNums(clearCells(solutionBoard, master))
    # input()
def checkNum(cell, num):
    if gameBoard[cell] != "·":
        return True

    if solutionBoard[cell] == num:
        gameBoard[cell] = num
        return True
    else:
        return False


def play():
    mistakes = 0
    victory = False
    while not victory:
        clear()
        print(difficulty.name, '||', '%d / 3 Mistakes'%mistakes)
        printBoardNums()

        if mistakes == 3:
            break 
        if fullBoard(gameBoard):
            victory = True
            break

        cell, num = input("\n[CELL:NUM]: ").split(':')
        
        if not checkNum(cell, int(num)):
            mistakes = mistakes + 1
    if victory:
        print("\nYOU WON!!")
    else:
        print("\nyou suck at this")


if __name__ == "__main__":
    solutionBoard = generateBoard()
    # debug(solutionBoard)
    difficulty = startMenu()

    # printBoardKeys(solutionBoard)
    # print()
    fillBoard(solutionBoard)
    while not fullBoard(solutionBoard):
        solutionBoard = generateBoard()
        fillBoard(solutionBoard)

    gameBoard = clearCells(solutionBoard, difficulty)
    
    play()
    
    # gameMain()
