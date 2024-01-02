import pygame as pg
from timer import Timer
from support import loadSprite
from models import Order

class UI:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.initializeButtonColours()

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.font = pg.font.Font(fontPath,34)
        self.fontColor = self.black
        self.timer = Timer(300)

        self.renderInventory = False
        self.initializeAvailableItems()

    def initializeAvailableItems(self):         
        self.itemSlotPosX = 145
        self.itemSlotStartPosY = 70
        
        self.slotWidth = 420
        self.slotHeight = 65
        
        itemSpriteSize = (35,35)
        self.itemSlots = {}
        for index,item in enumerate(["Burger","Bacon","Donut","Chocolate"]):
            y = self.itemSlotStartPosY + (index * 85)
            
            self.itemSlots[item] = {}
            self.itemSlots[item]["Sprite"] = loadSprite(f"Sprites/{item.lower()}.png",itemSpriteSize).convert_alpha()
            self.itemSlots[item]["Y"] = y
        

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

         for key,items in self.itemSlots.items():
             if not "Button" in self.itemSlots[key]: return # check if button exist first

             if self.itemSlots[key]["Button"].collidepoint(mousePos):
                if mousePressed[0] and not self.timer.activated:
                   newOrder = Order(name=item)
                   newOrder.save()
                   print(f"Pressed the button on {key}")
                   self.timer.activate()
             



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
        
        # Item Slots
        for key,item in self.itemSlots.items():
            # background
            pg.draw.rect(self.screen,invBGColor,(self.itemSlotPosX,item["Y"],self.slotWidth,self.slotHeight))
            # slots
            self.itemSlots[key]["Button"] = pg.draw.rect(self.screen,invColor,(self.itemSlotPosX+5,item["Y"]+5,self.slotWidth-10,self.slotHeight-10))

    def renderUI(self):
        self.timer.update()
        self.renderPurchaseButton()
        self.handleInventoryRendering()
         
        self.handleMouseEvent()

