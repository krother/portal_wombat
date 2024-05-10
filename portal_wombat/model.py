from pydantic import BaseModel
# from typing import List  # Py 3.9

class Position(BaseModel):
    x: int
    y: int


class Level(BaseModel):
    coins: list[Position]     # Py 3.10+
    # coins: List[Position]   # Py 3.9-


class Player(BaseModel):
    position: Position
    points: int = 0



if __name__ == "__main__":
    level = Level(coins=[])
    print(level)

    player = Player(position=Position(x=0, y=0))
    print(player)
    # pydantic checks the validity of types
    # at the time of object creation
