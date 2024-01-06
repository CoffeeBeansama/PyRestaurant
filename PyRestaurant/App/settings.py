from enum import Enum

class Scenes(Enum):
    Overworld = "Overworld"
    LoginScreen = "Login"

class MapTiles(Enum):
    Walls = 1
    InteractableObjects = 2
