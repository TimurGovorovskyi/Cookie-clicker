from pygame import *
from settings import window_size, background_color
from functionality import Cookie
import value

window = display.set_mode(window_size)
display.set_caption("Cookie Clicker")
window.fill(background_color)

cookie = Cookie(400, 300, 100, (255, 223, 0))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            if cookie.is_pressed(e.pos):
                pass

    window.fill(background_color)
    cookie.draw(window)
    display.update()