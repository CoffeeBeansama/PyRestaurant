import pygame as pg
from timer import Timer
from eventhandler import EventHandler
from settings import *

class MainMenu:
    def __init__(self):
        self.screen = pg.display.get_surface()

        self.black = (0,0,0)
        self.white = (255,255,255)

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.font = pg.font.Font(fontPath,34)
        self.fontColor = self.black
        self.timer = Timer(300)
        
        self.currentRendering = MenuScreen.Main

        self.menuScreens = {
            MenuScreen.Main : self.mainScreen,
            MenuScreen.CreateUser : self.createUserScreen
        }
        
        self.initializeButtonEvents()
        self.initializeButtons()
        
    def initializeButtons(self):
        self.buttonPosX = 145
        self.buttonStartPosY = 70

        self.buttonWidth = 420
        self.buttonHeight = 65

        self.buttonTextPos = 250

        self.submitButtonYPos = 270
        
        self.screenButtons = {
            MenuScreen.Main : {},
            MenuScreen.CreateUser : {},
        }
        
        self.createButtonUI(MainScreenButtons,MenuScreen.Main)
        self.createButtonUI(CreateUserScreenButtons,MenuScreen.CreateUser)
        self.submitText = self.font.render("Submit",True,self.white)
        self.backText = self.font.render("Back",True,self.white)
        

    def initializeButtonEvents(self):
        self.buttonEvents = {
            MainScreenButtons.CreateUser : self.createUserEventClicked,
            MainScreenButtons.Login : self.loginUserEventClicked,
            MainScreenButtons.Settings : self.settingEventClicked,
            MainScreenButtons.QuitGame : self.quitEventClicked,
            CreateUserScreenButtons.CreateUserField : self.textFieldClicked,
            CreateUserScreenButtons.CreatePasswordField : self.textFieldClicked
        }

    def createButtonUI(self,data,buttonUI):
        yOffset = 85
        for index,item in enumerate(data):
            y = self.buttonStartPosY + (index * yOffset)
            self.screenButtons[buttonUI][item] = {}
            self.screenButtons[buttonUI][item]["Y"] = y
            self.screenButtons[buttonUI][item]["Text"] = self.font.render(str(item.value),True,self.white)
            self.screenButtons[buttonUI][item]["Event"] = self.buttonEvents[item]


    def handleRendering(self): 
        # Background
        invX = 120
        invY = 50
        invWidth = 470
        invHeight = 360
        pg.draw.rect(self.screen,self.white,(invX,invY,invWidth,invHeight))
        pg.draw.rect(self.screen,self.black,(invX+5,invY+5,invWidth-10,invHeight-10))
        
        renderCurrentScreen = self.menuScreens.get(self.currentRendering)
        renderCurrentScreen()
    
    def drawButton(self, xPos, yPos, width, height, text):
        # Background
        pg.draw.rect(self.screen, self.white, (xPos, yPos, width, height))
    
        # Button
        button = pg.draw.rect(self.screen, self.black, (xPos + 5, yPos + 5, width - 10, height - 10))
    
        # Text
        self.screen.blit(text, (xPos + 20, yPos + 10))
    
        return button

    # Screens
    def mainScreen(self):
        for key, value in self.screenButtons[MenuScreen.Main].items():
            self.screenButtons[MenuScreen.Main][key]["Button"] = self.drawButton(self.buttonPosX, value["Y"],
                                                                                 self.buttonWidth, self.buttonHeight, value["Text"])


    def createUserScreen(self):
    # Username and Password
        for key, value in self.screenButtons[MenuScreen.CreateUser].items():
            self.screenButtons[MenuScreen.CreateUser][key]["Button"] = self.drawButton(self.buttonPosX, value["Y"],
                                                                                       self.buttonWidth, self.buttonHeight, value["Text"])

        # Submit
        self.createSubmitButton = self.drawButton(self.buttonPosX, self.submitButtonYPos, self.buttonWidth // 2, self.buttonHeight, self.submitText)

        # Back
        self.createBackButton = self.drawButton(self.buttonPosX + (self.buttonWidth // 2) + 10, self.submitButtonYPos,
                                       (self.buttonWidth // 2) - 10, self.buttonHeight, self.backText)
        

    # Button Events
    def createUserEventClicked(self):
        for buttons in self.screenButtons[MenuScreen.Main].values():
            del buttons["Button"]
        self.currentRendering = MenuScreen.CreateUser 

    def loginUserEventClicked(self):
        pass
    
    def settingEventClicked(self):
        pass

    def textFieldClicked(self):
        print("congrats :) ")

    def quitEventClicked(self):
        pass

    def handlePlayerInput(self):
        for menuButton, screenButton in self.screenButtons.items():
            for buttonName, buttonUI in screenButton.items():
                if "Button" in buttonUI and "Event" in buttonUI:
                    button = buttonUI["Button"]
                    function = buttonUI["Event"]
                    if button.collidepoint(EventHandler.mousePosition()):
                        if EventHandler.pressingLeftMouseButton() and not self.timer.activated:
                            function()
                            self.timer.activate()

    def update(self):
        self.timer.update()
        self.handleRendering()
        self.handlePlayerInput()

