import os
import curses

def screen_size():
	rows, columns = os.popen('stty size', 'r').read().split()
	return int(rows), int(columns)

def setup():
	curses.curs_set(0)

	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
