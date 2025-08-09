import pgzrun
import random
import time
HEIGHT = 600
WIDTH = 800
Satellite = []
Connectors = []
NumOfSatellites = 7
NextSatellite = 0
StartTime = 0
TotalTime = 0
Countdown = 15
GameOver = False

def CreateSatellites():
    global StartTime # global allows variable to be used in other functions
    for i in range(0, NumOfSatellites):
        SatImg = Actor('satellite')
        SatImg.pos = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
        Satellite.append(SatImg)
    StartTime = time.time()

def draw():
    #global TotalTime
    screen.blit("spacebg", (0,0))
    if GameOver == True:
        screen.draw.text("Time Over", (WIDTH//2, HEIGHT//2))
    Number = 1
    for SatImg in Satellite:
        screen.draw.text(str(Number), (SatImg.pos[0], SatImg.pos[1]+20))
        SatImg.draw()
        Number = Number + 1
    
    for i in Connectors:
        screen.draw.line(i[0], i[1], (255, 255, 255))
    #Totaltime = time.time() - StartTime
    RemainingTime = max(0, Countdown-(time.time()-StartTime))
    RemainingTime = round(RemainingTime, 1)
    screen.draw.text("Time Remaining: "+str(RemainingTime), (20, 20))
    if NumOfSatellites <= NextSatellite:
        screen.draw.text("YOU WIN!", (WIDTH//2, HEIGHT//2))

def update():
    global GameOver
    #global TotalTime
    if not GameOver:
        if (time.time()-StartTime) > Countdown and NextSatellite < NumOfSatellites:
            GameOver = True

def on_mouse_down(pos):
    global NextSatellite
    global Connectors
    if GameOver:
        return
    if NextSatellite < NumOfSatellites: #Are there satellites left
        if Satellite[NextSatellite].collidepoint(pos): #checks if the satellite is the correct one
            if NextSatellite: # if not 1st satellite
                Connectors.append((Satellite[NextSatellite-1].pos, Satellite[NextSatellite].pos))
            NextSatellite = NextSatellite + 1
        else:
            Connectors = []
            NextSatellite = 0


CreateSatellites()
pgzrun.go()
