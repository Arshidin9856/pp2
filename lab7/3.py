# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
# When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key.
# The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
import pygame
import os
pygame.init()
screen=pygame.display.set_mode((1000,700))
quit=True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x=50
y=50
while quit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit=False
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_UP :
                if y-20>=0+25 : y-=20
            if event.key==pygame.K_DOWN:
                if y+20<=500-25 : y+=20   
            if event.key==pygame.K_RIGHT:
                if x+20<=500-25 : x+=20
            if event.key==pygame.K_LEFT:
                if x-20>=25 : x-=20   
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_UP]:
    #    if y-20>=0+25 : y-=1            
    screen.fill((24,15,84))    
    pygame.draw.circle(screen,RED,(x,y),25)
    pygame.display.flip()
      
