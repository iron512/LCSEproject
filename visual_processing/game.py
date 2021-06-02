import automa

class GameSetting:
    def __init__(self, background_color, dim_wall, dim_character, img_character, img_wall, img_wall_removable, img_treasure):
        self.background_color = background_color
        self.dim_wall = dim_wall
        self.dim_character = dim_character
        self.img_character = loadImage(img_character)
        self.img_character.resize(dim_character, dim_character)
        self.img_wall = loadImage(img_wall)
        self.img_wall.resize(dim_wall, dim_wall)
        self.img_treasure = loadImage(img_treasure)
        self.img_treasure.resize(dim_wall, dim_wall)
        self.img_wall_removable = loadImage(img_wall_removable)
        self.img_wall_removable.resize(dim_wall, dim_wall)
        
    def getAllGameSettings(self):
        return self.background_color, self.img_character, self.img_wall, self.img_treasure, self.img_wall_removable

class Score:
    def __init__(self, treasure=0, wall=0):
        self.treasure = treasure
        self.wall = wall
    
    def getTreasureFound(self):
        return self.treasure
    def getRemovableWall(self):
        return self.treasure
    def addTreasureFound(self):
        self.treasure += 1
        return self.count
    def addRemovableWall(self):
        self.wall += 1
        return self.wall

class Dungeon:
    def __init__(self, rows, columns, game_settings):
        self.rows = rows
        self.columns = columns
        self.game_settings = game_settings
        self.player = None
        self.score = None
    
    def cave(self):
        self.matrix = automa.init(self.rows, self.columns)
        self.matrix = automa.cave(self.matrix, 1)
        self.score = Score(0, 0)
        self.player = Player(self,int(self.rows/2),int(self.columns/2), self.score)
    
    def show(self):
        background(self.game_settings.background_color[0], self.game_settings.background_color[1], self.game_settings.background_color[2])
        posX=0
        posY=0
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j == self.player.X and i == self.player.Y:
                    fill(30, 30, 30)
                    image(self.game_settings.img_character,posX-((self.game_settings.dim_character - self.game_settings.dim_wall)/2), posY-((self.game_settings.dim_character - self.game_settings.dim_wall)/2))
                if(self.matrix[i][j] == 2):
                    fill(244, 34, 60)
                    image(self.game_settings.img_wall, posX, posY)
                if(self.matrix[i][j] == 1):
                    image(self.game_settings.img_wall_removable, posX, posY)
                if(self.matrix[i][j] == 3):
                    image(self.game_settings.img_treasure, posX, posY)          
                posX += self.game_settings.dim_wall
            posY += self.game_settings.dim_wall
            posX = 0

class Player:
    def __init__(self, dungeon, playerX, playerY, score):
        self.X = playerX
        self.Y = playerY
        self.dungeon = dungeon
        self.score = score
    
    def getPosition(self):
        return self.X, self.Y
    
    def moveUp(self):
        self.Y = self.Y-1
    
    def moveDown(self):
        self.Y = self.Y+1
    
    def moveRight(self):
        self.X = self.X+1
    
    def moveLeft(self):
        self.X = self.X-1
    
    def getScore(self):
        return self.score
    
    def addTreasure(self):
        self.score.treasure += 1
        return self.score
    
    def addWall(self):
        self.score.wall += 1
        return self.score
        

    def checkMovement(self, direction):
        if self.X >= 0 and self.X < self.dungeon.rows and self.Y >= 0 and self.Y < self.dungeon.columns:
            if direction == "UP":
                return self.dungeon.matrix[self.Y-1][self.X] != 2
            if direction == "DOWN":
                return self.dungeon.matrix[self.Y+1][self.X] != 2
            if direction == "RIGHT":
                return self.dungeon.matrix[self.Y][self.X+1] != 2
            if direction == "LEFT":
                return self.dungeon.matrix[self.Y][self.X-1] != 2
        return False
    
    def nextPosition(self):
        if (self.dungeon.matrix[self.dungeon.player.Y][self.dungeon.player.X] == 1):
            self.addWall()
            self.dungeon.matrix[self.dungeon.player.Y][self.dungeon.player.X] = 0
        if (self.dungeon.matrix[self.dungeon.player.Y][self.dungeon.player.X] == 3 ):
            self.addTreasure()
            self.dungeon.matrix[self.dungeon.player.Y][self.dungeon.player.X] = 0
    
    
    
    
    
    
