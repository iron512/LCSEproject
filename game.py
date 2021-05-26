import curses
import helper
import numpy as np

import automa

class Dungeon:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.player = None

	def blank(self):
		self.matrix = []

		for x in range(self.rows):
			self.matrix.append([])
			for y in range(self.columns):
				if x == 0 or x == self.rows-1 or y == 0 or y == self.columns-1:
					self.matrix[x].append(1)
				else:
					self.matrix[x].append(0)
		
		self.player = Player(self,int(self.rows/2),int(self.columns/2))

	def cave(self):
		self.matrix = automa.init(self.rows,self.columns)
		self.matrix = automa.cave(self.matrix, 30)

		self.player = Player(self,int(self.rows/2),int(self.columns/2))

	def show(self,stdscr, fog = False):
		for x in range(len(self.matrix)):
			for y in range(len(self.matrix[0])):
				cathetus1 = np.power(x - self.player.X,2)
				cathetus2 = np.power(y/2 - self.player.Y/2,2)
				distance = np.sqrt(cathetus1+cathetus2)

				final = 0

				if distance < 6.5 or not fog:
					if self.matrix[x][y] < 10:
						self.matrix[x][y] += 10
					final = curses.A_BOLD
				else:
					final = curses.A_DIM 

				current = self.matrix[x][y]
				visited = False

				if current >= 10:
					current = self.matrix[x][y] - 10
					visited = True
	
				if visited or not fog:
					if current != 0:
						stdscr.insstr(x,y,"\u2588", curses.color_pair(2) | curses.A_DIM | final)
					else:
						stdscr.insstr(x,y,".", curses.color_pair(2) | final)
				else:
					stdscr.insstr(x,y," ")

		self.drawPlayer(stdscr)

	def drawPlayer(self,stdscr):
		x = self.player.X 
		y = self.player.Y

		if x >= 0 and x < self.rows and y >= 0 and y < self.columns:
			stdscr.addstr(self.player.X,self.player.Y,"@", curses.color_pair(1) | curses.A_BOLD)

class Player:
	def __init__(self, dungeon, playerX, playerY):
		self.X = playerX
		self.Y = playerY
		self.dungeon = dungeon

	def getPosition(self):
		return self.X, self.Y

	def moveUp(self):
		self.X = self.X-1

	def moveDown(self):
		self.X = self.X+1

	def moveRight(self):
		self.Y = self.Y+1

	def moveLeft(self):
		self.Y = self.Y-1

	def getWalls(self, direction):
		if self.X >= 0 and self.X < self.dungeon.rows and self.Y >= 0 and self.Y < self.dungeon.columns:
			if direction == "up":
				return self.dungeon.matrix[self.X-1][self.Y] == 1 or self.dungeon.matrix[self.X-1][self.Y] == 11
			elif direction == "down":
				return self.dungeon.matrix[self.X+1][self.Y] == 1 or self.dungeon.matrix[self.X+1][self.Y] == 11
			elif direction == "right":
				return self.dungeon.matrix[self.X][self.Y+1] == 1 or self.dungeon.matrix[self.X][self.Y+1] == 11
			elif direction == "left":
				return self.dungeon.matrix[self.X][self.Y-1] == 1 or self.dungeon.matrix[self.X][self.Y-1] == 11
		return False