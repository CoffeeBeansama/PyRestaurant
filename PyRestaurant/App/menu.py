import pygame as pg
from timer import Timer
from eventhandler import EventHandler
from settings import *
from views import addNewCustomer,customerExists

class MainMenu:
    def __init__(self,startOverworld):
        self.screen = pg.display.get_surface()
        self.startOverworld = startOverworld

        self.black = (0,0,0)
        self.white = (255,255,255)

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.font = pg.font.Font(fontPath,34)
        self.fontColor = self.black
        self.timer = Timer(300)
        self.textFieldTimer = Timer(170)        
        self.currentRendering = MenuScreen.Main

        self.menuScreens = {
            MenuScreen.Main : self.mainScreen,
            MenuScreen.CreateUser : self.createUserScreen,
            MenuScreen.Login : self.loginUserScreen,

        }
        
        self.newPlayer = None

        self.mainAlphaKeys = range(pg.K_a,pg.K_z + 1)
        self.mainNumberKeys = range(pg.K_0,pg.K_9 + 1)               

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
        self.createButtonUI(UserInfo,MenuScreen.CreateUser)

        self.submitText = self.font.render("Submit",True,self.white)
        self.backText = self.font.render("Back",True,self.white)
        
        self.startInputField = False
        
        self.submitButton = None
        self.backButton = None

    def initializeButtonEvents(self):
        self.buttonEvents = {
            MainScreenButtons.CreateUser : self.createUserEventClicked,
            MainScreenButtons.Login : self.loginUserEventClicked,
            MainScreenButtons.Settings : self.settingEventClicked,
            MainScreenButtons.QuitGame : self.quitEventClicked,
            UserInfo.Username : self.textFieldClicked,
            UserInfo.Password : self.textFieldClicked
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

        for button in self.screenButtons[MenuScreen.CreateUser].values():
            if "InputText" in button:
                button["Text"] = self.font.render(button['InputText'],True,self.white)
    
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
        self.submitButton = self.drawButton(self.buttonPosX, self.submitButtonYPos, self.buttonWidth // 2, self.buttonHeight, self.submitText)

        # Back
        self.backButton = self.drawButton(self.buttonPosX + (self.buttonWidth // 2) + 10, self.submitButtonYPos,
                                       (self.buttonWidth // 2) - 10, self.buttonHeight, self.backText)
        

    def loginUserScreen(self):
        # Username and Password
        for key, value in self.screenButtons[MenuScreen.CreateUser].items():
            self.screenButtons[MenuScreen.CreateUser][key]["Button"] = self.drawButton(self.buttonPosX, value["Y"],
                                                                                       self.buttonWidth, self.buttonHeight, value["Text"])

        # Submit
        self.submitButton = self.drawButton(self.buttonPosX, self.submitButtonYPos, self.buttonWidth // 2, self.buttonHeight, self.submitText)

        # Back
        self.backButton = self.drawButton(self.buttonPosX + (self.buttonWidth // 2) + 10, self.submitButtonYPos,
                                       (self.buttonWidth // 2) - 10, self.buttonHeight, self.backText)

    # Button Events
    def createUserEventClicked(self):
        for buttons in self.screenButtons[MenuScreen.Main].values():
            del buttons["Button"]
        self.currentRendering = MenuScreen.CreateUser 
        
        
        usernameField = self.screenButtons[MenuScreen.CreateUser][UserInfo.Username]
        passwordField = self.screenButtons[MenuScreen.CreateUser][UserInfo.Password]

        usernameField["FieldActive"] = False
        passwordField["FieldActive"] = False

    def loginUserEventClicked(self):
        for buttons in self.screenButtons[MenuScreen.Main].values():
            del buttons["Button"]
        self.currentRendering = MenuScreen.Login 
                
        usernameField = self.screenButtons[MenuScreen.CreateUser][UserInfo.Username]
        passwordField = self.screenButtons[MenuScreen.CreateUser][UserInfo.Password]

        usernameField["FieldActive"] = False
        passwordField["FieldActive"] = False
    
    def settingEventClicked(self):
        pass
    
    def textFieldClicked(self):
        pass
    
    def quitEventClicked(self):
        pass

    def isCapsLockOn(self):
        mods = pg.key.get_mods()    
        return mods & pg.KMOD_CAPS
    
    def getKeyboardPressed(self,textField,keys):
        if EventHandler.keyboardKeys()[pg.K_SPACE] and not self.textFieldTimer.activated:
           self.textFieldTimer.activate()
           textField["InputText"] += str(" ")
           return

        for key in keys:
            if EventHandler.keyboardKeys()[key] and not self.textFieldTimer.activated:
               self.textFieldTimer.activate()
               if self.isCapsLockOn():
                  textField["InputText"] += chr(key).upper()
               else:
                  textField["InputText"] += chr(key).lower()
               return
         


    def handleInputFieldEvents(self):
        for textField in self.screenButtons[MenuScreen.CreateUser].values():
            if not "FieldActive" in textField: return
            
            # Checks if mouse is still on the input field
            # Disables getting letters if mouse is outside the input field
            if "Button" in textField:
               if not textField["Button"].collidepoint(EventHandler.mousePosition()):
                  textField["FieldActive"] = False

            # Checks if input field is active
            # Loop through the keyboard keys (a-z) and (0-9)
            # converts any key pressed to character strings
            if textField["FieldActive"]:
               
               # Handles text deletion
               if EventHandler.keyboardKeys()[pg.K_BACKSPACE] and not self.textFieldTimer.activated:
                  textField["InputText"] = textField["InputText"][:-1]
                  self.textFieldTimer.activate()
            
               self.getKeyboardPressed(textField,self.mainAlphaKeys)
               self.getKeyboardPressed(textField,self.mainNumberKeys)



    def handleSubmitButtonEvent(self):
        if not self.submitButton: return

        usernameField = self.screenButtons[MenuScreen.CreateUser][UserInfo.Username]
        passwordField = self.screenButtons[MenuScreen.CreateUser][UserInfo.Password]

        match self.currentRendering:
            case MenuScreen.CreateUser:
                 if self.buttonPressed(self.submitButton):
                    # Creates and adds new user
                    self.newPlayer = addNewCustomer(usernameField["InputText"],passwordField["InputText"])
                    self.timer.activate()
                    self.startOverworld()

            case MenuScreen.Login:
                 if self.buttonPressed(self.submitButton):                    
                    if customerExists(usernameField["InputText"],passwordField["InputText"]):
                       self.startOverworld()
                    else:
                       print("This account doesn't exits")
                       print("Create an account or input the correct username and password")
                    self.timer.activate()

    def handleBackButtonEvent(self):
        if not self.backButton: return
        
        if self.currentRendering != MenuScreen.Main and self.buttonPressed(self.backButton):
           for key,button in self.screenButtons[MenuScreen.CreateUser].items():
               button["InputText"] = "Username" if key == UserInfo.Username else "Password"
           self.currentRendering = MenuScreen.Main

    def buttonPressed(self,button):
        if button.collidepoint(EventHandler.mousePosition()):
           if EventHandler.pressingLeftMouseButton() and not self.timer.activated:
              return True
           return False

    def currentPlayer(self):
        return self.newPlayer

    def handlePlayerInput(self):
        for menuButton, screenButton in self.screenButtons.items():
            for buttonName, buttonUI in screenButton.items():
                if "Button" in buttonUI and "Event" in buttonUI:
                    button = buttonUI["Button"]
                    function = buttonUI["Event"]
                    if self.buttonPressed(button):
                       self.handleTextFieldClickedEvent(buttonName,screenButton)
                       function()
                       self.timer.activate()

        self.handleInputFieldEvents()
        self.handleSubmitButtonEvent()
        self.handleBackButtonEvent()


    def handleTextFieldClickedEvent(self,buttonName,buttonUI):
        if buttonName in [UserInfo.Username,UserInfo.Password]:
           buttonUI[buttonName]["Text"] = self.font.render("|",True,self.white)
           buttonUI[buttonName]["InputText"] = ""
           buttonUI[buttonName]["FieldActive"] = True

    def update(self):
        self.timer.update()
        self.textFieldTimer.update()
        self.handleRendering()
        self.handlePlayerInput()
