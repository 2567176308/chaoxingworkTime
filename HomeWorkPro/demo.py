import curses
import time

def animation(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    x = width // 2
    y = height // 2
    for i in range(10, 0, -1):
        stdscr.clear()
        stdscr.addstr(y, x - 5, "Loading...")
        stdscr.addstr(y + 1, x - i, "*" * (2 * i - 1))
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.clear()
    stdscr.addstr(y, x - 5, "Loading complete!")
    stdscr.refresh()
    time.sleep(2)

curses.wrapper(animation)