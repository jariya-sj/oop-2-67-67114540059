import pygame
from pygame.locals import*

pygame.init()
size=(600,400)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Gameee!!!') #ชื่อที่มันจะขึ้น
clock=pygame.time.Clock()
sheet=pygame.image.load('Tiny_Swords\spritesheet.png') #ใส่ชื่อไฟล์ที่มันอยู่

running = True
frame=0
x,y=20,40
speed=10
# loop
while running:
 # 1. check events 
    for e in pygame.event.get():
        if e.type == QUIT: #QUIT คือไม่อยากจะรันแล้ว
            running = False
        # if event.type==KEYDOWN:
        #     if event.key in [K_a,K_LEFT]: x -=speed
        #     elif event.key in [K_d,K_RIGHT]: x +=speed
        #     elif event.key in [K_s,K_DOWN]: x +=speed
        #     elif event.key in [K_w,K_UP]: x -=speed
            
    keys=pygame.key.get_pressed()
    if keys[K_a]or keys[K_LEFT]: x -=speed
    elif keys[K_d]or keys[K_RIGHT]: x +=speed
    elif keys[K_s]or keys[K_DOWN]: y +=speed
    elif keys[K_w]or keys[K_UP]: y-=speed
            
 # 2. update game objects state/data
 
 # 3. draw on screen
    screen.fill((0, 0, 0)) #ตัวเลขคือตัวระบุขนาดของสี
    screen.blit(sheet,(x, y))
    clock.tick(30)
    
 # 4. show screen on display
    pygame.display.flip() 
    
pygame.quit() 