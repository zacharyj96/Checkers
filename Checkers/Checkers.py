from tkinter import Canvas, Tk
from itertools import product

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
        self.controlBoard = []
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
                          if cell != 0:
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
                self.logicBoard[self.prevI][self.prevJ] = 0
                if self.logicBoard[i][j] == 2 or i == 0:
                    #piece is a king
                    self.logicBoard[i][j] = 2
                else:
                    #piece is standard
                    self.logicBoard[i][j] = 1
                if i == self.prevI + 2 and j == self.prevJ + 2:
                    self.logicBoard[self.prevI + 1][self.prevJ + 1] = 0
                elif i == self.prevI + 2 and j == self.prevJ - 2:
                    self.logicBoard[self.prevI + 1][self.prevJ - 1] = 0
                elif i == self.prevI - 2 and j == self.prevJ + 2:
                    self.logicBoard[self.prevI - 1][self.prevJ + 1] = 0
                elif i == self.prevI - 2 and j == self.prevJ - 2:
                    self.logicBoard[self.prevI - 1][self.prevJ - 1] = 0

                self.repaint_board()
            else:
                print("Invalid move.")
            '''
            if self.logicBoard[i][j] == 2:
                #piece is a king
                if i - 1 == self.prevI and (j + 1 == self.prevJ or j - 1 == self.prevJ):
                    #possible standard move
                    if self.logicBoard[i][j] == 0:
                        #possible to move, update board
                        self.logicBoard[i][j] = 2
                        self.logicBoard[self.prevI][self.prevJ] = 0
                        print("Successful move.")
                        successfulMove = True
                        self.repaint_board()
                    else:
                        print("Invalid move. Select starting piece again.")
                elif i - 2 == self.prevI and j + 2 == self.prevJ:
                    #possible jump
                    if self.logicBoard[i][j] == 0:
                        #possible to move, check for opponent in between
                        if self.logicBoard[i - 1][j + 1] < 0:
                            #possible to move, update board
                            
                            self.logicBoard[i][j] = 2
                            self.logicBoard[self.prevI][self.prevJ] = 0
                            self.logicBoard[i - 1][j + 1] = 0
                            print("Successful move.")
                            successfulMove = True
                            self.repaint_board()
                        else:
                            print("Invalid move. Select starting piece again.")
                    else:
                        print("Invalid move. Select starting piece again.")
                elif i - 2 == self.prevI and j - 2 == self.prevJ:
                    #possible jump
                    if self.logicBoard[i][j] == 0:
                        #possible to move, check for opponent in between
                        if self.logicBoard[i - 1][j - 1] < 0:
                            #possible to move, update board

                            self.logicBoard[i][j] = 2
                            self.logicBoard[self.prevI][self.prevJ] = 0
                            self.logicBoard[i - 1][j - 1] = 0
                            print("Successful move.")
                            successfulMove = True
                            self.repaint_board()
                        else:
                            print("Invalid move. Select starting piece again.")
                    else:
                        print("Invalid move. Select starting piece again.")
                else:
                    print("Invalid king move.")



            if not successfulMove:
                #piece is normal
                if i + 1 == self.prevI and (j + 1 == self.prevJ or j - 1 == self.prevJ):
                    #possible standard move
                    if self.logicBoard[i][j] == 0:
                        #possible to move, update board
                        if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                            #piece is king
                            self.logicBoard[i][j] = 2
                            print("King successful.")
                        else:
                            self.logicBoard[i][j] = 1

                        self.logicBoard[self.prevI][self.prevJ] = 0
                        print("Successful move.")
                        self.repaint_board()
                    else:
                        print("Invalid move. Select starting piece again.")
                elif i + 2 == self.prevI and j + 2 == self.prevJ:
                    #possible jump
                    if self.logicBoard[i][j] == 0:
                        #possible to move, check for opponent in between
                        if self.logicBoard[i + 1][j + 1] < 0:
                            #possible to move, update board
                            if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                                #piece is king
                                self.logicBoard[i][j] = 2
                                print("King successful.")
                            else:
                                self.logicBoard[i][j] = 1

                            self.logicBoard[self.prevI][self.prevJ] = 0
                            self.logicBoard[i + 1][j + 1] = 0
                            print("Successful jump.")
                            self.repaint_board()
                        else:
                            #invalid move
                            print("Invalid move. Select starting piece again.")
                    else:
                        #invalid move
                        print("Invalid move. Select starting piece again.")
                elif i + 2 == self.prevI and j - 2 == self.prevJ:
                    #possible jump
                    if self.logicBoard[i][j] == 0:
                        #possible to move, check for opponent in between
                        if self.logicBoard[i + 1][j - 1] < 0:
                            #possible to move, update board
                            if i == 0 or self.logicBoard[self.prevI][self.prevJ] == 2:
                                #piece is king
                                self.logicBoard[i][j] = 2
                                print("King successful.")
                            else:
                                self.logicBoard[i][j] = 1

                            self.logicBoard[self.prevI][self.prevJ] = 0
                            self.logicBoard[i + 1][j - 1] = 0
                            print("Successful jump.")
                            self.repaint_board()
                        else:
                            #invalid move
                            print("Invalid move. Select starting piece again.")
                    else:
                        #invalid move
                        print("Invalid move. Select starting piece again.")
                else:
                    #invalid move
                    print("Invalid move. Select starting piece again.")
            '''
            self.secondClick = False
            self.generatePossibleMoves(True, self.logicBoard)
            print(self.overallK)
            prevK = 0
            prevprevK = 0

            for j in range(4):
                prevprevK = self.overallK
                for i in range(prevK, self.overallK):
                    if j % 2 != 0:
                        self.generatePossibleMoves(True, self.controlBoard[i])
                    else:
                        self.generatePossibleMoves(False, self.controlBoard[i])
                prevK = prevprevK

            print(self.overallK)

            #print(self.overallK)
        else:
            if self.logicBoard[i][j] > 0:
                #valid piece
                self.prevI = i
                self.prevJ  = j
                self.secondClick = True
                print ("You clicked on cell (%s, %s)" % (i, j))
            else:
                print ("Not a cell with one of your pieces. Please select a different cell")


    def generatePossibleMoves(self, isPlayer, boardToUse):
        print(isPlayer)
        for i in range(10):
            for j in range(10):
                if (isPlayer and boardToUse[i][j] > 0) or (not isPlayer and boardToUse[i][j] < 0):
                    if i >= 2 and j >= 2 and self.isValidMove(isPlayer, i, j, i - 2, j - 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 2][j - 2] = self.controlBoard[self.overallK][i][j]                 
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i - 1][j - 1] = 0
                        self.overallK += 1
                    if i >= 1 and j >= 1 and self.isValidMove(isPlayer, i, j, i - 1, j - 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 1][j - 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.overallK += 1
                    if i <= 8 and j <= 8 and self.isValidMove(isPlayer, i, j, i + 1, j + 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 1][j + 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.overallK += 1
                    if i <= 7 and j <= 7 and self.isValidMove(isPlayer, i, j, i + 2, j + 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 2][j + 2] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i + 1][j + 1] = 0
                        self.overallK += 1
                    if i >= 2 and j <= 7 and self.isValidMove(isPlayer, i, j, i - 2, j + 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 2][j + 2] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i - 1][j + 1] = 0
                        self.overallK += 1
                    if i >= 1 and j <= 8 and self.isValidMove(isPlayer, i, j, i - 1, j + 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i - 1][j + 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.overallK += 1
                    if i <= 8 and j >= 1 and self.isValidMove(isPlayer, i, j, i + 1, j - 1, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 1][j - 1] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.overallK += 1
                    if i <= 7 and j >= 2 and self.isValidMove(isPlayer, i, j, i + 2, j - 2, boardToUse):
                        self.copyBoard(boardToUse)
                        self.controlBoard[self.overallK][i + 2][j - 2] = self.controlBoard[self.overallK][i][j]
                        self.controlBoard[self.overallK][i][j] = 0
                        self.controlBoard[self.overallK][i + 1][j - 1] = 0
                        self.overallK += 1

    def copyBoard(self, logicBoard):
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
        for i in range(10):
            for j in range(10):
                self.controlBoard[self.overallK][i][j] = logicBoard[i][j]


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

    def calcPoints(self, logicBoard):
        points = 0
        xcounter = 0
        # Loop through the board
        for x in logicBoard:
            counter = 0
            for y in x:
                # AI Non-King
                if y == -1:
                    # Edge Piece
                    if counter == 0 or counter == 9 or xcounter == 0 or xcounter == 9:
                        points += 2
                    else:
                        points += 1
                # AI King
                elif y == -2:
                    # Edge Piece
                    if counter == 0 or counter == 9 or xcounter == 0 or xcounter == 9:
                        points += 4
                    else:
                        points += 3
                # Player Non-King
                elif y == 1:
                    # Edge Piece
                    if counter == 0 or counter == 9 or xcounter == 0 or xcounter == 9:
                        points -= 2
                    else:
                        points -= 1
                # Player King
                elif y == 2:
                    # Edge Piece
                    if counter == 0 or counter == 9 or xcounter == 0 or xcounter == 9:
                        points -= 4
                    else:
                        points -= 3
                counter += 1
            xcounter += 1
        return points






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