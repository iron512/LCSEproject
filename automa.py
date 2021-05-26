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

def init(rows,columns, seed = None):
	#procedural generation
	random.seed(seed)
	matrix = np.zeros((rows,columns), dtype=int)

	for x in range(rows):
		for y in range(columns):
			if False and (x == 0 or x == rows-1 or y == 0 or y == columns-1):
				matrix[x][y] = 2
			else:
				if random.randint(0,1) == 0: 
					matrix[x][y] = 1
				else:
					matrix[x][y] = 0
	return matrix

def cave(matrix, generations):
	replacement = []
	for z in range(generations):
		replacement = np.zeros((len(matrix),len(matrix[0])), dtype=int)
		replacement = replacement + 2
		for x in range(1,len(matrix)-1):
			for y in range(1,len(matrix[0])-1):
				total = -matrix[x][y]
				for a in range(x-1,x+2):
					for b in range(y-1,y+2):
						total += matrix[a][b] 

				if total > 5:
					replacement[x][y] = 1
				elif total < 4:
					replacement[x][y] = 0
				else:
					replacement[x][y] = matrix[x][y]
		matrix = replacement
	return replacement


def evolve(matrix):
	replacement = np.zeros((len(matrix),len(matrix[0])), dtype=int)

	for x in range(1,len(matrix)-1):
		for y in range(1,len(matrix[0])-1):
			total = -matrix[x][y]
			for a in range(x-1,x+2):
				for b in range(y-1,y+2):
					total += matrix[a][b] 

			if matrix[x][y] != 0:
				if total < 2:
					replacement[x][y] = 0
				elif total == 2 or total == 3:
					replacement[x][y] = 1
				elif total > 3:
					replacement[x][y] = 0
			else:
				if total == 3:
					replacement[x][y] = 1
				else:
					replacement[x][y] = 0
	return replacement

def main(stdscr):
	helper.setup()
	rows, columns = helper.screen_size()

	automa = init(rows,columns)
	show(stdscr,automa)

	while True:
		will = stdscr.getch()

		if chr(will) == "Q" or chr(will) == "q":
			break;

		automa = cave(automa, 1)
		show(stdscr,automa)

#MAIN
if (__name__ == '__main__'):
	curses.wrapper(main)