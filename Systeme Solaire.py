import core
import pygame
import random
from pygame.math import Vector2
def setup():
    print("setup START---------")
    core.fps = 144
    core.WINDOW_SIZE = [1200, 800]

    core.memory("centredecercle", pygame.Vector2(400, 400))
    core.memory("rayonducercle", 10)
    core.memory("couleurducercle", (0, 0,255))
    core.memory("direction", pygame.Vector2(0,0))
    core.memory("xprime", 0)
    core.memory("L", 0)
    core.memory("lo", 0)
    core.memory("Ux", 0)

    print("setup END-----------")
