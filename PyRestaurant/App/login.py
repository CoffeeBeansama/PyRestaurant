import pygame as pg
from timer import Timer

class LoginScreen:
    def __init__(self):
        self.screen = pg.display.get_surface()

        self.black = (0,0,0)
        self.white = (255,255,255)

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.font = pg.font.Font(fontPath,34)
        self.fontColor = self.black
        self.timer = Timer(300)

        self.initializeButtons()
        
    def initializeButtons(self):
        self.buttonPosX = 145
        self.buttonStartPosY = 70

        self.buttonWidth = 420
        self.buttonHeight = 65

        self.buttonData = ["Create User","Login","Settings","Quit Game"]
        self.buttonUI = {}
        
        self.buttonTextPos = 250

        for index,item in enumerate(self.buttonData):
            y = self.buttonStartPosY + (index * 85)

            self.buttonUI[item] = {}
            self.buttonUI[item]["Y"] = y
            self.buttonUI[item]["Text"] = self.font.render(str(item),True,self.white)

    def handleRendering(self): 
        # Background
        invX = 120
        invY = 50
        invWidth = 470
        invHeight = 360
        pg.draw.rect(self.screen,self.white,(invX,invY,invWidth,invHeight))
        pg.draw.rect(self.screen,self.black,(invX+5,invY+5,invWidth-10,invHeight-10))

        for key,value in self.buttonUI.items():
            # background
            pg.draw.rect(self.screen,self.white,
                         (self.buttonPosX,value["Y"],
                          self.buttonWidth,self.buttonHeight))
            # button
            pg.draw.rect(self.screen,self.black,
                         (self.buttonPosX+5,value["Y"]+5,
                          self.buttonWidth-10,self.buttonHeight-10))

            # text
            self.screen.blit(value["Text"],(self.buttonPosX+20,value["Y"]+10))

    def handlePlayerInput(self):
        pass

    def update(self):
        self.timer.update()
        self.handlePlayerInput()
        self.handleRendering()
