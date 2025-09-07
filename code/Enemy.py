import pygame
import random
from code.Consts import RED, WIN_WIDTH, WIN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2
        self.health = 30
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

        if self.rect.left <= 0 or self.rect.right >= WIN_WIDTH:
            self.direction_x *= -1
            if random.random() < 0.3:
                self.direction_y = random.choice([-1, 1])

        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.direction_y *= -1
            if random.random() < 0.3:
                self.direction_x = random.choice([-1, 1])

        if random.random() < 0.01:
            self.direction_x = random.choice([-1, 1])
            self.direction_y = random.choice([-1, 1])