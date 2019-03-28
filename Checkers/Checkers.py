from tkinter import Canvas, Tk
from itertools import product

class Board(Tk):
    def __init__(self, width, height, cellsize):
        Tk.__init__(self)
        self.cellsize = cellsize
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.bind("<Button-1>", self.onclick)
        self.canvas.pack()
    def draw_rectangle(self, x1, y1, x2, y2, color):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    def draw_circle(self, x1, y1, x2, y2, color):
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")
    def onclick(self, event):
        i = int(event.x / self.cellsize)
        j = int(event.y / self.cellsize)
        print ("You clicked on cell (%s, %s)" % (i, j))

if __name__=="__main__":
    size = 40
    board = Board(400, 400, size)
    board.title("Checkers")
    logicBoard = [[0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
    for (i, j) in product(range(10), range(10)):
                          coordX1 = (i * size)
                          coordY1 = (j * size)
                          coordX2 = coordX1 + size
                          coordY2 = coordY1 + size
                          color = "white" if i%2 == j%2 else "black"
                          board.draw_rectangle(coordX1, coordY1, coordX2, coordY2, color)
                          cell = logicBoard[i][j]
                          if cell != 0:
                            pawnColor = "red" if cell > 0 else "blue"
                            board.draw_circle(coordX1, coordY1, coordX2, coordY2, pawnColor)
    board.mainloop()