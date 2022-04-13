# Draw square
# Draw right triangle
# Draw equilateral triangle
# Draw rhombus

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
class square():
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
            self.dy=self.dx
            screen.fill(WHITE)
            for rect in range(0,len(self.rect_list),3):
                pg.draw.rect(screen,self.rect_list[rect+2], self.rect_list[rect],self.rect_list[rect+1])
            pg.draw.rect(screen,color,pg.Rect(self.sp[0],self.sp[1],self.dx,self.dy),weights)
            
            pg.display.update()    
    def Cloud(self):
            if self.rect_b:    
                self.dx,self.dy = self.pos[0]-self.sp[0],self.dx
                rect = pg.Rect(self.sp[0],self.sp[1],self.dx,self.dy)
                self.rect_list.append(rect)
                self.rect_list.append(weights) 
                self.rect_list.append(color)
                self.rect_b=False
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
class right_tr():
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
            self.dx = self.sp[0]
            self.dy=self.pos[1]
            screen.fill(WHITE)
            for rect in range(0,len(self.rect_list),3):
                pg.draw.lines(screen,self.rect_list[rect+2],True, (self.rect_list[rect][0],self.rect_list[rect][1],self.rect_list[rect][2]),self.rect_list[rect+1])
            pg.draw.lines(screen,color,True,([self.sp,self.pos,[self.dx,self.dy]]),weights)
            
            pg.display.update()    
    def Cloud(self):
            if self.rect_b:    
                self.dx,self.dy =self.sp[0],self.pos[1]
                rect = [self.sp,self.pos,(self.dx,self.dy)]
                self.rect_list.append(rect)
                self.rect_list.append(weights) 
                self.rect_list.append(color)
                self.rect_b=False
class equal_tr():
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
            self.dx =self.pos[0]/2-self.sp[0]/2 +self.sp[0]
            self.dy= self.sp[1]
            screen.fill(WHITE)
            for rect in range(0,len(self.rect_list),3):
                pg.draw.lines(screen,self.rect_list[rect+2],True, (self.rect_list[rect][0],self.rect_list[rect][1],self.rect_list[rect][2]),self.rect_list[rect+1])
            pg.draw.lines(screen,color,True,(self.pos,[self.sp[0],self.pos[1]],[self.dx,self.dy]),weights)
            
            pg.display.update()    
    def Cloud(self):
            if self.rect_b:    
                self.dx =(self.pos[0]-self.sp[0])/2 +self.sp[0]
                self.dy= self.sp[1]
                rect = [[self.dx,self.dy],self.pos,[self.sp[0],self.pos[1]]]
                self.rect_list.append(rect)
                self.rect_list.append(weights) 
                self.rect_list.append(color)
                self.rect_b=False
class rhombus():
    def __init__(self):
        self.bo=False
        self.sp=None
        self.rect_b=False
        self.dx=0
        self.dy=0
        self.cx=0
        self.cy=0
        self.zx=0
        self.zy=0
        self.wx=0
        self.wy=0

        self.rect_list = []
        self.pos=0        
    def draw(self):
        if self.rect_b:
            self.dx =self.pos[0]/2-self.sp[0]/2 +self.sp[0]
            self.dy= self.sp[1]
            self.cx=self.sp[0]
            self.cy=self.sp[1]+self.pos[1]/2-self.sp[1]/2
            self.zx=self.pos[0]
            self.zy=self.cy
            self.wx=self.dx
            self.wy=self.pos[1]
            screen.fill(WHITE)
            for rect in range(0,len(self.rect_list),3):
                pg.draw.lines(screen,self.rect_list[rect+2],True, (self.rect_list[rect][0],self.rect_list[rect][2],self.rect_list[rect][3],self.rect_list[rect][1]),self.rect_list[rect+1])
            pg.draw.lines(screen,color,True,([self.dx,self.dy],[self.cx,self.cy],[self.wx,self.wy],[self.zx,self.zy]),weights)
            
            pg.display.update()    
    def Cloud(self):
            if self.rect_b:
                self.dx =self.pos[0]/2-self.sp[0]/2 +self.sp[0]
                self.dy= self.sp[1]
                self.cx=self.sp[0]
                self.cy=self.sp[1]+self.pos[1]/2-self.sp[1]/2
                self.zx=self.pos[0]
                self.zy=self.cy
                self.wx=self.dx
                self.wy=self.pos[1]
                rect = [[self.dx,self.dy],[self.zx,self.zy],[self.cx,self.cy],[self.wx,self.wy]]
                self.rect_list.append(rect)
                self.rect_list.append(weights) 
                self.rect_list.append(color)
                self.rect_b=False


screen=pg.display.set_mode((w,h))
screen.fill(WHITE)


REC=rectangle()
CIR=circle()
SQR=square()
R_TR=right_tr()
EQ_TR=equal_tr()
ROMB=rhombus()
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key==pg.K_F1:
                REC.bo=True if not REC.bo else False
            if event.key==pg.K_F2:
                CIR.bo=True if not CIR.bo else False
            if event.key==pg.K_F3:
                SQR.bo=True if not SQR.bo else False
            if event.key==pg.K_F4:
                R_TR.bo=True if not R_TR.bo else False
            if event.key==pg.K_F5:
                EQ_TR.bo=True if not EQ_TR.bo else False
            if event.key==pg.K_F6:
                ROMB.bo=True if not ROMB.bo else False
            if event.key == pg.K_q:
                screen.fill(WHITE)
                pg.display.update()
                REC.rect_list = []
                CIR.rect_list = []
                SQR.rect_list = []
                R_TR.rect_list = []
                EQ_TR.rect_list = []
                ROMB.rect_list = []
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
                    if SQR.bo:
                        SQR.rect_b=True
                        SQR.sp=event.pos
                    if R_TR.bo:
                        R_TR.rect_b=True
                        R_TR.sp=event.pos                        
                    if EQ_TR.bo:
                        EQ_TR.rect_b=True
                        EQ_TR.sp=event.pos
                    if ROMB.bo:
                        ROMB.rect_b=True
                        ROMB.sp=event.pos
        
        if event.type == pg.MOUSEMOTION:
            REC.pos = event.pos
            REC.draw()
            CIR.pos=event.pos
            CIR.draw()  
            SQR.pos=event.pos
            SQR.draw()
            R_TR.pos=event.pos                        
            R_TR.draw()
            EQ_TR.pos=event.pos
            EQ_TR.draw()
            ROMB.pos=event.pos
            ROMB.draw()
        if event.type == pg.MOUSEBUTTONUP :
            if event.button == 1:
                REC.pos = event.pos
                REC.Cloud()
                CIR.pos=event.pos
                CIR.Cloud()
                SQR.pos=event.pos
                SQR.Cloud()
                R_TR.pos=event.pos
                R_TR.Cloud()
                EQ_TR.pos=event.pos
                EQ_TR.Cloud()
                ROMB.pos=event.pos
                ROMB.Cloud()
    if not (CIR.rect_b and  REC.rect_b and SQR.rect_b and R_TR.rect_b and EQ_TR.rect_b and ROMB.rect_b ) :                
        for rect in range(0,len(REC.rect_list),3):
                    pg.draw.rect(screen,REC.rect_list[rect+2], REC.rect_list[rect],REC.rect_list[rect+1])
        for rect in range(0,len(CIR.rect_list),5):
                    pg.draw.circle(screen,CIR.rect_list[rect+4], (CIR.rect_list[rect],CIR.rect_list[rect+1]),CIR.rect_list[rect+2],CIR.rect_list[rect+3])                
        for rect in range(0,len(SQR.rect_list),3):
                    pg.draw.rect(screen,SQR.rect_list[rect+2], SQR.rect_list[rect],SQR.rect_list[rect+1])
        for rect in range(0,len(R_TR.rect_list),3):
                pg.draw.lines(screen,R_TR.rect_list[rect+2],True, (R_TR.rect_list[rect][0],R_TR.rect_list[rect][1],R_TR.rect_list[rect][2]),R_TR.rect_list[rect+1])
        for rect in range(0,len(EQ_TR.rect_list),3):
                pg.draw.lines(screen,EQ_TR.rect_list[rect+2],True, (EQ_TR.rect_list[rect][0],EQ_TR.rect_list[rect][1],EQ_TR.rect_list[rect][2]),EQ_TR.rect_list[rect+1])
        for rect in range(0,len(ROMB.rect_list),3):
                pg.draw.lines(screen,ROMB.rect_list[rect+2],True, (ROMB.rect_list[rect][0],ROMB.rect_list[rect][2],ROMB.rect_list[rect][3],ROMB.rect_list[rect][1]),ROMB.rect_list[rect+1])
                
        pg.display.update()

    clockpy.tick(60)
    pg.display.flip()