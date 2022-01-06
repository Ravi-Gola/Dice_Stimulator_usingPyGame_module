import random
import pygame
import sys
from pygame.locals import *
FPS = 32
SCREENWIDTH = 327
SCREENHIEGHT = 581
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHIEGHT))#set screen dimensions of game window

def welcomeScreen():
        """ this function is for only welcome screen """
        while True:
                for event in pygame.event.get():#event handling of pygame
                        if event.type  == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                return

                        else:
                           SCREEN.blit(background, (0, 0))#blit backgound image in screen
                           pygame.display.update()
                           FPS_CLOCK.tick(FPS)

def maingame():

        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.KEYDOWN and(event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                                ans_dice = random.choice(phases_list)#randomly take face one by one from list using random.choice
                                SCREEN.blit(maingame_bg, (0, 0))#blit image on screen
                                SCREEN.blit(ans_dice, (95, 200))
                                pygame.display.update()#update pygame window
                                FPS_CLOCK.tick(FPS)#update FPS




if __name__ == '__main__':
        pygame.init() # initialise the screen
        pygame.display.set_caption("Dice Stimulator")#set caption
        FPS_CLOCK = pygame.time.Clock()#set FPS
        background=pygame.image.load('gameimg/dice_game_bg.png').convert()#load background image in a variable by using pygame load function
        maingame_bg=pygame.image.load('gameimg/dice_maingame_bg.jpg').convert()#load main game background image
        phase1=pygame.image.load('gameimg/phase 1.jpg').convert()#load dice face 1
        phase2=pygame.image.load('gameimg/phase 2.jpg').convert()#load dice face 2
        phase3=pygame.image.load('gameimg/phase 3.jpg').convert()#load dice face 3
        phase4=pygame.image.load('gameimg/phase 4.jpg').convert()#load dice face 4
        phase5=pygame.image.load('gameimg/phase 5.jpg').convert()#load dice face 5
        phase6=pygame.image.load('gameimg/phase 6.jpg').convert()#load dice face 6
        phases_list=[phase1,phase2,phase3,phase4,phase5,phase6]#make list of all faces
        """function call"""
        welcomeScreen()
        maingame()