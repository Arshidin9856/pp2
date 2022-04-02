from tkinter import CENTER
import pygame
import os
import math
pygame.init()
screen = pygame.display.set_mode((1200, 750))
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen.fill(WHITE)
clockpy = pygame.time.Clock()
clock=pygame.image.load("clock.jpg")
clock = pygame.transform.scale(clock, (clock.get_width()//1.2, clock.get_height()//1.2))
# clock_rec=clock.get_rect(center=(600,325))
screen.blit(clock,(0,0))
pygame.display.update()
left=pygame.image.load("left.jpg")
left = pygame.transform.scale(left, (left.get_width()//1.2, left.get_height()//1.2))
w, h = left.get_size()
left.set_alpha(152)
# screen.blit(left,(clock.get_rect().center[0],clock.get_rect().center[0]-h/2-h+15))
pygame.display.update()
right=pygame.image.load("right.jpg")
right = pygame.transform.scale(right, (right.get_width()//1.2, right.get_height()//1.2))
w1, h1 = right.get_size()
right.set_alpha(152)

screen.blit(right,(clock.get_rect().center[0]-w1+15+20+5,clock.get_rect().center[0]-h1/2-h1+10))
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
    pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)
    

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)



# _image_library={}
# def get_image(path):
#     global _image_library
#     image = _image_library.get(path)
#     if image is None:
#         canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#         image = pygame.image.load(canonicalized_path)
#         _image_library[path] = image
#     return image
angle=0
while running:
    clockpy.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pos = (screen.get_width()/2, screen.get_height()/2)
    blitRotate(screen,left, pos,(w,h), angle)
    # blitRotate(screen,right, pos, (w1/2, h1/2), angle)
    
    angle+=1
    
    
    pygame.display.flip()