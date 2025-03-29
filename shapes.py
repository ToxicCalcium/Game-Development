import pgzrun
HEIGHT = 400
WIDTH = 400

'''def draw():
    rect = Rect((200,250),(400,300))
    rect.center = 200,200
    screen.draw.filled_rect(rect,(0, 255, 0))'''

'''def draw():
    screen.draw.line((0,200),(400,200), (255,0,0))'''

def draw():
    screen.draw.circle((200,200), 100, "green")

pgzrun.go()