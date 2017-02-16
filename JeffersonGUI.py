# -*- coding: utf-8 -*-
import sys, pygame
from JeffersonShell import *
from pygame.locals import *

pygame.init()

def main():
    # Init vars
    global size, screen, surface, n, selectedItems, keyList, myKeyList, reloadRender
    play_again = 1
    fontSmall = pygame.font.Font('AgencyFB_Light_Wide.ttf', 15)
    font = pygame.font.Font('AgencyFB_Light_Wide.ttf', 20)
    fontBig = pygame.font.Font('AgencyFB_Light_Wide.ttf', 30)
    selectedItems = {}
    keyList = []
    myKeyList = []
    keyComplete = 0
    cipherMode = 0
    file = 'cylinder.txt'
    cylinder = loadCylinder(file)
    newCylinder = {}

    # The screen size depends of the disks count in opened file
    size = width, height = ((len(cylinder) * 40 + 220), 760)
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0, 0, 0))
    
    # Functions
    # Add a wheel to the game area and save it to file
    def addWheel(mySurface, cylinder):
        createCylinder(file, (n + 1))
        # Reload app on addWheel()
        main()

    # Remove a wheel from the game area ...
    def delWheel(mySurface, cylinder):
        createCylinder(file, (n - 1))
        # Reload app on delWheel()
        main()

    # Display a cylinder (defined by i) on the "right" place in mySurface
    def displayCylinder(mySurface, cylinder, i):
        dictLen = len(newCylinder)
        newCylinder[dictLen + 1] = cylinder[i]
        if len(newCylinder) == n:
            cylinder = newCylinder
            mySurface.fill((0, 0, 0), (0, 0, 800, 720))
            return cylinder

    # Display all cylinders on mySurface
    def displayCylinders(mySurface, cylinder):
        x = 10
        y = 10
        text = ''

        # Displays all letters contained in file, line by line on surface
        for i in range(1, n + 1):
            for c in range(len(cylinder[i])):
                text = cylinder[i][c]
                renderText = font.render(text, 0, (249, 0, 0))
                mySurface.blit(renderText, (y, x))
                # Increment x to display vertically letters
                x = x + 25

            # x back to origin value and moving to next column (y)
            x = 10
            y = y + 40

        # Give ability to add / remove wheels while the key have not been yet defined
        if cipherMode == 0:
            addWheelText = fontSmall.render("ADD WHEEL |", True, (249, 0, 0))
            delWheelText = fontSmall.render("DEL WHEEL", True, (249, 0, 0))
            addWheelSurface = surface.blit(addWheelText, ((len(cylinder) * 41),735,100,20))
            delWheelSurface = surface.blit(delWheelText, ((len(cylinder) * 41 + 100),735,100,20))

            # Add / remove wheels buttons events
            if event.type == MOUSEBUTTONDOWN and addWheelSurface.collidepoint(pygame.mouse.get_pos()):
                cylinder = addWheel(mySurface, cylinder)
                return cylinder

            if event.type == MOUSEBUTTONDOWN and delWheelSurface.collidepoint(pygame.mouse.get_pos()):
                cylinder = delWheel(mySurface, cylinder)
                return cylinder
        else: # Secret word selection activated, hide add / remove wheels buttons
            mySurface.fill((0, 0, 0), (len(cylinder) * 41, 735, 200, 20))

        return cylinder

    # Displays disk numbers, wait for key selection and return it when completed
    def enterKey(mySurface, n):
        global wheelKeys
        x = 50 + (26 * 25)
        y = 10
        texts = []

        # key is retrieved and displayed below the associated disk
        for key, value in cylinder.items():
            text = str(key)
            renderText = font.render(text, 0, (249, 0, 0))
            texts.append(renderText)
            renderSurface = mySurface.blit(renderText, (y, x))

            # Define click event on displayed key
            if event.type == MOUSEBUTTONDOWN and renderSurface.collidepoint(pygame.mouse.get_pos()):
                selectedItems[key] = value

                # Add the key in keyList
                if key not in keyList:
                    keyList.append(key)

            # Highlight the new inserted key
            if key in selectedItems:
                texts[key - 1] = font.render(text, 0, (255, 255, 255))
                
            renderSurface = mySurface.blit(texts[key - 1], (y, x))

            y = y + 40

        # Display below selected keys in the correct order
        v = 10
        w = 80 + (26 * 25)

        for a in keyList:
            keyText = str(a)
            renderKey = font.render(keyText, 0, (249, 0, 0))
            mySurface.blit(renderKey, (v, w))
            v = v + 40

        return keyList
                
    # Modify cylinder at a up or down position
    def rotateCylinder(cylinder, i, up = True):
        a = 1
        myNewCylinder = {}
        myStr = ''

        # One disk is processed, other disk before are added to myNewCylinder
        while a < i:
            myNewCylinder[a] = cylinder[a]
            a += 1    

        # Down move
        if up == False:
            for x in range(len(cylinder[i])):
                # Outside dict size
                if x == 25:
                    break

                # cylinder last letter moved at first myStr position
                if x == 0:
                    myStr += cylinder[i][25]

                # Add the rest of letters to myStr
                myStr += cylinder[i][x]
            myNewCylinder.update({i:myStr})

        # Up move
        if up == True:
            for x in range(len(cylinder[i])):
                if x == 25:
                    # Last myStr position got first cylinder letter 
                    myStr += cylinder[i][0]
                else:
                    # Rest of letters that we decals to x + 1
                    myStr += cylinder[i][x + 1]
            myNewCylinder.update({i:myStr})

        # Rest of disks after the current one beeing modified are added to myNewCylinder
        a += 1
        while a <= n:
            myNewCylinder[a] = cylinder[a]
            a += 1
        
        return myNewCylinder

    # Rendering cylinders rotation
    def rotateCylinders(mySurface, cylinder):
        x = 2
        y = 20 + (26 * 25)

        # Draw Texts and Lines for CLEAR and CYPHER Texts areas
        clearText = 'CLEAR'
        cipherText = 'CIPHER'
        
        renderClearText = font.render(clearText, 0, (249, 0, 0))
        renderCipherText = font.render(cipherText, 0, (249, 0, 0))
        surface.blit(renderClearText, ((len(cylinder) * 42), 235))
        surface.blit(renderCipherText, ((len(cylinder) * 42), 385))
        
        pygame.draw.line(surface, (254, 0, 0), (5, 230), ((len(cylinder) * 40), 230))
        pygame.draw.line(surface, (254, 0, 0), (5, 255), ((len(cylinder) * 40), 255))
        pygame.draw.line(surface, (254, 0, 0), (5, 380), ((len(cylinder) * 40), 380))
        pygame.draw.line(surface, (254, 0, 0), (5, 405), ((len(cylinder) * 40), 405))

        # Define arrows to rotate disks
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

            # Add click events to this new arrows buttons
            if event.type == MOUSEBUTTONDOWN and upRender.collidepoint(pygame.mouse.get_pos()):
                # Call rotateCylinder() function
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
        # Define n
        n = len(cylinder)
        
        # Events loop
        for event in pygame.event.get():
            # Manage quit / closing window event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Display cylinder at every loop and save it
            cylinder = displayCylinders(surface, cylinder)

            # "Enter the Key" mode
            if len(myKeyList) != n:
                myKeyList = enterKey(surface, n)
                text = 'ENTER THE KEY'
                renderText = font.render(text, 0, (249, 0, 0))
                surface.blit(renderText, ((len(cylinder) * 42), 700))
            else:
                # Key entered now let's rotate cylinders
                cipherMode = 1
                surface.fill((0, 0, 0), ((len(cylinder) * 42), 700, 150, 20))
                text = 'FINISH'

                # Using the key to place cylinders in correct order
                while keyComplete < n:
                    for key in myKeyList:
                        someCylinder = displayCylinder(surface, cylinder, key)
                        keyComplete += 1
                    cylinder = someCylinder
                cylinder = rotateCylinders(surface, cylinder)
                renderText = font.render(text, 0, (249, 0, 0))
                finishRender = surface.blit(renderText, ((len(cylinder) * 42), 700))

                # Finish button event to store the key, cypher and clear texts
                if event.type == MOUSEBUTTONDOWN and finishRender.collidepoint(pygame.mouse.get_pos()):
                    # Create Reload button
                    text = 'RELOAD'
                    renderText = font.render(text, 0, (249, 0, 0))
                    reloadRender = surface.blit(renderText, ((len(cylinder) * 42), 670))
                    fileSave = open('myCipher.txt', "w")
                    output = 'CLEAR PHRASE  : '
                    
                    for i in range(1, n + 1):
                        for c in range(len(cylinder[i])):
                            if c == 9:
                                output += cylinder[i][c]

                    output += '\nCIPHER PHRASE : '
                    
                    for i in range(1, n + 1):
                        for c in range(len(cylinder[i])):
                            if c == 15:
                                output += cylinder[i][c]
                    
                    output += '\nKEY CHAIN     : '
                    output += str(myKeyList)

                    fileSave.write(output)
                    fileSave.close()

                # Reload button event that reload main program
                try:
                  if event.type == MOUSEBUTTONDOWN and reloadRender.collidepoint(pygame.mouse.get_pos()):
                        main()
                except NameError:
                  continue
        
        screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
