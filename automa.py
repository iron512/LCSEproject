#!/usr/bin/env python3
from copy import deepcopy

import curses
import time
import numpy as np
import random

import helper

def show(stdscr, matrix):
	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			if matrix[x][y] == 0:
				stdscr.insstr(x,y,".")
			else:
				stdscr.insstr(x,y,"\u2588")
	stdscr.refresh()

def init(rows,columns, seed = None):
	#procedural generation
	random.seed(seed)
	matrix = np.zeros((rows,columns), dtype=int)

	for x in range(rows):
		for y in range(columns):
			if random.randint(0,1) == 0: 
				matrix[x][y] = 1
			else:
				matrix[x][y] = 0
	return matrix

def cave(matrix, generations):
	##CODE HERE##
	return matrix

def evolve(matrix):
	##CODE HERE##
	return matrix

def main(stdscr):
	helper.setup()
	rows, columns = helper.screen_size()

	automa = init(rows,columns)
	show(stdscr,automa)

	##CODE HERE##

	while True:
		choice = chr(stdscr.getch())

		if choice == "0":
			break;

		automa = cave(automa, 1)
		#automa = evolve(automa)
		show(stdscr,automa)

#MAIN
if (__name__ == '__main__'):
	curses.wrapper(main)
