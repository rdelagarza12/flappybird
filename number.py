import pygame

class Number(pygame.sprite.Sprite):
    pipes_passed = 0
    def __init__(self, x, y, count):
        pygame.sprite.Sprite.__init__(self)
        number_0 = pygame.image.load("sprites/0.png").convert_alpha()
        number_1 = pygame.image.load("sprites/1.png").convert_alpha() 
        number_2 = pygame.image.load("sprites/2.png").convert_alpha()
        number_3 = pygame.image.load("sprites/3.png").convert_alpha()
        number_4 = pygame.image.load("sprites/4.png").convert_alpha()
        number_5 = pygame.image.load("sprites/5.png").convert_alpha()
        number_6 = pygame.image.load("sprites/6.png").convert_alpha()
        number_7 = pygame.image.load("sprites/7.png").convert_alpha()
        number_8 = pygame.image.load("sprites/8.png").convert_alpha()
        number_9 = pygame.image.load("sprites/9.png").convert_alpha()
        self.index = count
        self.number_list = [number_0, number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9]
        self.image = self.number_list[self.index]
        self.rect = self.image.get_rect(center = (x, y))
        self.change_for_pipe = False

    def change_number(self, new_number):
        self.index = new_number
        self.image = self.number_list[self.index]
