import pygame
import math

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        bird_top = pygame.transform.scale(pygame.image.load("sprites/yellowbird-upflap.png").convert_alpha(), (50,35))
        bird_mid = pygame.transform.scale(pygame.image.load("sprites/yellowbird-midflap.png").convert_alpha(), (50,35))
        bird_bottom = pygame.transform.scale(pygame.image.load("sprites/yellowbird-downflap.png").convert_alpha(), (50,35))
        self.bird_frames = [bird_top, bird_mid, bird_bottom]
        self.frame_delay = 10
        self.frame_counter = 0
        self.frame_index = 0
        self.bird = self.bird_frames[self.frame_index]
        self.image = self.bird
        self.rect = self.image.get_rect(center = (100,350))

    def flap(self):
        if self.frame_counter >= self.frame_delay:
            if self.frame_index == 2:
                self.frame_index = 0
                self.frame_counter = 0
            else:
                self.frame_index += 1
                self.frame_counter = 0
        else:
            self.frame_counter += 1
        self.image = self.bird_frames[self.frame_index]

    def update(self):
        self.flap()