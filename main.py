from email import message_from_binary_file
from json.tool import main
import time
import sys
import pygame
from pygame.locals import *
import random


FPS = 32
SCREENWIDTH = 289

SCREENHEIGHT = 511

SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

GROUNDY = SCREENHEIGHT * 0.8

GAME_SPRITES = {}

GAME_SOUNDS = {}

PLAYER = 'gallery/sprites/bird.png'

BACKGROUND = 'gallery/sprites/background.png'

PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    playerx = int(SCREENWIDTH/2.5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_height())*2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN and (event.type == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0)) 
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery)) 
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey)) 
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY)) 
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()


    upperPipes

def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 *offset))
    pipex = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [{'x': pipex , 'y': -y1},#upper pipe
        {'x' : pipex, 'y': y2}
    ]
    return pipe


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Nick')
    GAME_SPRITES['numbers'] = (     
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),


    )
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()

    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),

        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        mainGame()
