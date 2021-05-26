#!/usr/bin/env python3

import os
import curses
import time
import numpy as np

import helper

def main(stdscr):
	rows, columns = helper.screen_size()

	#Disable cursor and blocking keyboard
	stdscr.nodelay(1)
	curses.curs_set(0)

	#Initialize some colors
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

	curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)

	for x in range(columns-1):
		stdscr.addstr(0,x,"\u2550")
		stdscr.addstr(rows-1,x,"\u2550")
		
	for x in range(rows-1):
		stdscr.addstr(x,0,"\u2551")
		stdscr.addstr(x,columns-1,"\u2551")
	
	#Top left corner
	stdscr.addstr(0,0,"\u2554")
	#Bottom left corner
	stdscr.addstr(0,columns-1,"\u2557")
	#Top right corner
	stdscr.addstr(rows-1,0,"\u255A")
	#Bottom right corner. Avoid cursor to exceed window
	stdscr.insstr(rows-1,columns-1,"\u255D")

	#Some cool ascii writings
	center = int(columns/2)
	stdscr.addstr(10,center-25," ██████╗██╗   ██╗██████╗ ███████╗███████╗███████╗",curses.color_pair(5) | curses.A_BOLD)
	stdscr.addstr(11,center-25,"██╔════╝██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝",curses.color_pair(5) | curses.A_BOLD)
	stdscr.addstr(12,center-25,"██║     ██║   ██║██████╔╝███████╗█████╗  ███████╗",curses.color_pair(5) | curses.A_BOLD)
	stdscr.addstr(13,center-25,"██║     ██║   ██║██╔══██╗╚════██║██╔══╝  ╚════██║",curses.color_pair(5) | curses.A_BOLD)
	stdscr.addstr(14,center-25,"╚██████╗╚██████╔╝██║  ██║███████║███████╗███████║",curses.color_pair(5) | curses.A_BOLD)
	stdscr.addstr(15,center-25," ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝",curses.color_pair(5) | curses.A_BOLD)

	stdscr.addstr(rows-15,center-17,"████████╗███████╗███████╗████████╗",curses.color_pair(4) | curses.A_BOLD)
	stdscr.addstr(rows-14,center-17,"╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝",curses.color_pair(4) | curses.A_BOLD)
	stdscr.addstr(rows-13,center-17,"   ██║   █████╗  ███████╗   ██║   ",curses.color_pair(4) | curses.A_BOLD)
	stdscr.addstr(rows-12,center-17,"   ██║   ██╔══╝  ╚════██║   ██║   ",curses.color_pair(4) | curses.A_BOLD)
	stdscr.addstr(rows-11,center-17,"   ██║   ███████╗███████║   ██║   ",curses.color_pair(4) | curses.A_BOLD)
	stdscr.addstr(rows-10,center-17,"   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ",curses.color_pair(4) | curses.A_BOLD)

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

	anykey = "Press ANY key to continue"
	
	for x in range(len(anykey)):
		stdscr.addstr(1,2+x,anykey[x])
		time.sleep(0.05)
		stdscr.refresh()
	
	stdscr.addstr(1,2+len(anykey),"_",curses.A_BLINK)
	stdscr.refresh()

	while stay:
		if stdscr.getch() != -1:
			stay = False

		item = cycle[count%len(cycle)]
		stdscr.addstr(int(rows/2)+item[1],center+item[2],item[0],curses.color_pair(count%3+1))
		stdscr.refresh()
		stdscr.addstr(int(rows/2)+item[1],center+item[2]," ")
		count = count + 1
		time.sleep(0.15)

curses.wrapper(main)
