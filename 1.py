import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1200, 750))
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen.fill(WHITE)
clock=pygame.image.load("clock.jpg")
clock = pygame.transform.scale(clock, (clock.get_width()//1.2, clock.get_height()//1.2))
clock1 = clock.get_rect(bottomright=(1000,650))
screen.blit(clock, clock1)
pygame.display.update()
left=pygame.image.load("left.jpg")
left = pygame.transform.scale(left, (left.get_width()//1.2, left.get_height()//1.2))
left.set_colorkey(BLACK)
left_rect = left.get_rect(bottomright=(1150,740))
screen.blit(left,left_rect)
pygame.display.update()
right=pygame.image.load("right.jpg")
right = pygame.transform.scale(right, (right.get_width()//1.2, right.get_height()//1.2))
right.set_colorkey(BLACK)
right_rect = right.get_rect(bottomright=(1176,740))
screen.blit(right,right_rect)
pygame.display.update()


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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    left2 = pygame.transform.rotate(left,angle)
    new_rect =left2.get_rect(center = left.get_rect(topleft = (0,0)).center)
    angle+=1
    screen.blit(left2, new_rect)
    
    

    # screen.blit(get_image("left.jpg"),(0,0))

    pygame.display.flip()