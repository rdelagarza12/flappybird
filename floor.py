import pygame

class Base(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        base = pygame.transform.scale(pygame.image.load("sprites/base.png").convert_alpha(), (452,100))
        self.x = x
        self.y = y
        self.image = base
        self.rect = self.image.get_rect(bottomleft = (self.x, self.y))

    def shift_floor(self):
        if self.x <= -450:
            self.x = 450
        else:
            self.x -= 2
            self.rect.x = self.x

    def update(self):
        self.shift_floor()