#Python 2.7.13
#Etude6: part1 - Iterative
#Fergus Farrell
from Tkinter import *

def delete(x, y, size):
    window.create_rectangle(size+x, size+y, x+size*2, y+size*2, fill="white", width=0)
        
def fractalSquares(n, size):
    x = 0
    x_count = 3**n
    y = 0
    while (n >= 0):
        removals = 3**(n*2)
        newSize = size/3**(n+1)
        if removals == 1:
            newSize = size/3
        while removals > 0:
            if x >= size or x_count < 0:
                y = (y+(newSize*3)) % size
                x = 0
                if(n != 0):
                    x_count = 3**n
            else:
                x_count = x_count-1
                if x_count >= 0:
                    delete(x, y, newSize)
                    x = (x+(newSize*3))
                    removals = removals-1
        x = 0
        x_count = 3**n
        y = 0
        n = n-1

root = Tk()
genNum = int(sys.argv[1])
size = 800
c_size = 800
window = Canvas(root, width=c_size, height=c_size)

window.pack()
window.create_rectangle(0, 0, size, size, fill="blue", width=0)
fractalSquares(genNum, size)
root.mainloop()