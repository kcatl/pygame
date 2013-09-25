import sys, pygame
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()


displaysurf = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Animation')

white = (255,255,255)
pic = pygame.image.load('hello.jpg')
catx = 10
caty = 10
direction = 'right'



#the while loop part:
while True:
    displaysurf.fill(white)
    
    if direction == 'right':
        catx += 5
        if catx == 350:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 250:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction =  'right'
    
    displaysurf.blit(pic,(catx,caty))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)