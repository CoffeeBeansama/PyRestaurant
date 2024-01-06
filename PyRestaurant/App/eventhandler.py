import pygame as pg

class EventHandler(object):
    
    pressingUp = False
    pressingDown = False
    pressingRight = False
    pressingLeft = False
    pressingMouseButton = False
    mousePos = None
    mousePressed = None


    @staticmethod
    def handlePlayerInput():
        keys = pg.key.get_pressed()

        EventHandler.mousePos = pg.mouse.get_pos()
        EventHandler.mousePressed = pg.mouse.get_pressed()

        EventHandler.pressingMouseButton = True if EventHandler.mousePressed[0] else False
        EventHandler.pressingUp = True if keys[pg.K_UP] else False
        EventHandler.pressingDown = True if keys[pg.K_DOWN] else False
        EventHandler.pressingLeft = True if keys[pg.K_LEFT] else False
        EventHandler.pressingRight = True if keys[pg.K_RIGHT] else False

    def mousePosition():
        return EventHandler.mousePos
    
    def pressingLeftMouseButton():
        return EventHandler.pressingMouseButton

    def pressingUpKey():
        return EventHandler.pressingUp

    def pressingDownKey():
        return EventHandler.pressingDown

    def pressingLeftKey():
        return EventHandler.pressingLeft

    def pressingRightKey():
        return EventHandler.pressingRight
