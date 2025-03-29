import pgzrun
HEIGHT = 400
WIDTH = 400
def draw():
    rect = Rect((200,250),(400,300))
    rect.center = 200,200
    screen.draw.rect(rect, "white")

pgzrun.go()