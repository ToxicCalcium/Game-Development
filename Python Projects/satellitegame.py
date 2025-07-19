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
EndTime = 0
TotalTime = 0

def CreateSatellites():
    global StartTime # global allows variable to be used in other functions
    for i in range(0, NumOfSatellites):
        SatImg = Actor('satellite.png')
        SatImg.pos = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
        Satellite.append(SatImg)
    StartTime = time.time()

def draw():
    global TotalTime
    screen.blit("spacebg", (0,0))
    Number = 1
    for SatImg in Satellite:
        screen.draw.text(str(Number), (SatImg.pos[0], SatImg.pos[1]+20))
        SatImg.draw()
        Number = Number + 1
    
    for Line in Connectors:
        screen.draw.line(Connectors[0], Connectors[1], (255, 255, 255))
    if NextSatellite < NumOfSatellites:
        Totaltime = time.time() - StartTime
        screen.draw.text("You Win!", (0, 0))
