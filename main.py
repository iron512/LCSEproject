#!/usr/bin/env python3

import curses

import helper
import game

def main(stdscr):
	helper.setup()

	##CODE HERE##

	rows, columns = helper.screen_size()

	dung = game.Dungeon(rows, columns)
	dung.cave()
	dung.show(stdscr, fog = True)

	while True:
		choice = chr(stdscr.getch())

		if choice == "0":
			break

		if (choice == "W" or choice == "w") and not dung.player.getWalls("up"):
			dung.player.moveUp()
		
		if (choice == "S" or choice == "s") and not dung.player.getWalls("down"):
			dung.player.moveDown()
		
		if (choice == "D" or choice == "d") and not dung.player.getWalls("right"):
			dung.player.moveRight()

		if (choice == "A" or choice == "a") and not dung.player.getWalls("left"):
			dung.player.moveLeft()

		dung.show(stdscr, fog = True)

curses.wrapper(main)
