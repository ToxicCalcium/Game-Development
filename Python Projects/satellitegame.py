import pgzrun
import random
import time
HEIGHT = 600
WIDTH = 800
Satellite = []
Connectors = []
NumOfSatellites = 7
StartTime = 0
EndTime = 0
TotalTime = 0

def CreateSatellites():
    global StartTime # global allows variable to be used in other functions
    for i in range(0, NumOfSatellites):
        Satellites = Actor('satellite.png')
        
