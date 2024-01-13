import sys
import pygame as pg
import ast
from settings import *
from eventhandler import EventHandler
from player import Player
from camera import CameraGroup
from support import *
from tile import Tile
from ui import UI
from npc import NPC
from menu import MainMenu

class Game:
    def __init__(self):
        pg.init()
        width,height = 700,500
        self.window = pg.display.set_mode((width,height))
        
        self.running = True
        self.FPS = 60
        self.clock = pg.time.Clock()

        self.visibleSprites = CameraGroup()
        self.collisionSprites = pg.sprite.Group()
        self.interactableSprites = pg.sprite.Group()
        

        self.menuScreen = MainMenu(self.startOverworld)
        self.createMap()
        
        self.currentScene = Scenes.MenuScreen
        
        self.scenes = {
            Scenes.Overworld : self.handleOverworldUpdates,
            Scenes.MenuScreen : self.menuScreen.update,

        }

        p1Pos = (240,130)
        self.player = Player(p1Pos,self.visibleSprites,self.collisionSprites,self.interactableSprites)

        NPC("Sprites/StoreClerk.png",(238,58),self.visibleSprites)

        fontPath = "Fonts/DeterminationMonoWebRegular-Z5oq.ttf"
        self.fontColor = (255,255,255)
        self.fpsFont = pg.font.Font(fontPath,18)

        self.ui = UI()
        
        pg.display.set_caption("PyRestaurant")

    def createMap(self):
        mapLayouts = {
            MapTiles.Walls: import_csv_layout("Map/wall.csv"),
            MapTiles.InteractableObjects: import_csv_layout("Map/interactableObjects.csv")    
        }

        self.tileSize = 16

        for style,layout in mapLayouts.items():
            for rowIndex,row in enumerate(layout):
                for columnIndex,column in enumerate(row):
                    if column != "-1":
                        x = columnIndex * self.tileSize
                        y = rowIndex * self.tileSize

                        if style == MapTiles.Walls:
                            Tile((x,y),[self.collisionSprites])

                        

    def displayFPS(self):
         fps = self.fpsFont.render(f"{round(self.clock.get_fps())}",True,self.fontColor)
         pos = (670,10)
         self.window.blit(fps,pos)

    def handleOverworldUpdates(self):
        self.visibleSprites.custom_draw(self.player)
        self.player.update()
        self.ui.renderUI()  

    def startOverworld(self):
        self.currentScene = Scenes.Overworld
        self.ui.player = self.menuScreen.currentPlayer()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    break

            self.window.fill("black")
            EventHandler.handlePlayerInput() 
            
            updateCurrentScene = self.scenes.get(self.currentScene)
            updateCurrentScene()
            
            self.displayFPS()
            pg.display.update()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
