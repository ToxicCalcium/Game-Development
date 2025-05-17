import pgzrun
from random import randint
HEIGHT = 400
WIDTH = 500
Bee = Actor("Bee")
Flower = Actor("Flower")
Score = 0
GameOver = False

Bee.pos = 200, 100
Flower.pos = 200, 300

def draw():
    screen.blit("GrassBG", (0,0))
    Bee.draw()
    Flower.draw()
    screen.draw.text("Score:" + str(Score)) #the operator '+' is used to combine multiple strings together known as string concatenation. It is used here to combine the text "Score:" with the variable 'Score'.
    if GameOver == True:
        screen.fill("red")
        screen.draw.text("Time's Up! Score:" + str(Score))
