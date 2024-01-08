import pygame as pg
from timer import Timer
from eventhandler import EventHandler
from settings import MenuScreen

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

        self.mainScreenButtonData = ["Create User","Login","Settings","Quit Game"]
        self.playerScreenButtonData = ["Username","Password"]
        
        self.screenButtons = {
            "Main Screen" : {},
            "Create User" : {},
        }
        
        self.createButtonUI(self.mainScreenButtonData,"Main Screen")
        self.createButtonUI(self.playerScreenButtonData,"Create User")
        
        self.submitText = self.font.render("Submit",True,self.white)
        self.backText = self.font.render("Back",True,self.white)

    def initializeButtonEvents(self):
        self.buttonEvents = {
            "Create User" : self.createUserEventClicked,
            "Login" : self.loginUserEventClicked,
            "Settings" : self.settingEventClicked,
            "Quit Game" : self.quitEventClicked,
            "Username" : self.userNameOrPasswordEventClicked,
            "Password" : self.userNameOrPasswordEventClicked
        }

    def createButtonUI(self,data,buttonUI):
        yOffset = 85
        for index,item in enumerate(data):
            y = self.buttonStartPosY + (index * yOffset)
            self.screenButtons[buttonUI][item] = {}
            self.screenButtons[buttonUI][item]["Y"] = y
            self.screenButtons[buttonUI][item]["Text"] = self.font.render(str(item),True,self.white)
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
    
    # Screens
    def mainScreen(self):
        for key,value in self.screenButtons["Main Screen"].items():
            # Background
            pg.draw.rect(self.screen,self.white,
                         (self.buttonPosX,value["Y"],
                          self.buttonWidth,self.buttonHeight))
            # Button
            self.screenButtons["Main Screen"][key]["Button"] = pg.draw.rect(self.screen,self.black,
                         (self.buttonPosX+5,value["Y"]+5,
                          self.buttonWidth-10,self.buttonHeight-10))

            # Text
            self.screen.blit(value["Text"],(self.buttonPosX+20,value["Y"]+10))
    
    def createUserScreen(self):
        # Username and Password
        for key,value in self.screenButtons["Create User"].items():
            # Background
            pg.draw.rect(self.screen,self.white,
                         (self.buttonPosX,value["Y"],
                          self.buttonWidth,self.buttonHeight))
            # Button
            self.screenButtons["Create User"][key]["Button"] = pg.draw.rect(self.screen,self.black,
                         (self.buttonPosX+5,value["Y"]+5,
                          self.buttonWidth-10,self.buttonHeight-10))
            # Text
            self.screen.blit(value["Text"],(self.buttonPosX+20,value["Y"]+10))
        
        # Submit and back

        # Submit
        # Background
        pg.draw.rect(self.screen,self.white,
                    (self.buttonPosX,self.submitButtonYPos,
                    self.buttonWidth//2,self.buttonHeight))

        # Button
        self.createSubmitButton = pg.draw.rect(self.screen,self.black,
                    (self.buttonPosX+5,self.submitButtonYPos+5,
                    (self.buttonWidth-20)//2,self.buttonHeight-10))
        # Text
        self.screen.blit(self.submitText,(self.buttonPosX+20,self.submitButtonYPos+10))

        # Back
        # Background
        pg.draw.rect(self.screen,self.white,
                    ((self.buttonPosX+(self.buttonWidth//2))+10,self.submitButtonYPos,
                    (self.buttonWidth//2)-10,self.buttonHeight))

        # Button
        self.createSubmitButton = pg.draw.rect(self.screen,self.black,
                    ((self.buttonPosX+(self.buttonWidth//2))+15,self.submitButtonYPos+5,
                    (self.buttonWidth//2)-20,self.buttonHeight-10))
        # Text
        self.screen.blit(self.backText,(self.buttonPosX+(self.buttonWidth//2)+30,
                                        self.submitButtonYPos+10))

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

