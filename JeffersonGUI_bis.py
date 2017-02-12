# -*- coding: utf-8 -*-
import sys, pygame
from JeffersonShell import *
from pygame.locals import *

def main():
    class Wheel:
        hovered = False
        
        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()
                
        def draw(self):
            self.set_rend()
            surface.blit(self.rend, self.rect)
            
        def set_rend(self):
            for letter in range(len(self.text)):
                self.rend = font.render(self.text[letter], 0, self.get_color())
            
        def get_color(self):
            if self.hovered:
                return (255, 255, 255)
            else:
                return (249, 0, 0)
            
        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

    pygame.init()
    
    # Init vars
    global cylinder
    play_again = 1
    size = width, height = 800, 750
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0, 0, 0))
    font = pygame.font.Font('AgencyFB_Light_Wide.ttf', 20)
    cylinder = loadCylinder('cylinder.txt')
    n = len(cylinder)

    def displayCylinders(mySurface, myCylinder):
        global wheels
        wheels = []
        x = 10
        
        for i in range(1, n + 1):
            wheels.append(Wheel(myCylinder[i], (x, 10)))
            x = x + 20
            
    # Main Loop
    while play_again:
        displayCylinders(surface, cylinder)
        #enterKey(surface, n)

        for wheel in wheels:
            if wheel.rect.collidepoint(pygame.mouse.get_pos()):
                wheel.hovered = True
            else:
                wheel.hovered = False
            wheel.draw()
        
        # Events loop
        for event in pygame.event.get():
            # Manage quit / closing window event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
        