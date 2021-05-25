#!/usr/bin/env python3

import curses

import helper
import game

def main(stdscr):
	helper.setup()
	rows, columns = helper.screen_size()

	dung = game.Dungeon(rows,columns)
	dung.cave()
	dung.show(stdscr,fog = True)

	while True:
		will = stdscr.getch()

		if chr(will) == "0":
			break

		if (chr(will) == "W" or chr(will) == "w") and not dung.player.getWalls("up"):
			dung.player.moveUp()

		if chr(will) == "S" or chr(will) == "s" and not dung.player.getWalls("down"):
			dung.player.moveDown()

		if chr(will) == "D" or chr(will) == "d" and not dung.player.getWalls("right"):
			dung.player.moveRight()

		if chr(will) == "A" or chr(will) == "a" and not dung.player.getWalls("left"):
			dung.player.moveLeft()

		dung.show(stdscr,fog = True)

curses.wrapper(main)
