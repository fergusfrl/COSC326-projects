#Python 2.7.13
#Etude6: part1 - Recursive
#Fergus Farrell
from Tkinter import *


def delete(x, y, size):
    window.create_rectangle(x+size, y+size, x+size*2, y+size*2, fill = "white", width = 0)


def drawFrac(n, x, y, size):
    k = n - 1
    if (n < 0):
        return
    newSize = size / 3
    delete(x, y, newSize)
    drawFrac(k, x, y, newSize)
    drawFrac(k, x + newSize, y, newSize)
    drawFrac(k, x + newSize * 2, y, newSize)
    drawFrac(k, x, y + newSize, newSize)
    drawFrac(k, x + newSize * 2, y + newSize, newSize)
    drawFrac(k, x, y + newSize * 2, newSize)
    drawFrac(k, x + newSize, y + newSize * 2, newSize)
    drawFrac(k, x + newSize * 2, y + newSize * 2, newSize)


base = Tk()
startingSize = 800
canvasSize = 800
genNum = int(sys.argv[1])
window = Canvas(base, width=canvasSize, height=canvasSize)

window.pack()
window.create_rectangle(0, 0, canvasSize, canvasSize, fill = "blue", width = 0)
drawFrac(genNum, 0, 0, startingSize)
base.mainloop()