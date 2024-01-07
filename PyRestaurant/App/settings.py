from enum import Enum

class MenuScreen(Enum):
    Main = "Main"
    CreateUser = "CreateUser"
    Login = "Login"
    Settings = "Settings"
    

class Scenes(Enum):
    Overworld = "Overworld"
    LoginScreen = "Login"

class MapTiles(Enum):
    Walls = 1
    InteractableObjects = 2
