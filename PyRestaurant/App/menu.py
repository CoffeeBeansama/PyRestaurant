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
            CreateUserScreenButtons.Username : self.userNameOrPasswordEventClicked,
            CreateUserScreenButtons.Password : self.userNameOrPasswordEventClicked
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
        button_rect = pg.draw.rect(self.screen, self.black, (xPos + 5, yPos + 5, width - 10, height - 10))
    
        # Text
        self.screen.blit(text, (xPos + 20, yPos + 10))
    
        return button_rect

    # Screens
    def mainScreen(self):
        for key, value in self.screenButtons[MenuScreen.Main].items():
            button_rect = self.drawButton(self.buttonPosX, value["Y"], self.buttonWidth, self.buttonHeight, value["Text"])
            self.screenButtons[MenuScreen.Main][key]["Button"] = button_rect

    def createUserScreen(self):
        # Username and Password
        for key, value in self.screenButtons[MenuScreen.CreateUser].items():
            button_rect = self.drawButton(self.buttonPosX, value["Y"], self.buttonWidth, self.buttonHeight, value["Text"])
            self.screenButtons[MenuScreen.CreateUser][key]["Button"] = button_rect

        # Submit
        submit_button_rect = self.drawButton(self.buttonPosX, self.submitButtonYPos, self.buttonWidth // 2, self.buttonHeight, self.submitText)
        self.createSubmitButton = submit_button_rect

        # Back
        back_button_rect = self.drawButton(self.buttonPosX + (self.buttonWidth // 2) + 10, self.submitButtonYPos,
                                       (self.buttonWidth // 2) - 10, self.buttonHeight, self.backText)
        self.createBackButton = back_button_rect
        
    # Button Events
    def createUserEventClicked(self):
        self.currentRendering = MenuScreen.CreateUser
    
    def loginUserEventClicked(self):
        pass
    
    def settingEventClicked(self):
        pass

    def userNameOrPasswordEventClicked(self):
        pass

    def quitEventClicked(self):
        pass

    def handlePlayerInput(self): 
        for screenButtons in self.screenButtons.values():
            for key,value in screenButtons.items():
                if not "Button" in screenButtons[key]: return
                if not "Event" in screenButtons[key]: return                  
                if screenButtons[key]["Button"].collidepoint(EventHandler.mousePosition()):
                   if EventHandler.pressingLeftMouseButton() and not self.timer.activated:
                      screenButtons[key]["Event"]()
                      self.timer.activate()

    def update(self):
        self.timer.update()
        self.handlePlayerInput()
        self.handleRendering()

