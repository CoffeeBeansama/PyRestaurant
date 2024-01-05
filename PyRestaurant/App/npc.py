import pygame as pg
from support import loadSprite,import_folder

class NPC(pg.sprite.Sprite):
    def __init__(self,image,pos,groups):
        super().__init__(groups)
        self.image = pg.image.load(f"{image}").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
