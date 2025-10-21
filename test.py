import curses
from curses import wrapper
import time

def main(stdscr):
    # Get the maximum rows and columns of the *physical screen*
    max_row, max_col = stdscr.getmaxyx()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    RIB = curses.color_pair(1)
    BIR = curses.color_pair(2)

    # stdscr.addstr(10, 10, "Hello", curses.A_BOLD)

    begin_x = 0; begin_y = 0
    height = 5; width = 20
    win = curses.newwin(height, width, begin_y, begin_x)

    options = ["Hello", "World", "Type shit"]

    select_index = 0

    for i in range(0, len(options)):
        selected_indicator = ""

        if i == select_index % len(options):
            selected_indicator = "> "
        
        win.addstr(selected_indicator + options[i] + " \n", RIB)

    stdscr.refresh() # main screen must be refreshed before sub window avoiding overlapping type shit

    win.bkgd(' ', BIR)
    
    win.refresh()

    while(True):
        inp = stdscr.getch()
        if inp == ord('q'):
            break
        else:
            if inp == ord('j') or inp == curses.KEY_DOWN:
                if select_index < len(options) - 1:
                    select_index += 1
            elif inp == ord('k') or inp == curses.KEY_UP:
                if select_index > 0:
                    select_index -= 1

            win.clear()

            for i in range(0, len(options)):
                selected_indicator = ""

                if i == select_index:
                    selected_indicator = "> "

                win.addstr(selected_indicator + options[i] + "\n", RIB)
                win.refresh()
            
            continue



wrapper(main)