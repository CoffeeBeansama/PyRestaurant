import pygame as pg
from timer import Timer

class UI:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.initializeButtonColours()

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.font = pg.font.Font(fontPath,34)
        self.fontColor = self.black

        self.timer = Timer(300)

        self.renderInventory = False
        
    def initializeButtonColours(self):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.yellow = (255,0,0)

        self.buttonColor = self.black

    def handleMouseEvent(self):
         mousePos = pg.mouse.get_pos()
         mousePressed = pg.mouse.get_pressed()

         if self.readyButton.collidepoint(mousePos):
              self.buttonColor = self.white
              self.fontColor = self.black
              if mousePressed[0] and not self.timer.activated:
                    
                    self.renderInventory = True if not self.renderInventory else False
                                        
                    self.timer.activate()
                    self.fontColor = self.yellow
         else:
              self.buttonColor = self.black
              self.fontColor = self.white

    def renderPurchaseButton(self):
         btnX = 530
         btnY = 430
         btnWidth = 150
         btnHeight = 50
         self.readyButton = pg.draw.rect(self.screen,self.buttonColor,(btnX,btnY,btnWidth,btnHeight))

         ready = self.font.render("Purchase",True,self.fontColor)
         self.screen.blit(ready,(538,432))
    
    def handleInventoryRendering(self):
        if not self.renderInventory: return
        
        # Background
        invX = 120
        invY = 50
        invWidth = 470   
        invHeight = 360
        invBGColor = (255,255,255)
        invColor = (0,0,0)
        pg.draw.rect(self.screen,invBGColor,(invX,invY,invWidth,invHeight))
        pg.draw.rect(self.screen,invColor,(invX+5,invY+5,invWidth-10,invHeight-10))
        
    def renderUI(self):
        self.timer.update()
        self.renderPurchaseButton()
        self.handleInventoryRendering()

        self.handleMouseEvent()
