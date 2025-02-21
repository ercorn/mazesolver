from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + (self._cell_size_x * j)
        cell_y1 = self._y1 + (self._cell_size_y * i)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)