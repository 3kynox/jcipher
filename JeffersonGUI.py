# -*- coding: utf-8 -*-
import sys, pygame
from JeffersonShell import *
from pygame.locals import *

pygame.init()

def main():
    # Init vars
    global n, selectedItems, keyList
    play_again = 1
    size = width, height = 800, 750
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0, 0, 0))
    font = pygame.font.Font('AgencyFB_Light_Wide.ttf', 20)
    selectedItems = {}
    keyList = []

    # Define later ability to load cylinder file
    cylinder = loadCylinder('cylinder.txt')
    n = len(cylinder)
    
    # Functions
    def displayCylinder(mySurface, cylinder, i):
        # Missing "Le bon endroit ..."
        x = 10
        y = 10
        text = ''
        
        for c in range(len(cylinder[i])):
            text = cylinder[i][c]
            renderText = font.render(text, 0, (249, 0, 0))
            mySurface.blit(renderText, (y, x))
            x = x + 25

    def displayCylinders(mySurface, cylinder):
        x = 10
        y = 10
        text = ''

        for i in range(1, n + 1):
            for c in range(len(cylinder[i])):
                text = cylinder[i][c]
                renderText = font.render(text, 0, (249, 0, 0))
                mySurface.blit(renderText, (y, x))
                x = x + 25
            x = 10
            y = y + 40

    def enterKey(mySurface, n):
        global wheelKeys
        x = 50 + (26 * 25)
        y = 10
        texts = []

        for key, value in cylinder.items():
            text = str(key)
            renderText = font.render(text, 0, (249, 0, 0))
            texts.append(renderText)
            renderSurface = mySurface.blit(renderText, (y, x))

            if event.type == MOUSEBUTTONDOWN and renderSurface.collidepoint(pygame.mouse.get_pos()):
                selectedItems[key] = value

                if key not in keyList:
                    keyList.append(key)

            if key in selectedItems:
                texts[key - 1] = font.render(text, 0, (255, 255, 255))
                
            renderSurface = mySurface.blit(texts[key - 1], (y, x))

            y = y + 40

        
        v = 10
        w = 80 + (26 * 25)

        for a in keyList:
            keyText = str(a)
            renderKey = font.render(keyText, 0, (255, 255, 255))
            mySurface.blit(renderKey, (v, w))
            v = v + 40

        text = 'ENTER THE KEY'
        renderText = font.render(text, 0, (249, 0, 0))
        mySurface.blit(renderText, (y + 25 , x))

        return keyList
                

    def rotateCylinder(cylinder, i, up = True):
        return True

    def rotateCylinders(mySurface, cylinder):
        return True

    # Main Loop
    while play_again:
        displayCylinders(surface, cylinder)
        
        # Events loop
        for event in pygame.event.get():
            # Manage quit / closing window event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            myKeyList = enterKey(surface, n)
        
        screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
