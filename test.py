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
    height = 15; width = 35
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
        elif inp == ord('g'):
            stdscr.refresh()

            win.bkgd(curses.COLOR_BLACK)

            win.clear()
            win.erase()

            win.addstr(0,0,"      _.-'''''-._", RIB)
            win.addstr(1,0,"    .'  _     _  '.", RIB)
            win.addstr(2,0,"   /   (_)   (_)   \\", RIB)
            win.addstr(3,0,"  |  ,           ,  |", RIB)
            win.addstr(4,0,"  |  \\`.       .`/  |", RIB)
            win.addstr(5,0,"   \\  '.`'\"\"'\"`.'  /", RIB)
            win.addstr(6,0,"    '.  `'---'`  .'", RIB)
            win.addstr(7,0,"jgs   '-._____.-'", RIB)

            win.refresh()

        elif inp == ord('j') or inp == curses.KEY_DOWN or inp == ord('k') or inp == curses.KEY_UP:
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