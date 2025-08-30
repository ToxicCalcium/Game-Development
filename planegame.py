import pgzrun
import random
import time
import pygame
HEIGHT = 600
WIDTH = 800
Plane = []
Connectors = []
NumOfPlanes = 7
NextPlane = 0
StartTime = 0
TotalTime = 0
Countdown = 15
GameOver = False

def CreatePlanes():
    global StartTime
    for i in range(0, NumOfPlanes):
        Plnimg = Actor('plane')
        Plnimg.pos = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
        Plane.append(Plnimg)
    StartTime = time.time()

def draw():
    bg = pygame.image.load("images/skybg.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))
    screen.blit(bg, (0,0))
    if GameOver == True:
        screen.draw.text("Time Over", (WIDTH//2, HEIGHT//2))
    Number = 1
    for Plnimg in Plane:
        screen.draw.text(str(Number), (Plnimg.pos[0], Plnimg.pos[1]+20), color=(255, 0, 0))
        Plnimg.draw()
        Number = Number + 1
    

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    for i in Connectors:
        screen.draw.line(i[0], i[1], (r, g, b))
    RemainingTime = max(0, Countdown-(time.time()-StartTime))
    RemainingTime = round(RemainingTime, 1)
    screen.draw.text("Time Remaining: "+str(RemainingTime), (20, 20))
    if NumOfPlanes <= NextPlane:
        screen.draw.text("YOU WIN!", (WIDTH//2, HEIGHT//2), color=(255, 0, 0))

def update():
    global GameOver
    if not GameOver:
        if (time.time()-StartTime) > Countdown and NextPlane < NumOfPlanes:
            GameOver = True

def on_mouse_down(pos):
    global NextPlane
    global Connectors
    if GameOver:
        return
    if NextPlane < NumOfPlanes:
        if Plane[NextPlane].collidepoint(pos):
            if NextPlane: 
                Connectors.append((Plane[NextPlane-1].pos, Plane[NextPlane].pos))
            NextPlane = NextPlane + 1
        else:
            Connectors = []
            NextPlane = 0


CreatePlanes()
pgzrun.go()
