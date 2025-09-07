import pygame

from code.Consts import WHITE


class Attack(pygame.sprite.Sprite):
    def __init__(self, x, y, facing_right, player):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.facing_right = facing_right
        self.player = player


        self.offset_x = 30
        self.update_position(x, y)

        self.hitbox = pygame.Rect(
            self.rect.x + 5,
            self.rect.y + 5,
            self.rect.width - 10,
            self.rect.height - 10
        )

        if facing_right:
            self.rect.midleft = (x + 30, y)
        else:
            self.rect.midright = (x - 30, y)

        self.lifetime = 10
        self.hit_enemies = set()

    def update(self):
        self.update_position(self.player.rect.centerx, self.player.rect.centery)

        self.hitbox.x = self.rect.x + 5
        self.hitbox.y = self.rect.y + 5

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()


    def update_position(self, player_x, player_y):
        """Atualiza a posição baseada no jogador"""
        if self.facing_right:
            self.rect.midleft = (player_x + self.offset_x, player_y)
        else:
            self.rect.midright = (player_x - self.offset_x, player_y)