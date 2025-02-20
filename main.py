from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    a = Cell(win)
    a.draw(300, 300, 500, 500)

    b = Cell(win)
    b.draw(150, 150, 100, 100)

    a.draw_move(b)

    win.wait_for_close()


main()