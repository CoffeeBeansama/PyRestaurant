from enum import Enum

class MenuScreen(Enum):
    Main = "Main Screen"
    CreateUser = "Create User"
    Login = "Login"
    Settings = "Settings"

class MainScreenButtons(Enum):
    CreateUser = "Create User"
    Login = "Login"
    Settings = "Settings"
    QuitGame = "Quit Game"

class CreateUserScreenButtons(Enum):
    Username = "Create User"
    Password = "Login"

class Scenes(Enum):
    Overworld = "Overworld"
    LoginScreen = "Login"

class MapTiles(Enum):
    Walls = 1
    InteractableObjects = 2
