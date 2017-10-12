#!/usr/bin/env python 

import curses

# Create a new screen
stdscr = curses.initscr()

# Add the title of the player
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
title = "M_PLAYER"
titleX = int(stdscr.getmaxyx()[1]/2) - int(len(title)/2)
stdscr.addstr(0, titleX, title, curses.color_pair(1))

# Refresh screen
stdscr.refresh()

command = stdscr.getstr(3,3,20).decode("utf-8") 
if command == "play":
    stdscr.addstr(0, titleX, "You played!", curses.color_pair(1))

stdscr.refresh()
stdscr.getch()

# Close window
curses.endwin()
