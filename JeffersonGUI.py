# -*- coding: utf-8 -*-
import sys, pygame
from JeffersonShell import *
from pygame.locals import *

pygame.init()

def main():
    # Init vars
    global n, selectedItems, keyList, myKeyList
    play_again = 1
    size = width, height = 800, 750
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0, 0, 0))
    font = pygame.font.Font('AgencyFB_Light_Wide.ttf', 20)
    fontBig = pygame.font.Font('AgencyFB_Light_Wide.ttf', 30)
    selectedItems = {}
    keyList = []
    myKeyList = []
    keyComplete = 0

    # Define later ability to load cylinder file
    cylinder = loadCylinder('cylinderWiki.txt')
    n = len(cylinder)
    newCylinder = {}
    
    # Functions
    def displayCylinder(mySurface, cylinder, i):
        dictLen = len(newCylinder)
        newCylinder[dictLen + 1] = cylinder[i]
        if len(newCylinder) == n:
            cylinder = newCylinder
            mySurface.fill((0, 0, 0), (0, 0, 800, 720))
            return cylinder

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
            renderKey = font.render(keyText, 0, (249, 0, 0))
            mySurface.blit(renderKey, (v, w))
            v = v + 40

        return keyList
                

    def rotateCylinder(cylinder, i, up = True):
        a = 1
        myNewCylinder = {}
        myStr = ''

        while a < i:
            myNewCylinder[a] = cylinder[a]
            a += 1    
        
        if up == False:
            for x in range(len(cylinder[i])):
                if x == 25:
                    break
                if x == 0:
                    myStr += cylinder[i][25]

                myStr += cylinder[i][x]
            myNewCylinder.update({i:myStr})

        if up == True:
            for x in range(len(cylinder[i])):
                if x == 25:
                    myStr += cylinder[i][0]
                else:
                    myStr += cylinder[i][x + 1]
            myNewCylinder.update({i:myStr})

        a += 1
        while a <= n:
            myNewCylinder[a] = cylinder[a]
            a += 1
        
        return myNewCylinder

    def rotateCylinders(mySurface, cylinder):
        x = 2
        y = 20 + (26 * 25)
        
        clearText = 'CLEAR'
        cipherText = 'CIPHER'
        
        renderClearText = font.render(clearText, 0, (249, 0, 0))
        renderCipherText = font.render(cipherText, 0, (249, 0, 0))
        surface.blit(renderClearText, (410 , 235))
        surface.blit(renderCipherText, (410 , 385))
        
        pygame.draw.line(surface, (254, 0, 0), (5, 230), (395, 230))
        pygame.draw.line(surface, (254, 0, 0), (5, 255), (395, 255))
        pygame.draw.line(surface, (254, 0, 0), (5, 380), (395, 380))
        pygame.draw.line(surface, (254, 0, 0), (5, 405), (395, 405))
        
        for key, value in cylinder.items():
            upArrow = '>'
            downArrow = '<'
            upRender = fontBig.render(upArrow, 0, (249, 0, 0))
            upRender = pygame.transform.rotate(upRender, 90)
            downRender = fontBig.render(downArrow, 0, (249, 0, 0))
            downRender = pygame.transform.rotate(downRender, 90)
            upRender = mySurface.blit(upRender, (x, y))
            downRender = mySurface.blit(downRender, (x + 1, y + 25))
            x = x + 40

            if event.type == MOUSEBUTTONDOWN and upRender.collidepoint(pygame.mouse.get_pos()):
                cylinder = rotateCylinder(cylinder, key, True)
                mySurface.fill((0, 0, 0), (0, 0, 800, 720))
                return cylinder

            if event.type == MOUSEBUTTONDOWN and downRender.collidepoint(pygame.mouse.get_pos()):
                cylinder = rotateCylinder(cylinder, key, False)
                mySurface.fill((0, 0, 0), (0, 0, 800, 720))
                return cylinder
        return cylinder

    # Main Loop
    while play_again:
        displayCylinders(surface, cylinder)
        
        # Events loop
        for event in pygame.event.get():
            # Manage quit / closing window event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if len(myKeyList) != n:
                myKeyList = enterKey(surface, n)
                text = 'ENTER THE KEY'
            else:
                text = 'FINISH'
                while keyComplete < n:
                    for key in myKeyList:
                        someCylinder = displayCylinder(surface, cylinder, key)
                        keyComplete += 1
                    cylinder = someCylinder
                cylinder = rotateCylinders(surface, cylinder)
        
            renderText = font.render(text, 0, (249, 0, 0))
            surface.blit(renderText, (410 , 700))
        
        screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
