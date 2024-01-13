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
    CreateUserField = "Username"
    CreatePasswordField = "Password"

class Scenes(Enum):
    Overworld = "Overworld"
    MenuScreen = "MenuScreen"

class MapTiles(Enum):
    Walls = 1
    InteractableObjects = 2
