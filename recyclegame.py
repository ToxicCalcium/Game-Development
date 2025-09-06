import pgzrun
import random
HEIGHT = 800
WIDTH = 800
centerx = WIDTH/2
centery = HEIGHT/2
gameover = False
complete = False
speed = 10
score = 0
animations = []
fallitems = []
nritems = ["plasticbag", "applecore", "battery", "computerchip"]

def draw():
    global nritems, gameover, complete
    screen.clear()
    bg = pygame.image.load("images/skybg.png")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))
    screen.blit(bg, (0, 0))
    if gameover == True:
        print("game over")
    elif complete == True:
        print("you win")
    else:
        for i in nritems:
            i.draw()
