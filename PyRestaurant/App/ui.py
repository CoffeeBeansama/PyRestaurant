import pygame as pg

class UI:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.initializeButtonColours()

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.font = pg.font.Font(fontPath,34)
        self.fontColor = self.black

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
              if mousePressed[0]:
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

    def renderUI(self):
        self.renderPurchaseButton()

        self.handleMouseEvent()
