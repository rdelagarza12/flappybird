import pygame

class Pipe(pygame.sprite.Sprite):

    def __init__(self, x, y, r):
        pygame.sprite.Sprite.__init__(self)
        top_pipe = pygame.transform.rotate(pygame.image.load("sprites/pipe-green.png").convert_alpha(), r)
        self.image = top_pipe
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def move_left(self):
        self.rect.x -= 2

    def update(self):
        self.move_left()
        if self.rect.x == -300:
            self.kill()