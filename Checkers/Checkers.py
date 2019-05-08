from tkinter import Canvas, Tk
from itertools import product
import math

class Tree(object):
    def __init__(self, name='root', children=None, pointValue=0, controlBoard=[]):
        self.name = name
        self.children = []
        self.pointValue = pointValue
        self.controlBoard = controlBoard
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

class Board(Tk):
    def __init__(self, width, height, cellsize):
        Tk.__init__(self)
        self.cellsize = cellsize
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.bind("<Button-1>", self.onclick)
        self.canvas.pack()
        self.prevI = -1
        self.prevJ = -1
        self.overallK = 0
        self.secondClick = False
        #self.controlBoard = []
        self.logicBoard = [[0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
        self.controlBoard = [[0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
        self.masterTree = Tree('root', None, 0, [[0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]])
    def draw_rectangle(self, x1, y1, x2, y2, color):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    def draw_circle(self, x1, y1, x2, y2, color):
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")
    def repaint_board(self):
        for (i, j) in product(range(10), range(10)):
                          coordX1 = (i * size)
                          coordY1 = (j * size)
                          coordX2 = coordX1 + size
                          coordY2 = coordY1 + size
                          color = "white" if i%2 == j%2 else "black"
                          board.draw_rectangle(coordX1, coordY1, coordX2, coordY2, color)
                          cell = board.logicBoard[i][j]
                          if cell != 0 and (i != 0 or j != 0):
                            pawnColor = "red" if cell > 0 else "green"
                            board.draw_circle(coordX1, coordY1, coordX2, coordY2, pawnColor)
    def onclick(self, event):
        i = int(event.x / self.cellsize)
        j = int(event.y / self.cellsize)
        #successfulMove = False

        
        
        if self.secondClick:
            if self.isValidMove(True, self.prevI, self.prevJ, i, j, self.logicBoard):
                print("Successful move.")
                #repaint board
                
                if self.logicBoard[self.prevI][self.prevJ] == 2 or i == 0:
                    #piece is a king
                    self.logicBoard[i][j] = 2
                else:
                    #piece is standard
                    self.logicBoard[i][j] = 1
                self.logicBoard[self.prevI][self.prevJ] = 0
                if i == self.prevI + 2 and j == self.prevJ + 2:
                    self.logicBoard[self.prevI + 1][self.prevJ + 1] = 0
                elif i == self.prevI + 2 and j == self.prevJ - 2:
                    self.logicBoard[self.prevI + 1][self.prevJ - 1] = 0
                elif i == self.prevI - 2 and j == self.prevJ + 2:
                    self.logicBoard[self.prevI - 1][self.prevJ + 1] = 0
                elif i == self.prevI - 2 and j == self.prevJ - 2:
                    self.logicBoard[self.prevI - 1][self.prevJ - 1] = 0

                self.repaint_board()

                self.masterTree.controlBoard = self.copyBoardReturn(self.logicBoard)

                self.moveLayers(3, self.masterTree)

                self.checkLeafVals(self.masterTree)

                print(str(self.highestPointVal(self.masterTree, -math.inf)))

                #self.printTree(self.masterTree, 0)


                #print(self.masterTree.children[1].children[0].children[0].name)

                '''
                #generate move set for opponent and allow computer to move
                self.generatePossibleMoves(False, self.logicBoard, -50, self.masterTree)
                #print(self.overallK)
                prevK = 0
                prevprevK = 0


                #generates a total of 4 layers
                for j in range(3):
                    prevprevK = self.overallK
                    for i in range(prevK, self.overallK):
                        if j % 2 != 0:
                            print(self.controlBoard[i])
                            self.generatePossibleMoves(False, self.controlBoard[i], i)
                        else:
                            print(self.controlBoard[i])
                            self.generatePossibleMoves(True, self.controlBoard[i], i)
                    prevK = prevprevK

                print(self.overallK)

                masterTree = Tree('root', None, 0)
                for j in range(self.overallK):
                    t = Tree(j, None, 0)
                    for i in range(j + 1, self.overallK):
                        if(self.controlBoard[i][0][0] == j):
                            #control board is a child of control board j
                            t2 = Tree(i, None, 0)
                            t.add_child(t2)



                print(self.controlBoard[self.overallK - 1])
                '''
            else:
                print("Invalid move.")
 
            self.secondClick = False

        else:
            if self.logicBoard[i][j] > 0:
                #valid piece
                self.prevI = i
                self.prevJ  = j
                self.secondClick = True
                print ("You clicked on cell (%s, %s)" % (i, j))
            else:
                print ("Not a cell with one of your pieces. Please select a different cell")


    def checkLeafVals(self, treeToUse):
        if (len(treeToUse.children) == 0):
            treeToUse.pointValue = self.calcPoints(treeToUse.controlBoard)
        else:
            for i in range(len(treeToUse.children)):
                self.checkLeafVals(treeToUse.children[i])

    def highestPointVal(self, treeToUse, maxVal):
        if (len(treeToUse.children) == 0):
            return max(maxVal, treeToUse.pointValue)
        else:
            for i in range(len(treeToUse.children)):
                maxVal = max(self.highestPointVal(treeToUse.children[i], maxVal), maxVal)
            return maxVal
                    

    def printTree(self, treeToUse, layerNum):
        if (len(treeToUse.children) == 0):
            #print("layer num:" + str(layerNum))
            print("name:" + str(treeToUse.name))
            print("tree value:" + str(treeToUse.pointValue))
        else:
            for i in range(len(treeToUse.children)):         
                self.printTree(treeToUse.children[i], layerNum + 1)

    def calcPoints(self, logicBoard):
        points = 0
        for i in range(10):
            for j in range(10):
                if (logicBoard[i][j] == -2):
                    if (i == 0 or i == 9 or j == 0 or j == 9):
                        points += 4
                    else:
                        points += 3
                elif (logicBoard[i][j] == -1):
                    if (i == 0 or i == 0 or j == 0 or j == 9):
                        points += 2
                    else:
                        points += 1
                elif (logicBoard[i][j] == 1):
                    if (i == 0 or i == 0 or j == 0 or j == 9):
                        points -= 2
                    else:
                        points -= 1
                elif (logicBoard[i][j] == 2):
                    if (i == 0 or i == 9 or j == 0 or j == 9):
                        points -= 4
                    else:
                        points -= 3

        return points

    def moveLayers(self, numLayers, treeToUse):
        if numLayers == 0:
            print("end reached")
        else:
            if (numLayers % 2 != 0):
                self.generatePossibleMoves(False, treeToUse.controlBoard, treeToUse)
            else:
                self.generatePossibleMoves(True, treeToUse.controlBoard, treeToUse)
            for i in range(len(treeToUse.children)):
                self.moveLayers(numLayers - 1, treeToUse.children[i])

    def generatePossibleMoves(self, isPlayer, boardToUse, treeToUse):
        print(isPlayer)
        for i in range(10):
            for j in range(10):
                if (isPlayer and boardToUse[i][j] > 0) or (not isPlayer and boardToUse[i][j] < 0):
                    if i >= 2 and j >= 2 and self.isValidMove(isPlayer, i, j, i - 2, j - 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i - 2][j - 2] = self.controlBoard[i][j]                 
                        self.controlBoard[i][j] = 0
                        self.controlBoard[i - 1][j - 1] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i >= 1 and j >= 1 and self.isValidMove(isPlayer, i, j, i - 1, j - 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i - 1][j - 1] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 8 and j <= 8 and self.isValidMove(isPlayer, i, j, i + 1, j + 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i + 1][j + 1] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        t = Tree(self.overallK, None, 0, self.copyBoardReturn(self.controlBoard))
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 7 and j <= 7 and self.isValidMove(isPlayer, i, j, i + 2, j + 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i + 2][j + 2] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        self.controlBoard[i + 1][j + 1] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i >= 2 and j <= 7 and self.isValidMove(isPlayer, i, j, i - 2, j + 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i - 2][j + 2] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        self.controlBoard[i - 1][j + 1] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i >= 1 and j <= 8 and self.isValidMove(isPlayer, i, j, i - 1, j + 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i - 1][j + 1] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 8 and j >= 1 and self.isValidMove(isPlayer, i, j, i + 1, j - 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i + 1][j - 1] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 7 and j >= 2 and self.isValidMove(isPlayer, i, j, i + 2, j - 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[i + 2][j - 2] = self.controlBoard[i][j]
                        self.controlBoard[i][j] = 0
                        self.controlBoard[i + 1][j - 1] = 0
                        t = Tree(self.overallK, None, 0, self.controlBoard)
                        treeToUse.add_child(t)
                        self.overallK += 1


    '''
    def generatePossibleMoves(self, isPlayer, boardToUse, parentNum, treeToUse):
        print(isPlayer)
        for i in range(10):
            for j in range(10):
                if (isPlayer and boardToUse[i][j] > 0) or (not isPlayer and boardToUse[i][j] < 0):
                    if i >= 2 and j >= 2 and self.isValidMove(isPlayer, i, j, i - 2, j - 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 2][j - 2] = self.controlBoard[self.overallK][i][j]                 
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i - 1][j - 1] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i >= 1 and j >= 1 and self.isValidMove(isPlayer, i, j, i - 1, j - 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 1][j - 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 8 and j <= 8 and self.isValidMove(isPlayer, i, j, i + 1, j + 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 1][j + 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 7 and j <= 7 and self.isValidMove(isPlayer, i, j, i + 2, j + 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 2][j + 2] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i + 1][j + 1] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i >= 2 and j <= 7 and self.isValidMove(isPlayer, i, j, i - 2, j + 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 2][j + 2] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i - 1][j + 1] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i >= 1 and j <= 8 and self.isValidMove(isPlayer, i, j, i - 1, j + 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 1][j + 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 8 and j >= 1 and self.isValidMove(isPlayer, i, j, i + 1, j - 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 1][j - 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
                    if i <= 7 and j >= 2 and self.isValidMove(isPlayer, i, j, i + 2, j - 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 2][j - 2] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i + 1][j - 1] = 0
                        self.controlBoard[self.overallK][0][0] = parentNum
                        t = Tree(self.overallK, None, 0)
                        treeToUse.add_child(t)
                        self.overallK += 1
    '''

    def copyBoard(self, logicBoard):
        #self.controlBoard = logicBoard

        self.controlBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        '''
        self.controlBoard.append([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        '''
        for i in range(10):
            for j in range(10):
                self.controlBoard[i][j] = logicBoard[i][j]



    def copyBoardReturn(self, logicBoard):
        #self.controlBoard = logicBoard

        boardToReturn = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        '''
        self.controlBoard.append([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        '''
        for i in range(10):
            for j in range(10):
                boardToReturn[i][j] = logicBoard[i][j]

        return boardToReturn


    def isValidMove(self, isPlayer, i1, j1, i2, j2, boardToUse):
        successfulMove = False
        if boardToUse[i1][j1] == 0:
            return False
        elif boardToUse[i1][j1] > 0 and isPlayer:
            #player move
            if boardToUse[i1][j1] == 2:
                #piece is a king
                if i1 + 1 == i2 and (j1 + 1 == j2 or j1 - 1 == j2):
                    #possible standard move
                    if boardToUse[i2][j2] == 0:
                        #possible to move, update board

                        #self.logicBoard[i][j] = 2
                        #self.logicBoard[self.prevI][self.prevJ] = 0
                        #print("Successful move.")
                        successfulMove = True
                        #self.repaint_board()
                        return True
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 + 2 == i2 and j1 + 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 - 1][j2 - 1] < 0:
                            #possible to move, update board
                            
                            #self.logicBoard[i][j] = 2
                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i - 1][j + 1] = 0
                            #print("Successful move.")
                            successfulMove = True
                            #self.repaint_board()
                            return True
                        else:
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 + 2 == i2 and j1 - 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 - 1][j2 + 1] < 0:
                            #possible to move, update board

                            #self.logicBoard[i][j] = 2
                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i - 1][j - 1] = 0
                            #print("Successful move.")
                            successfulMove = True
                            #self.repaint_board()
                            return True
                        else:
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                #else:
                    #print("Invalid king move.")



            if not successfulMove:
                #piece is normal
                if i1 - 1 == i2 and (j1 + 1 == j2 or j1 - 1 == j2):
                    #possible standard move
                    if boardToUse[i2][j2] == 0:
                        #possible to move, update board

                        #if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                            #piece is king
                            #self.logicBoard[i][j] = 2
                            #print("King successful.")
                        #else:
                            #self.logicBoard[i][j] = 1

                        #self.logicBoard[self.prevI][self.prevJ] = 0
                        #print("Successful move.")
                        #self.repaint_board()
                        return True
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 - 2 == i2 and j1 + 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 + 1][j2 - 1] < 0:
                            #possible to move, update board
                            #if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                                #piece is king
                                #self.logicBoard[i][j] = 2
                                #print("King successful.")
                            #else:
                                #self.logicBoard[i][j] = 1

                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i + 1][j + 1] = 0
                            #print("Successful jump.")
                            #self.repaint_board()
                            return True
                        else:
                            #invalid move
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        #invalid move
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 - 2 == i2 and j1 - 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 + 1][j2 + 1] < 0:
                            #possible to move, update board
                            #if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                                #piece is king
                                #self.logicBoard[i][j] = 2
                                #print("King successful.")
                            #else:
                                #self.logicBoard[i][j] = 1

                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i + 1][j - 1] = 0
                            #print("Successful jump.")
                            #self.repaint_board()
                            return True
                        else:
                            #invalid move
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        #invalid move
                        return False
                        #print("Invalid move. Select starting piece again.")
                else:
                    #invalid move
                    return False
                    #print("Invalid move. Select starting piece again.")
        elif boardToUse[i1][j1] < 0 and not isPlayer:
            #computer move
            if boardToUse[i1][j1] == -2:
                #piece is a king
                if i1 - 1 == i2 and (j1 + 1 == j2 or j1 - 1 == j2):
                    #possible standard move
                    if boardToUse[i2][j2] == 0:
                        #possible to move, update board

                        #self.logicBoard[i][j] = 2
                        #self.logicBoard[self.prevI][self.prevJ] = 0
                        #print("Successful move.")
                        successfulMove = True
                        #self.repaint_board()
                        return True
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 - 2 == i2 and j1 + 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 + 1][j2 - 1] > 0:
                            #possible to move, update board
                            
                            #self.logicBoard[i][j] = 2
                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i - 1][j + 1] = 0
                            #print("Successful move.")
                            successfulMove = True
                            #self.repaint_board()
                            return True
                        else:
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 - 2 == i2 and j1 - 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 + 1][j2 + 1] > 0:
                            #possible to move, update board

                            #self.logicBoard[i][j] = 2
                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i - 1][j - 1] = 0
                            #print("Successful move.")
                            successfulMove = True
                            #self.repaint_board()
                            return True
                        else:
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                #else:
                    #print("Invalid king move.")



            if not successfulMove:
                #piece is normal
                if i1 + 1 == i2 and (j1 + 1 == j2 or j1 - 1 == j2):
                    #possible standard move
                    if boardToUse[i2][j2] == 0:
                        #possible to move, update board

                        #if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                            #piece is king
                            #self.logicBoard[i][j] = 2
                            #print("King successful.")
                        #else:
                            #self.logicBoard[i][j] = 1

                        #self.logicBoard[self.prevI][self.prevJ] = 0
                        #print("Successful move.")
                        #self.repaint_board()
                        return True
                    else:
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 + 2 == i2 and j1 + 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 - 1][j2 - 1] > 0:
                            #possible to move, update board
                            #if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                                #piece is king
                                #self.logicBoard[i][j] = 2
                                #print("King successful.")
                            #else:
                                #self.logicBoard[i][j] = 1

                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i + 1][j + 1] = 0
                            #print("Successful jump.")
                            #self.repaint_board()
                            return True
                        else:
                            #invalid move
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        #invalid move
                        return False
                        #print("Invalid move. Select starting piece again.")
                elif i1 + 2 == i2 and j1 - 2 == j2:
                    #possible jump
                    if boardToUse[i2][j2] == 0:
                        #possible to move, check for opponent in between
                        if boardToUse[i2 - 1][j2 + 1] > 0:
                            #possible to move, update board
                            #if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                                #piece is king
                                #self.logicBoard[i][j] = 2
                                #print("King successful.")
                            #else:
                                #self.logicBoard[i][j] = 1

                            #self.logicBoard[self.prevI][self.prevJ] = 0
                            #self.logicBoard[i + 1][j - 1] = 0
                            #print("Successful jump.")
                            #self.repaint_board()
                            return True
                        else:
                            #invalid move
                            return False
                            #print("Invalid move. Select starting piece again.")
                    else:
                        #invalid move
                        return False
                        #print("Invalid move. Select starting piece again.")
                else:
                    #invalid move
                    return False
                    #print("Invalid move. Select starting piece again.")
        else:
            return False


if __name__=="__main__":
    size = 40
    board = Board(400, 400, size)
    board.title("Checkers")
    for (i, j) in product(range(10), range(10)):
                          coordX1 = (i * size)
                          coordY1 = (j * size)
                          coordX2 = coordX1 + size
                          coordY2 = coordY1 + size
                          color = "white" if i%2 == j%2 else "black"
                          board.draw_rectangle(coordX1, coordY1, coordX2, coordY2, color)
                          cell = board.logicBoard[i][j]
                          if cell != 0:
                            pawnColor = "red" if cell > 0 else "green"
                            board.draw_circle(coordX1, coordY1, coordX2, coordY2, pawnColor)
    board.mainloop()