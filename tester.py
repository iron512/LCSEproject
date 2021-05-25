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
	cycle = [["\u2597",+1,-1],["\u2596",+1,-1],["\u2598",+1,-1],
			["\u2596",0,-1],["\u2598",0,-1],
			["\u2596",-1,-1],["\u2598",-1,-1],["\u259D",-1,-1],
			["\u2598",-1,0],["\u259D",-1,0],
			["\u2598",-1,+1],["\u259D",-1,+1],["\u2597",-1,+1],
			["\u259D",0,+1],["\u2597",0,+1],
			["\u259D",+1,+1],["\u2597",+1,+1],["\u2596",+1,+1],
			["\u2597",+1,0],["\u2596",+1,0]]
	count = 0

	while stay:
		if stdscr.getch() != -1:
			stay = False

		item = cycle[count%len(cycle)]
		stdscr.addstr(int(rows/2)+item[1],int(columns/2)+item[2],item[0])
		stdscr.refresh()
		stdscr.addstr(int(rows/2)+item[1],int(columns/2)+item[2]," ")
		count = count + 1
		time.sleep(0.1)

curses.wrapper(main)
