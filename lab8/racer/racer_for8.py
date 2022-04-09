# Adding randomly appearing coins on the road
# Showing the number of collected coins in the top right corner

from glob import glob
import pygame as pg,random,time,sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pg.init()
phon=pg.image.load("AnimatedStreet.png")
w,h=phon.get_size()
score=0
speed=5
screen=pg.display.set_mode((w,h))
screen.blit(phon,(0,0))

rect=phon.get_rect()
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# pos_x = 0
# def road(speed) :
    # global pos_x
    # rect.move_ip(0,speed)
    # pos_x+=speed    
    
    # x_rel = pos_x % h
    # x_part2 = x_rel - h if x_rel > 0 else x_rel + h
    # screen.blit(phon, (0, x_rel))
    # screen.blit(phon, (0,x_part2))
    # pg.display.update()
class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.x,self.y=self.image.get_size()
        self.rect.center = (random.randint(20,w-self.x), 0)

      def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > h):
            self.rect.top = 0
            self.rect.center = (random.randint(20, w - self.x), 0)
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.x=w/2
        self.y=h-50
        self.rect.center = (self.x,self.y)
       
    def move(self):
        pressed_keys = pg.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[pg.K_LEFT]:
                  self.x+=-5
                  self.rect.move_ip(-5, 0)
        if self.rect.right < w:        
              if pressed_keys[pg.K_RIGHT]:
                  self.x+=5
                  self.rect.move_ip(5, 0)
coin_cnt=0
class Coins(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.size=15
        self.x=random.randint(15,w-15)
        self.y=15
    def draw(self):
        pg.draw.circle(screen, (249,166,2), (self.x, self.y), self.size) 
        
    def move(self):
        global coin_cnt
        self.y += speed
        if pg.Rect.collidepoint(P1.rect,self.x,self.y):
            coin_cnt+=1
            self.x=random.randint(15,w-15)
            self.y=15
        if (self.y > h-15):
            self.x=random.randint(15,w-15)
            self.y=15
            
            
       
P1 = Player()
E1 = Enemy()
C=Coins()
# Creating Sprites Groups
# Co=pg.sprite.Group()
# Co.add(C)
# Co.add(C)
# Co.add(Coins())
Coins_list=[Coins(),Coins()]


enemies = pg.sprite.Group()
enemies.add(E1)
all_sprites = pg.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
running = True
k=1
clockpy = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if coin_cnt==5*k :
        speed += 0.5
        k+=1    
    # road(speed)


    for i in Coins_list:
        i.move()
    screen.blit(phon,(0,0))
    for i in Coins_list:
        i.draw()
    
    coins = font_small.render(f"Coins--{coin_cnt}", True, BLACK)
    screen.blit(coins, (w-150,10))
    
    # scores = font_small.render(str(score), True, BLACK)
    # screen.blit(scores, (10,10))
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
        
    if pg.sprite.spritecollideany(P1, enemies):
          pg.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          screen.fill(RED)
          screen.blit(game_over, (30,250))
          
          pg.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pg.quit()
          sys.exit()        
        
   
    clockpy.tick(60)
    pg.display.flip()