import pygame

class Pipe(pygame.sprite.Sprite):

    def __init__(self, x, y, r, pipe):
        pygame.sprite.Sprite.__init__(self, )
        top_pipe = pygame.transform.scale_by(pygame.image.load("sprites/top-green-pipe.png").convert_alpha(), .1)
        bottom_pipe = pygame.transform.scale_by(pygame.image.load("sprites/pipe-green.png").convert_alpha(), 1.24)

        
        if pipe == 1:
            self.image = top_pipe
        if pipe == 2:
            self.image = bottom_pipe
        self.x = x
        self.y = y
        if pipe == 1:
            self.rect = self.image.get_rect(bottomleft = (self.x, self.y))
        if pipe == 2:
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.passed = False

    def move_left(self):
        self.rect.x -= 4
    
    def update(self):
        self.move_left()
        if self.rect.x == -1000:
            self.kill()