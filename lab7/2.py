# Create music player with keyboard controller. You have to be able to press keyboard:
# play, stop, next and previous as some keys. Player has to react to the given command appropriately.
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
quit=True
l=["music1.mp3","music2.mp3","music3.mp3"]
pygame.mixer.music.load(l[0])
cnt=0
while quit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit=False
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_s :
                pygame.mixer.music.stop()
            if event.key ==pygame.K_p :
                pygame.mixer.music.play()
            if event.key ==pygame.K_n :
                pygame.mixer.music.stop()
                if cnt!=len(l)-1:
                    pygame.mixer.music.load(l[cnt+1])
                    pygame.mixer.music.play()
                    cnt+=1
                else: 
                    cnt=0
                    pygame.mixer.music.load(l[cnt])
                    pygame.mixer.music.play()
            if event.key ==pygame.K_b :
                pygame.mixer.music.stop()
                if cnt==0:
                    pygame.mixer.music.load(l[len(l)-1])
                    pygame.mixer.music.play()
                    cnt=len(l)-1
                else: 
                    pygame.mixer.music.load(l[cnt-1])
                    pygame.mixer.music.play()
                    cnt-=1
    pygame.display.flip()
      
