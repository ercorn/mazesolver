from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self._x1 + (self._cell_size_x * i)
        cell_y1 = self._y1 + (self._cell_size_y * j)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #Check the cells that are directly adjacent to the current cell. 
            # Keep track of any that have not been visited as "possible directions" to move to
            if i > 0 and not self._cells[i - 1][j].visited: #right side: is not leftmost and more exist rightward
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited: #left side: is not rightmost and more exist leftward
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited: #upwards: is not topmost and more exist downward
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited: #downwards: is not downmost and more exist upward
                to_visit.append((i, j + 1))

            #If there are zero directions you can go from the current cell, then draw the current cell and return
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            #Otherwise, pick a random direction
            next_dir_idx = to_visit[random.randrange(len(to_visit))]

            #Knock down the walls between the current cell and the chosen cell
            #left
            if next_dir_idx[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False            
            #right
            if next_dir_idx[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            #up
            if next_dir_idx[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False            
            #down
            if next_dir_idx[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            #Move to the chosen cell by recursively calling _break_walls_r
            self._break_walls_r(next_dir_idx[0], next_dir_idx[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        curr_cell = self._cells[i][j]
        #left
        
        if i > 0 and not curr_cell.has_left_wall and not self._cells[i - 1][j].visited:
            to_cell = self._cells[i - 1][j]
            curr_cell.draw_move(to_cell)
            if self._solve_r(i - 1, j):
                return True
            else:
                curr_cell.draw_move(to_cell, undo=True)
        #right
        
        if i < self._num_cols - 1  and not curr_cell.has_right_wall and not self._cells[i + 1][j].visited:
            to_cell = self._cells[i + 1][j]
            curr_cell.draw_move(to_cell)
            if self._solve_r(i + 1, j):
                return True
            else:
                curr_cell.draw_move(to_cell, undo=True)
        #up
        
        if j > 0 and not curr_cell.has_top_wall and not self._cells[i][j - 1].visited:
            to_cell = self._cells[i][j - 1]
            curr_cell.draw_move(to_cell)
            if self._solve_r(i, j - 1):
                return True
            else:
                curr_cell.draw_move(to_cell, undo=True)
        #down
        
        if j < self._num_rows - 1 and not curr_cell.has_bottom_wall and not self._cells[i][j + 1].visited:
            to_cell = self._cells[i][j + 1]
            curr_cell.draw_move(to_cell)
            if self._solve_r(i, j + 1):
                return True
            else:
                curr_cell.draw_move(to_cell, undo=True)
        #if none of the directions worked out
        return False