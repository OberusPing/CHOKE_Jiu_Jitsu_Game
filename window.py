import pygame, sys
from sys import exit as _exit


class PG_Window_UI:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))

    def update(self):
        pygame.display.flip()

    def clear(self, r, g, b):
        self.window.fill((r, g, b))

    def close(self):
        pygame.quit()
        _exit()


# handles events
def handleEvents(events, pg_window):
    exitGame = False
    for event in events:
        if event.type == pygame.QUIT:
            pg_window.close()


# Takes rectangle's size, position and a point. Returns true if that
# point is inside the rectangle and false if it isn't.
def pointInRectanlge(px, py, rw, rh, rx, ry):
    if px > rx and px < rx + rw:
        if py > ry and py < ry + rh:
            return True
    return False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
