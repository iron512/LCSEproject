from game import Dungeon, Player, GameSetting
dim = 30
dim_c = 30

rows = 25
columns = 25
dim_console = 70
window_sizeX = dim * columns
window_sizeY = dim * rows + dim_console

background_color = (179, 179, 179)
#img_character =  "man.png"
#img_wall = "wall_dungeon.png"
#img_wall_removable = "wood.png"
#img_treasure = "treasure.png"

img_character =  "mario.png"
img_wall = "wall.jpeg"
img_wall_removable = "grass.png"
img_treasure = "money.png"
#background_color = (32, 110, 4)

def setup():
    size(window_sizeX, window_sizeY)
    global dungeon, game_settings, img_character, img_wall, img_wall_removable, img_treasure
    # CREATE SETTINGS
    #game_settings = GameSetting(background_color, dim, dim_c, "mario.png", "wall.jpeg", "grass.png", "money.png")
    game_settings = GameSetting(background_color, dim, dim_c, img_character, img_wall, img_wall_removable, img_treasure)
    # CREATE DUNGEON
    dungeon = Dungeon(rows, columns, game_settings)
    dungeon.cave()
    
    
    
def draw():
    global game_settings
    dungeon.show()
    # CONSOLE
    fill(230, 230, 230)
    noStroke()
    rect(0,game_settings.dim_wall * len(dungeon.matrix), game_settings.dim_wall * len(dungeon.matrix[0]), dim_console)
    image(game_settings.img_treasure, game_settings.dim_wall * len(dungeon.matrix[0])/2 - game_settings.dim_wall, game_settings.dim_wall * len(dungeon.matrix)+10)
    fill(0)
    text("%d" % dungeon.player.getScore().treasure, game_settings.dim_wall * len(dungeon.matrix[0])/2 - game_settings.dim_wall, game_settings.dim_wall * len(dungeon.matrix)+55)
    image(game_settings.img_wall_removable, game_settings.dim_wall * len(dungeon.matrix[0])/2 + game_settings.dim_wall, game_settings.dim_wall * len(dungeon.matrix)+10)
    fill(0)
    text("%d" % dungeon.player.getScore().wall, game_settings.dim_wall * len(dungeon.matrix[0])/2 + game_settings.dim_wall, game_settings.dim_wall * len(dungeon.matrix)+55)

def keyPressed():
    global dungeon, count_treasure
    if keyCode == UP:
        if(dungeon.player.checkMovement("UP")):
            dungeon.player.moveUp()
            dungeon.player.nextPosition()
    elif keyCode == DOWN:
        if(dungeon.player.checkMovement("DOWN")):
            dungeon.player.moveDown()
            dungeon.player.nextPosition()
    elif keyCode == RIGHT:
        if(dungeon.player.checkMovement("RIGHT")):
            dungeon.player.moveRight()
            dungeon.player.nextPosition()
    elif keyCode == LEFT:
        if(dungeon.player.checkMovement("LEFT")):
            dungeon.player.moveLeft()
            dungeon.player.nextPosition()
    
