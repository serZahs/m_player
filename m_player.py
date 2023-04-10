import time
import curses
import vlc
import os

active = 0

# Screen operations
stdscr = curses.initscr()
scrH = stdscr.getmaxyx()[0]
scrW = stdscr.getmaxyx()[1]

# VLC operations
files = vlc.MediaList()
player = vlc.MediaListPlayer()
player.set_media_list(files)

def init_scr():
    # Colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    # Add the title of the program
    title = "M_PLAYER"
    titleX = int(scrW/2) - int(len(title)/2)
    stdscr.addstr(0, titleX, title, curses.color_pair(1))

    # Add rest of UI
    stdscr.addstr(1, 10, "Commands", curses.color_pair(1))
    stdscr.addstr(3, 10, "$$ open <file> - open a media file", curses.A_BOLD)
    stdscr.addstr(4, 10, "$$ play <num> - play media file at position num", curses.A_BOLD)
    stdscr.addstr(3, 60, "$$ stop - stop playing media", curses.A_BOLD)
    stdscr.addstr(4, 60, "$$ leave - exit program", curses.A_BOLD)
    stdscr.addstr(6, 10, "Current files available", curses.color_pair(1))
    
def user_input():
    stdscr.addstr(scrH-1, 0, "$$ ")
    instream = stdscr.getstr(scrH-1,3,scrW-1).decode("utf-8")
    stdscr.addstr(scrH-1, 3, " "*len(instream))
    res = instream.lower().strip()
    return res

def stop_media(active):
    if (player.is_playing()):
        player.stop()
        stdscr.addstr(active+7, 13+len(os.path.basename(files[active].get_mrl()[8:])), " STOPPED ", curses.color_pair(4))
        stdscr.refresh()
        time.sleep(0.5) 
        stdscr.addstr(active+7, 13+len(os.path.basename(files[active].get_mrl()[8:])), " "*10)

init_scr()
action = user_input()

# Main loop of program
while (action != "leave"):
    
    if action[0:4] == "open":
        path = (action[5:])
        files.add_media(path)
        for i in range(len(files)):
            stdscr.addstr(i+7, 10, str(i+1)+". ")
            stdscr.addstr(i+7, 13, os.path.basename(files[i].get_mrl()[8:]), curses.color_pair(3))

    elif action[0:4] == "play":
        stop_media(active)
        active = int(action[5:])-1
        player.play_item_at_index(active)
        stdscr.addstr(active+7, 13+len(os.path.basename(files[active].get_mrl()[8:])), ": PLAYING", curses.color_pair(2))

    elif action == "stop":
        stop_media(active)

    stdscr.refresh()
    action = user_input()

# Close window
curses.endwin()
