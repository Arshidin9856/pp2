# Draw rectangle
# Draw circle
# Eraser
# Color selection
import pygame as pg
pg.init()
done=False 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
clockpy = pg.time.Clock()
w,h=700,500
color=BLACK
weights=1
class rectangle():
    def __init__(self):
        self.bo=False
        self.sp=None
        self.rect_b=False
        self.dx=0
        self.dy=0
        self.rect_list = []
        self.pos=0        
    def draw(self):
        if self.rect_b:
            self.dx=self.pos[0]-self.sp[0]
            self.dy=self.pos[1]-self.sp[1]        
            screen.fill(WHITE)
            for rect in range(0,len(self.rect_list),3):
                pg.draw.rect(screen,self.rect_list[rect+2], self.rect_list[rect],self.rect_list[rect+1])
            pg.draw.rect(screen,color,pg.Rect(self.sp[0],self.sp[1],self.dx,self.dy),weights)
            pg.display.update()    
    def Cloud(self):
            if self.rect_b:    
                self.dx,self.dy = self.pos[0]-self.sp[0], self.pos[1]-self.sp[1]
                rect = pg.Rect(self.sp[0],self.sp[1],self.dx,self.dy)
                self.rect_list.append(rect)
                self.rect_list.append(weights) 
                self.rect_list.append(color)
                self.rect_b=False
class circle():
    def __init__(self):
        self.bo=False
        self.rect_b=False
        self.sp=None
        self.cx=0
        self.cy=0
        self.rect_list = []
        self.pos=0
        self.rad=0        
    def draw(self):
        if self.rect_b:
          
            self.cx=self.pos[0]/2-self.sp[0]/2+self.sp[0]
            self.cy=self.pos[1]/2-self.sp[1]/2+self.sp[1]        
            self.rad=self.pos[1]/2-self.sp[1]/2
            screen.fill(WHITE)
            for rect in range(0,len(self.rect_list),5):
                pg.draw.circle(screen,self.rect_list[rect+4], (self.rect_list[rect],self.rect_list[rect+1]),self.rect_list[rect+2],self.rect_list[rect+3])
            pg.draw.circle(screen,color,(self.cx,self.cy),self.rad,weights)
            pg.display.update()    
    def Cloud(self):
            if self.rect_b:    
                self.cx,self.cy = self.pos[0]/2-self.sp[0]/2+self.sp[0],self.pos[1]/2-self.sp[1]/2+self.sp[1] 
                self.rad=self.pos[1]/2-self.sp[1]/2
                
                self.rect_list.append(self.cx)
                self.rect_list.append(self.cy)
                self.rect_list.append(self.rad)

                self.rect_list.append(weights) 
                self.rect_list.append(color)
                self.rect_b=False


screen=pg.display.set_mode((w,h))
screen.fill(WHITE)
pg.display.flip()


REC=rectangle()
CIR=circle()
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key==pg.K_F1:
                REC.bo=True if not REC.bo else False
            if event.key==pg.K_F2:
                CIR.bo=True if not CIR.bo else False
            if event.key == pg.K_q:
                screen.fill(WHITE)
                pg.display.update()
                REC.rect_list = []
                CIR.rect_list = []
                
                

                
            if event.key == pg.K_r:
                color =RED
            if event.key == pg.K_g:
                color =GREEN
            if event.key == pg.K_b:
                color =BLUE
            if event.key == pg.K_w:
                color =WHITE
            if event.key == pg.K_a:
                color =BLACK
            if event.key == pg.K_KP_MINUS:
                weights=max(weights-1,1)
            if event.key == pg.K_KP_PLUS:
                weights=min(200,weights+1)
                 
            
            
        if event.type == pg.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    if REC.bo:
                        REC.rect_b=True
                        REC.sp=event.pos
                    if CIR.bo:
                        CIR.rect_b=True
                        CIR.sp=event.pos
                    
                        

        if event.type == pg.MOUSEMOTION:
            REC.pos = event.pos
            REC.draw()
            CIR.pos=event.pos
            CIR.draw()  
           
             
        if event.type == pg.MOUSEBUTTONUP :
            if event.button == 1:
                REC.pos = event.pos
                REC.Cloud()
                CIR.pos=event.pos
                CIR.Cloud()
    if not (CIR.rect_b and  REC.rect_b) :                
        for rect in range(0,len(REC.rect_list),3):
                    pg.draw.rect(screen,REC.rect_list[rect+2], REC.rect_list[rect],REC.rect_list[rect+1])
        for rect in range(0,len(CIR.rect_list),5):
                    pg.draw.circle(screen,CIR.rect_list[rect+4], (CIR.rect_list[rect],CIR.rect_list[rect+1]),CIR.rect_list[rect+2],CIR.rect_list[rect+3])                
            

        pg.display.update()    

    clockpy.tick(60)