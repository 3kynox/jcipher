# -*- coding: utf-8 -*-
import sys, pygame
from JeffersonShell import *
from pygame.locals import *

pygame.init()

def main():
    # Init vars
    play_again = 1
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0, 0, 0))
    font = pygame.font.Font('AgencyFB_Light_Wide.ttf', 36)
    
    # Functions
    def displayCylinder(mySurface, cylinder, i):
        return True

    def displayCylinders(mySurface, cylinder):
        return True

    def enterKey(mySurface, n):
        return True

    def rotateCylinder(cylinder, i, up = True):
        return True

    def rotateCylinders(mySurface, cylinder):
        return True

    # Main Loop
    while play_again:
        text = font.render("GDILVJJNHS", 1, (249, 0, 0))
        textpos = text.get_rect(centerx=surface.get_width()/2)
        surface.blit(text, textpos)
        
        # Events loop
        for event in pygame.event.get():
            # Manage quit / closing window event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
        
