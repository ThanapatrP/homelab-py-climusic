import curses
from curses import wrapper
import time

def main(stdscr):
    # Get the maximum rows and columns of the *physical screen*
    max_row, max_col = stdscr.getmaxyx()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_YELLOW)

    BNR = curses.color_pair(1)
    BNY = curses.color_pair(2)

    pad = curses.newpad(1, 15)
    stdscr.refresh()

    pad.addstr("HelloWorld")

# Define the screen display area dynamically
    pminrow = 0   # Start at the top of the pad
    pmincol = 0   # Start at the left of the pad
    
    sminrow = 5   # Top-left screen point
    smincol = 5   # Top-left screen point
    
    # Calculate the bottom-right screen point:
    # Use the lesser of the hardcoded 25, or the screen's maximum size minus a margin
    smaxrow = min(10, max_row - 1)
    smaxcol = min(25, max_col - 1)
    
    # Ensure the minimum is not greater than the maximum
    if sminrow > smaxrow: smaxrow = sminrow
    if smincol > smaxcol: smaxcol = smincol

    # Refresh the pad, displaying content from (0, 0) of the pad 
    # onto the rectangle (5, 5) to (smaxrow, smaxcol) of the screen.
    i = 0
    while True:
        if i > 100:
            i = 0
        pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)
        time.sleep(0.1)
        i+=1
    
    stdscr.getch()

wrapper(main)