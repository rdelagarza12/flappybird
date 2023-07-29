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
        self.hover_delay = 1
        self.hover_counter = 0
        self.frame_index = 0
        self.bird = self.bird_frames[self.frame_index]
        self.image = self.bird
        self.rect = self.image.get_rect(center = (100,350))
        self.up = True
        self.start = False
        self.falling = False
        self.fall_speed = 0
        self.max_height = 5
        self.fly_speed = 0
        self.rotation_angle = 0

    def flap_animation(self):
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

    def hover(self):
        if self.hover_counter >= self.hover_delay:
            if self.up and self.rect.y <= 358:
                self.rect.y += 1
                if self.rect.y == 358:
                    self.up = False
            elif self.up == False and self.rect.y >= 347:
                self.rect.y -= 1
                if self.rect.y == 347:
                    self.up = True
            self.hover_counter = 0
        else:
            self.hover_counter += 1

    def gravity(self):
        self.rect.y += self.fall_speed
        if self.fall_speed <= 4:
            self.fall_speed += .5



    def flying(self):
        if self.fly_speed != 15:
            self.rect.y -= self.fly_speed
            self.fly_speed += 1
            if self.fly_speed == 15:
                self.falling = True

        else:
            self.falling = True

        



    def update(self):
        if self.start == True:
            if self.falling == True:
                self.gravity()
                self.flap_animation()
                if self.rotation_angle > -20:
                    self.rotation_angle -= 20
                
            else:
                self.flying()
                self.flap_animation()
                if self.rotation_angle < 20:
                    self.rotation_angle += 20
            self.image = pygame.transform.rotate(self.bird_frames[self.frame_index], self.rotation_angle)
        else: 
            self.flap_animation()
            self.hover()