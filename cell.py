from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.__x1 = None
        self.__x2 = None
        self.__y2 = None
        self.__y1 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray"
        if undo:
            fill_color = "red"
        line = Line(
                    Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2), 
                    Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)
                    )
        self.__win.draw_line(line, fill_color)
