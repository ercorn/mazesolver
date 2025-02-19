from graphics import Window, Point, Line

def main():
    win = Window(800, 600)

    line = Line(Point(100, 10), Point(300, 200))
    win.draw_line("black", line)

    win.wait_for_close()


main()