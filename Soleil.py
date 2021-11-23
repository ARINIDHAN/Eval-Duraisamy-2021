import random
import pygame



class Saturne :
    def __init__(self):
        self.rayon = 15
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = 0


    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)