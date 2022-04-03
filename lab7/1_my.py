import pygame
import os
import math
pygame.init()
screen = pygame.display.set_mode((927, 777))
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen.fill(WHITE)
clockpy = pygame.time.Clock()
clock=pygame.image.load("clock.jpg")
left=pygame.image.load("left.jpg")
right=pygame.image.load("right.jpg")

screen.blit(clock,(0,0))
pygame.display.update()
# left.set_colorkey(BLACK)
# left.set_alpha(100)
pos1=(screen.get_rect().centerx,screen.get_rect().centery-130)
# screen.blit(left,(screen.get_rect().centerx,screen.get_rect().centery-130))
pygame.display.update()

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  
    # draw rectangle around the image
    # pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)








w, h = left.get_size()

angle=0
while running:
    clockpy.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    blitRotate(screen,left,pos1,(w/2,h/2),angle)
    angle+=1



    pygame.display.flip()