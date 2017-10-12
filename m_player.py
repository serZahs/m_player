#!/usr/bin/env python 

import curses
import vlc

songs = []
files = []
songPointer = -1

# Screen operations
stdscr = curses.initscr()
screenH = stdscr.getmaxyx()[0]
screenW = stdscr.getmaxyx()[1]

def user_input():
    stdscr.addstr(screenH-1, 0, "> ")
    instream = stdscr.getstr(screenH-1,2,screenW-1).decode("utf-8")
    stdscr.addstr(screenH-1, 2, " "*len(instream))
    return instream.lower().strip()

# Colors
curses.start_color()
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

# Add the title of the player
title = "M_PLAYER"
titleX = int(screenW/2) - int(len(title)/2)
stdscr.addstr(0, titleX, title, curses.color_pair(1))

# Basic UI elements
stdscr.addstr(1, 10, "Commands", curses.color_pair(1))
stdscr.addstr(3, 10, "> open <file> - open an audio file", curses.A_BOLD)
stdscr.addstr(4, 10, "> play - play most recently added audio file", curses.A_BOLD)
stdscr.addstr(3, 60, "> stop - stop playing file", curses.A_BOLD)
stdscr.addstr(4, 60, "> leave - exit program", curses.A_BOLD)
stdscr.addstr(6, 10, "Current songs available", curses.color_pair(1))

# Ask for input
command = user_input()
while (command!="leave"):
    if command[0:4] == "open":
        active = vlc.MediaPlayer("/Users/ramesses/Downloads/"+command[5:])
        songs.append(command[5:])
        songPointer+=1
        for i in range(len(songs)):
            stdscr.addstr(i+7, 10, str(i+1) + ". " + songs[i], curses.color_pair(3)) 
    elif command == "play":
        active.play()
        stdscr.addstr(songPointer+7, 10+len(songs[songPointer]), ": Playing", curses.color_pair(2))
    elif command == "stop":
        active.stop()
    stdscr.refresh()
    command = user_input()

# Close window
curses.endwin()
