from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    #win = Window(800, 600)

    #a = Cell(win)
    #a.draw(300, 300, 500, 500)

    #b = Cell(win)
    #b.draw(150, 150, 100, 100)

    #a.draw_move(b)

    #test_maze = Maze(0, 0, 5, 5, 50, 50, win)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    win.wait_for_close()


main()