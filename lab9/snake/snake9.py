import pygame
import random
import time 
# Randomly generating food with different weights
# Foods which are disappearing after some time(timer)
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Surface
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)

BLOCK_SIZE = 20

score = 0
clock = pygame.time.Clock()
FPS = 3

def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)


class Wall:
    def __init__(self):
        self.body_wall = []
        self.level=1
        self.load_wall()
    
    def load_wall(self ):
        with open(f'level{self.level}.txt', 'r') as f:
            wall_body = f.readlines()
        
        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
                if value == '#':
                    self.body_wall.append([j, i])
    
    def draw(self):
        for x, y in self.body_wall:
            pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    def levelup(self):
        self.body_wall=[]
        if self.level<2:
            self.level+=1
        self.load_wall()
wall = Wall()
class Snake:
    def __init__(self):
        self.body = [[10, 10], [11, 10]]
        self.dx = 1
        self.dy = 0
        self.go=False
    def draw(self):
        for i, (x, y) in enumerate(self.body):
            color = RED if i == 0 else GREEN
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        # print(self.body)
        self.INscreen()
        if (self.body[0]) in  wall.body_wall: 
            self.go=True
        if self.body[0] in self.body[1:]:
            self.go=True     
    def INscreen(self):
        if self.body[0][0]*BLOCK_SIZE > 500:
            self.body[0][0] = 0
        if self.body[0][0] < 0:
            self.body[0][0]  = 500/BLOCK_SIZE 
        if self.body[0][1]*BLOCK_SIZE > 500:
            self.body[0][1] = 0
        if self.body[0][1] < 0:
            self.body[0][1] = 500/BLOCK_SIZE
snake = Snake()
i=4
class Food:
    def __init__(self):
        self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
        self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
        self.dx = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
        self.dy = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
       
        self.cnt=0
        self.generate_random_pos()
    def my_round(self, value, base=BLOCK_SIZE):
        return base * round(value / base)
    
    def generate_random_pos(self):
        self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
        self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
        
        while (self.x,self.y) in wall.body_wall and (self.x,self.y) in snake.body:
            self.x = self.my_round(random.randint(0,WINDOW_WIDTH - BLOCK_SIZE))
            self.y = self.my_round(random.randint(0,WINDOW_HEIGHT- BLOCK_SIZE))
        

    def draw(self):
        if self.cnt==25:
            self.dx = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
            self.dy = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
            
            while (self.x,self.y) in wall.body_wall and (self.x,self.y) in snake.body:
                self.dx = self.my_round(random.randint(0,WINDOW_WIDTH - BLOCK_SIZE))
                self.dy = self.my_round(random.randint(0,WINDOW_HEIGHT- BLOCK_SIZE))
                    
            self.x=self.dx
            self.y=self.dy        

            self.cnt=0
        self.cnt+=1
        pygame.draw.rect(screen, BLUE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
    def eat(self):
        global score,i,FPS
        if snake.body[0][0] * BLOCK_SIZE == self.x and snake.body[0][1] * BLOCK_SIZE == self.y:
            # print("EATEn")
            snake.body.append([0, 0])
            self.generate_random_pos()
            self.cnt=0
            score += 1
        if score >= i:
            wall.levelup()
            FPS+=1
            i=i*2
    def dis(self):
        self.generate_random_pos()
class Food1:
    def __init__(self):
        self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
        self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
        
        self.dx = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
        self.dy = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
        self.cnt=0
        self.generate_random_pos()
        
    def my_round(self, value, base=BLOCK_SIZE):
        return base * round(value / base)
    
    def generate_random_pos(self):
        self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
        self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
        
        while (self.x,self.y) in wall.body_wall and (self.x,self.y) in snake.body:
            self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
            self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
        

    def draw(self):
        if self.cnt==25:
            self.dx = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
            self.dy = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
            
            while (self.x,self.y) in wall.body_wall and (self.x,self.y) in snake.body:
                self.dx = self.my_round(random.randint(0,WINDOW_WIDTH - BLOCK_SIZE))
                self.dy = self.my_round(random.randint(0,WINDOW_HEIGHT- BLOCK_SIZE))
                    
            self.x=self.dx
            self.y=self.dy        

            self.cnt=0
        self.cnt+=1
        pygame.draw.rect(screen, GREEN, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
    def eat(self):
        global score,i,FPS
        if snake.body[0][0] * BLOCK_SIZE == self.x and snake.body[0][1] * BLOCK_SIZE == self.y:
            self.cnt=0
            # print("EATEn")
            snake.body.append([0, 0])
            self.generate_random_pos()
            score += 2
        if score >= i :
            wall.levelup()
            FPS+=1
            i=i*2
    


    
        
      


food = Food()
food1=Food1()

r=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if snake.dx!= -1 and snake.dy!=0:  
                    snake.dx = 1
                    snake.dy = 0
            if event.key == pygame.K_LEFT:
                if snake.dx!= 1 and snake.dy!=0:  
                    snake.dx = -1
                    snake.dy = 0
            if event.key == pygame.K_UP:
                if snake.dx!= 0 and snake.dy!=1:  
                    snake.dx = 0
                    snake.dy = -1
            if event.key == pygame.K_DOWN:
                if snake.dx!= 0 and snake.dy!=-1:  
                    snake.dx = 0
                    snake.dy = 1
    snake.move()    
    
    screen.fill(BLACK)
  
    draw_grid()
    wall.draw()
    snake.draw()
    food1.draw()
    food.draw()
    
    food1.eat()
    
    food.eat()
    
    font = pygame.font.Font(None, 100)
  
    font1 = pygame.font.Font(None, 30)

    text = font1.render(f'Score: {score}', True, (255, 0, 0))
    lev=font1.render(f"Level: {wall.level}", True ,(255,0,0))
    game_over=font.render("GAME_OVER",True,(BLACK))
    screen.blit(text, (20, 20))
    screen.blit(lev, (360, 20))

    if not r:
        running=False     
        pygame.time.wait(1000)

    if snake.go:
        pygame.draw.rect(screen,RED,(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
        screen.blit(game_over,(50,100))
        r=False

    pygame.display.update()
    clock.tick(FPS)