import pgzrun
from random import randint
TITLE = "Shoot The Alien"
HEIGHT = 400
WIDTH = 400
hitmsg = ""

alien = Actor('alien')
alien.pos=50,50
def draw():
    screen.fill(color=(0,255,0))
    alien.draw()
    screen.draw.text(hitmsg, center=(350,10), fontsize=30, color="white")

def position():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global hitmsg
    if alien.collidepoint(pos):
        hitmsg = "You hit the alien"
        position()
    else:
        hitmsg = "You missed the alien"

position()

pgzrun.go()