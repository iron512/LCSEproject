#!/usr/bin/env python3

import os
import curses
import time

def main(stdscr):
	rows, columns = os.popen('stty size', 'r').read().split()
	rows = int(rows)
	columns = int(columns)

	stdscr.nodelay(1)
	curses.curs_set(0)

	stdscr.addstr(0,0,"\u2554")
	stdscr.addstr(0,1,"\u2550")
	stdscr.addstr(0,2,"\u2550")
	stdscr.addstr(1,0,"\u2551")

	stdscr.addstr(0,columns-1,"\u2557")
	stdscr.addstr(0,columns-2,"\u2550")
	stdscr.addstr(0,columns-3,"\u2550")
	stdscr.addstr(1,columns-1,"\u2551")

	stdscr.addstr(rows-1,0,"\u255A")
	stdscr.addstr(rows-1,1,"\u2550")
	stdscr.addstr(rows-1,2,"\u2550")
	stdscr.addstr(rows-2,0,"\u2551")

	stdscr.insstr(rows-1,columns-1,"\u255D")
	stdscr.addstr(rows-1,columns-2,"\u2550")
	stdscr.addstr(rows-1,columns-3,"\u2550")
	stdscr.addstr(rows-2,columns-1,"\u2551")
	stdscr.refresh()

	stay = True
	cycle = ["\u2596","\u2598","\u259D","\u2597"]
	count = 0

	while stay:
		if stdscr.getch() != -1:
			stay = False
		stdscr.addstr(int(rows/2),int(columns/2),cycle[count%4])
		stdscr.addstr(1,1,str(count))
		stdscr.refresh()
		count = count + 1
		time.sleep(0.2)

curses.wrapper(main)
print()