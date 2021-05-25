#John Conway's Game of Life
from graphics import *
import time
import random
from pprint import pprint

class Cell:
    def __init__(self,cell,neighbors):
        self.cell = cell
        self.neighbors = neighbors

    def livesordies(self):
        counter = 0
        for i in self.neighbors:
            if i == True:
                counter+=1
        if self.cell == True:
            if (counter < 2):
                self.cell = False
            elif (counter==2 or counter==3):
                self.cell = True
            elif (counter > 3):
                self.cell = False
        elif self.cell == False:
            if counter == 3:
                self.cell = True
        return(self.cell)

def main():
    win  = GraphWin("Game of Life", 1001,1001)
    window = GraphWin("Menu", 400,400)
    win.setBackground(color_rgb(0,0,0))
    window.setBackground(color_rgb(0,0,0))
    x = 0
    y = 0
    for i in range(0,51):
        line = Line(Point(x,0),Point(x,1000))
        line.setWidth(1)
        line.setFill(color_rgb(255,255,255))
        line.draw(win)
        lines = Line(Point(0,y),Point(1000,y))
        lines.setWidth(1)
        lines.setFill(color_rgb(255,255,255))
        lines.draw(win)
        x+=20               #each cell is 18x18
        y+=20
    list_of_cells = []
    yy = 1
    yyy = 19
    for i in range(50):
        sample_list = []
        xx = 1
        xxx = 19
        for j in range(50):
            sample_list.append(Rectangle(Point(xx,yy),Point(xxx,yyy)))
            xx += 20
            xxx += 20
        yy += 20
        yyy += 20
        list_of_cells.append(sample_list)

    live_cells = []
    while True:
        clickpoint = win.checkMouse()
        to_start = window.checkMouse()
        if clickpoint != None:
            for i in range(50):
                for j in range(50):
                    if inside(clickpoint,list_of_cells[j][i]):
                        live_cells.append(list_of_cells[j][i])
                        k = list_of_cells[j][i]
                        k.setFill(color_rgb(0,255,0))
                        k.draw(win)
        if to_start!= None:
            # time.sleep(0.5)
            if inside(to_start,Rectangle(Point(0,0),Point(399,399))):
                for i in live_cells:
                    i.undraw()
                # time.sleep(0.5)

                for i in range(25000):
                    sim = simulating(live_cells,list_of_cells)
                    # copy = [i for i in sim]
                    for x in live_cells:
                        x.undraw()
                    # time.sleep(0.5)
                    for x in sim:
                        live_cells = [i for i in sim]
                        x.setFill(color_rgb(0,255,0))
                        x.draw(win)
                    copy = [i for i in sim]
                    time.sleep(0.1)
    win.close()
    window.close()

def simulating(live_cells,all_cells):
    to_return = []
    for i in range(0,49):
        for j in range(0,49):
            x = all_cells[j][i]
            state = False
            neighbors = []
            if all_cells[j][i] in live_cells:
                state = True
            temp_neighbors = [all_cells[j-1][i-1],all_cells[j-1][i],all_cells[j-1][i+1],all_cells[j][i-1],all_cells[j][i+1],all_cells[j+1][i-1],all_cells[j+1][i],all_cells[j+1][i+1]]
            for counter in temp_neighbors:
                if counter in live_cells:
                    neighbors.append(True)
                else:
                    neighbors.append(False)
            x = Cell(state,neighbors)
            if x.livesordies() == True:
                to_return.append(all_cells[j][i])
    return to_return            #list of cells alive in next generation

def inside(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


main()
