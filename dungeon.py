class DungeonMap:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.player = False

	def blank(self):
		self.matrix = []

		for x in range(self.rows):
			self.matrix.append([])
			for y in range(self.columns):
				if x == 0 or x == self.rows-1 or y == 0 or y == self.columns-1:
					self.matrix[x].append("M")
				else:
					self.matrix[x].append("T")
		
		self.matrix[int(self.rows/2)][int(self.columns/2)] = "P"

		self.player = True
		self.playerX = int(self.columns/2)
		self.playerY = int(self.rows/2)

	def cave(self):
		self.blank()

	def moveUp():
		if self.player:
			self.matrix[self.playerX][self.playerY] = "T"
			
			if (self.playerX != 0):
				self.playerX -= 1
				self.matrix[self.playerX][self.playerY] = "P"
			else:
				self.player = False
