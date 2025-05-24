import pgzrun
from random import randint
HEIGHT = 400
WIDTH = 500
Bee = Actor("bee")
Flower = Actor("flower")
Score = 0
GameOver = False

Bee.pos = 200, 100
Flower.pos = 200, 300

def draw():
    screen.blit("grassbg", (0,0))
    Bee.draw()
    Flower.draw()
    screen.draw.text("Score:" + str(Score)) #the operator '+' is used to combine multiple strings together known as string concatenation. It is used here to combine the text "Score:" with the variable 'Score'.
    if GameOver == True:
        screen.fill("red")
        screen.draw.text("Time's Up! Score:" + str(Score))

def flowerpos():
    Flower.x = randint(50, (WIDTH-50))
    Flower.y = randint(50, (HEIGHT-50))

def update():
    global Score
    if keyboard.a:
        Bee.x = Bee.x - 5
    if keyboard.d:
        Bee.x = Bee.x + 5
    if keyboard.w:
        Bee.y = Bee.y + 5
    if keyboard.s:
        Bee.y = Bee.y - 5
    
    bfc = Bee.colliderect(Flower)
    if bfc:
        Score = Score + 1
        flowerpos()

def timer():
    global GameOver
    GameOver = True

clock.schedule(timer, 60.0)

pgzrun.go()