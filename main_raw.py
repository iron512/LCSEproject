#!/usr/bin/env python3

import os
import curses

rows, columns = os.popen('stty size', 'r').read().split()

#INIT CURSES
stdscr = curses.initscr()
stdscr.clear()

curses.curs_set(0)
curses.noecho()
curses.cbreak()

#ACTUAL CODE
stdscr.addstr(10,100,"hello")
stdscr.refresh()

stdscr.getch()

#TERMINATE CURSES
curses.curs_set(1)
curses.echo()
curses.nocbreak()
		
curses.endwin()	