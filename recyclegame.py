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
        screen.draw.text("Game Over", (WIDTH//2, HEIGHT//2))
    elif complete == True:
        screen.draw.text("You Win", (WIDTH//2, HEIGHT//2))
    else:
        for i in nritems:
            i.draw()

def update():
    global nritems
    if fallitems.len() == 0 and not gameover:
        fallitems = makeitems()

def makeitems():
    itemstocreate = ["paper"]
    for i in range(3):
        itemstocreate.append(random.choice(nritems))
    newfallitems = createitems(itemstocreate)
    itemlayout(newfallitems)
    itemanims(newfallitems)
    return newfallitems

def createitems(itemstocreate):
    newfallitems = []
    for i in itemstocreate:
        fallitems = Actor(i)
        newfallitems.append(fallitems)
    return fallitems