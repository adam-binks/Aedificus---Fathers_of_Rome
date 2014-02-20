import pygame, sys
pygame.init()
from pygame.locals import *

class Input:
    """A class to handle input accessible by all other classes"""
    def __init__(self):
        self.pressedKeys = []
        self.mousePressed = False
        self.mouseUnpressed = False
        self.mousePos = (0, 0)
        

    def get(self):
        """Update variables - mouse position and click state, and pressed keys"""
        self.checkForQuit()
        self.mouseUnpressed = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.event.post(event)
            elif event.type == KEYDOWN:
                self.pressedKeys.append(event.key)
            elif event.type == KEYUP:
                for key in self.pressedKeys:
                    if event.key == key:
                        self.pressedKeys.remove(key)
            elif event.type == MOUSEMOTION:
                self.mousePos = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                self.mousePressed = True
                self.mouseUnpressed = False
            elif event.type == MOUSEBUTTONUP:
                self.mousePressed = False
                self.mouseUnpressed = True


    def checkForQuit(self):
        """Terminate if QUIT events or K_ESCAPE"""
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self.terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back


    def terminate(self):
        """Safely end the program"""
        pygame.quit()
        sys.exit()