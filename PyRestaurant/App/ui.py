import pygame as pg
from timer import Timer
from support import loadSprite
from views import addOrder
from eventhandler import EventHandler


class UI:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.player = None
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
        
        self.itemSpriteXPos = 495

        self.slotWidth = 420
        self.slotHeight = 65
        
        itemSpriteSize = (60,60)

        self.itemList = ["Burger","Bacon","Donut","Chocolate"]
        self.itemSlots = {}

        for index,item in enumerate(self.itemList):
            y = self.itemSlotStartPosY + (index * 85)
            
            self.itemSlots[item] = {}
            self.itemSlots[item]["Sprite"] = loadSprite(f"Sprites/{item.lower()}.png",itemSpriteSize).convert_alpha()
            self.itemSlots[item]["Y"] = y
            white = (255,255,255)
            self.itemSlots[item]["Text"] = self.font.render(f"Order: {str(item)}",True,self.white)
        

    def initializeButtonColours(self):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.yellow = (255,0,0)

        self.buttonColor = self.black

    def handleMouseEvent(self):

         if self.readyButton.collidepoint(EventHandler.mousePosition()):
             self.buttonColor = self.white
             self.fontColor = self.black
             if EventHandler.pressingLeftMouseButton() and not self.timer.activated:
                self.renderInventory = True if not self.renderInventory else False
                self.timer.activate()
                self.fontColor = self.yellow
         else:
              self.buttonColor = self.black
              self.fontColor = self.white

         for key,items in self.itemSlots.items():
             if not "Button" in self.itemSlots[key]: return # check if button exist first

             if self.itemSlots[key]["Button"].collidepoint(EventHandler.mousePosition()):
                if EventHandler.pressingLeftMouseButton() and not self.timer.activated:
                   print(f"Pressed the button on {key}")
                   addOrder(key,self.player)
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
        invBGColor = self.white
        invColor = self.black
        pg.draw.rect(self.screen,invBGColor,(invX,invY,invWidth,invHeight))
        pg.draw.rect(self.screen,invColor,(invX+5,invY+5,invWidth-10,invHeight-10))
        
        # Item Slots
        for key,item in self.itemSlots.items():
            # background
            pg.draw.rect(self.screen,invBGColor,(self.itemSlotPosX,item["Y"],self.slotWidth,self.slotHeight))
            # slots
            self.itemSlots[key]["Button"] = pg.draw.rect(self.screen,invColor,
                                            (self.itemSlotPosX+5,item["Y"]+5,
                                            self.slotWidth-10,self.slotHeight-10))
            # text
            self.screen.blit(item["Text"],(self.itemSlotPosX+20,item["Y"]+10))
            
            # sprite
            self.screen.blit(item["Sprite"],(self.itemSpriteXPos,item["Y"]))

            
    def renderUI(self):
        self.timer.update()
        self.renderPurchaseButton()
        self.handleInventoryRendering()
         
        self.handleMouseEvent()

