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
        self.secondClick = False
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
        successfulMove = False
        
        if self.secondClick:
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

            self.secondClick = False
        else:
            if self.logicBoard[i][j] == 1:
                #valid piece
                self.prevI = i
                self.prevJ  = j
                self.secondClick = True
                print ("You clicked on cell (%s, %s)" % (i, j))
            else:
                print ("Not a cell with one of your pieces. Please select a different cell")

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