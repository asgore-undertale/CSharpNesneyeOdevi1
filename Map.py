import os
import random

class Position:
    x = 0
    y = 0
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Tile:
    tile_value = ""
    def __init__(self, tile_value: str):
        self.tile_value = tile_value

class Map:
    width = 0
    height = 0
    board = [[]]
    def __init__(self, width: int, height: int, default_tile: Tile):
        self.width = width
        self.height = height
        self.board = [
            [
                default_tile
                for x in range(width)
            ]
            for y in range(height)
        ]

    def print(self):
        for y in self.board:
            for x in y:
                print(x.tile_value, end="")
            print()

    def check_position(self, position: Position):
        if position.x < 0 or position.x > self.width:
            raise Exception("X value is out of bounds")
        
        if position.y < 0 or position.y > self.height:
            raise Exception("Y value is out of bounds")
    
    def get_tile(self, position: Position) -> Tile:
        self.check_position(position)
        return self.board[position.y][position.x]

    def set_tile(self, position: Position, tile: Tile):
        self.check_position(position)
        self.board[position.y][position.x] = tile
        
    def set_tile_range(self, position1: Position, position2: Position, tile: Tile): # position1 -> top left, position2 -> down right
        for y in range(position1.y, position2.y):
            for x in range(position1.x, position2.x):
                self.set_tile(Position(x, y), tile)
                
class Movement:
    solid_tiles = []
    def __init__(self, solid_tiles: list[Tile]):
        self.solid_tiles = solid_tiles

    def check_position(self, position: Position, map_: Map) -> (bool, Tile):
        tile = map_.get_tile(position)

        for t in self.solid_tiles:
            if t.tile_value == tile.tile_value:
                return False, tile
        
        return True, tile

class Entity:
    def __init__(self, background_tile: Tile):
        self.background_tile = background_tile

class Controller:
    def step(self, command):
        if command == "q":
            print("Game exited.")
            return True
        elif command == "w":
            if player.move(Position(player.position.x, player.position.y-1), map01):
                print("GAME OVER!!!")
                return True
        elif command == "s":
            if player.move(Position(player.position.x, player.position.y+1), map01):
                print("GAME OVER!!!")
                return True
        elif command == "a":
            if player.move(Position(player.position.x-1, player.position.y), map01):
                print("GAME OVER!!!")
                return True
        elif command == "d":
            if player.move(Position(player.position.x+1, player.position.y), map01):
                print("GAME OVER!!!")
                return True

        return False

class Player:
    def __init__(self, position: Position, tile: Tile, movement: Movement, entity: Entity, controller: Controller):
        self.position = position
        self.tile = tile
        self.movement = movement
        self.entity = entity
        self.controller = controller

    def move(self, position: Position, map_: Map) -> None | bool: # True -> Game Over
        state, tile = self.movement.check_position(position, map_)
        
        if state:
            map_.set_tile(self.position, self.entity.background_tile)
            self.position = position
            map_.set_tile(self.position, self.tile)

        if tile.tile_value == gem_tile.tile_value:
            global score
            score += 1
        elif tile.tile_value == monster_tile.tile_value or tile.tile_value == ghost_tile.tile_value:
            map_.set_tile(self.position, self.entity.background_tile)
            return True
            
def update_screen(map_: Map):
    os.system("cls" if os.name == "nt" else "clear")
    map_.print()
    print("\n", "SCORE:", score, "\n")


"""
P -> Player #
G -> Ghost
M -> Monster
# -> Wall #
. -> Gem #
  -> Tile #
"""

wall_tile = Tile("#")
empty_tile = Tile(" ")
gem_tile = Tile(".")
monster_tile = Tile("M")
ghost_tile = Tile("G")

player = Player(
    Position(
        6, 6
    ),
    Tile(
        "P"
    ),
    Movement(
        [
            wall_tile,
            monster_tile,
            ghost_tile
        ]
    ),
    Entity(
        empty_tile
    ),
    Controller()
)

map01 = Map(16, 9, wall_tile)

map01.set_tile_range(Position(1, 1), Position(15, 8), empty_tile)

for _ in range(10):
    map01.set_tile(Position(random.randint(1, 14), random.randint(1, 7)), gem_tile)

map01.set_tile(Position(3, 3), ghost_tile)
map01.set_tile(Position(13, 7), monster_tile)

map01.set_tile(player.position, player.tile)

score = 0
while True:
    update_screen(map01)
    
    command = input("Move using wasd, q to exit.\n> ").lower()
    if player.controller.step(command):
        update_screen(map01)
        break
