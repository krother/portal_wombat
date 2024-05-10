"""
Proof-of-concept: move around on a 2D grid

Install dependencies:

    pip install opencv-python
"""
import numpy as np
import cv2

from model import Player, Level, Position


# constants measured in pixel
SCREEN_SIZE_X, SCREEN_SIZE_Y = 640, 640
TILE_SIZE = 64



def read_image(filename):
    """returns an image twice as big"""
    img = cv2.imread(filename)
    return np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))


player_img = read_image("tiles/deep_elf_high_priest.png")
coin_img = read_image("tiles/gold.png")

def draw(x, y, level):
    """draws the player image on the screen"""
    # clear the screen
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    # draw coins
    for c in level.coins:
        xpos, ypos = c.x * TILE_SIZE, c.y * TILE_SIZE
        frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = coin_img
    # draw player        
    xpos, ypos = x * TILE_SIZE, y * TILE_SIZE
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = player_img
    cv2.imshow("frame", frame)


def move(key: str, plr: Player, lvl: Level):
    if key == "d":
        plr.position.x += 1
    elif key == "a":
        plr.position.x -= 1
    elif key == "w":
        plr.position.y -= 1
    elif key == "s":
        plr.position.y += 1

    # collect a coin
    if player.position in lvl.coins:
        print("collected a coin")
        player.points += 10
        print(f"you have {player.points} points")
        lvl.coins.remove(player.position)


level = Level(coins=[Position(x=3, y=1), Position(x=5, y=5)])
player = Player(position=Position(x=0, y=0))
# pydantic checks the validity of types
# at the time of object creation


exit_pressed = False

while not exit_pressed:
    draw(player.position.x, player.position.y, level)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    move(key, player, level)
    if key == "q":
        exit_pressed = True

cv2.destroyAllWindows()
