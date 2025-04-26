import pgzrun
HEIGHT = 400
WIDTH = 400
def draw():
    w = 400
    h = 100
    r = 0
    g = 0
    b = 255
    for i in range(20):
        rect = Rect((200,250),(w,h))
        rect.center = 200,200
        screen.draw.rect(rect, (r, g, b))
        w -= 15
        h += 15
        g += 10
        b -=10
pgzrun.go()