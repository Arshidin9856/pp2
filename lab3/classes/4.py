class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"{self.x}-->x\n{self.y}-->y")
    def move(self,nx,ny):
        self.x=nx
        self.y=ny
    def dist(self,x2,y2):
        print(f'{((self.x-x2)**2-(self.y-y2)**2)**0.5}-->dist')
l=list(map(int,input().split()))    
p=point(l[0],l[1])
d=list(map(int,input().split()))
p.dist(d[0],d[1])
#p.show()
        