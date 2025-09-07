import random

import pygame

from code.Consts import BLACK, WIN_HEIGHT, WIN_WIDTH, FPS, RED, BLUE, WHITE, GRAY, PLATFORMS, BACKGROUNDS
from code.AudioManager import AudioManager
from code.Player import Player
from code.Attack import Attack
from code.Enemy import Enemy
from code.ScoreManager import ScoreManager


class Stage:
    def __init__(self, window,audio_manager:AudioManager):
        self.window = window
        self.clock = pygame.time.Clock()
        self.player = Player(audio_manager=audio_manager)
        self.score = 0
        self.count = 0
        self.next_level_time = 10

        self.score_manager = ScoreManager()

        self.audio_manager = audio_manager

        self.enemies = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()
        for _ in range(3):
            enemy = Enemy(
                random.randint(300, WIN_WIDTH - 50),
                random.randint(100, WIN_HEIGHT - 100)
            )
            self.enemies.add(enemy)
        try:
            self.background = pygame.image.load(BACKGROUNDS['stage']).convert_alpha()
            self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))
        except:
            self.background = None

    def run(self):
        while True:
            dt = self.clock.tick(FPS)
            self.count += (dt/1000)
            if(self.count > self.next_level_time):
                self.count = 0
                new_enemy = self.get_safe_enemy_position()
                self.enemies.add(new_enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    if self.player.attack():
                        attack = Attack(self.player.rect.centerx,
                                        self.player.rect.centery,
                                        self.player.facing_right,
                                        self.player)
                        self.attacks.add(attack)

            for attack in self.attacks:
                hits = pygame.sprite.spritecollide(attack, self.enemies, False)
                for enemy in hits:
                    enemy.health -= 100
                    if enemy.health <= 0:
                        self.audio_manager.play_sound('enemy_dying_sound')
                        enemy.kill()
                        self.score += 1
                        # Respawn do inimigo
                        new_enemy = self.get_safe_enemy_position()
                        self.enemies.add(new_enemy)

            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if hits:
                self.player.health -= 5
                if self.player.health <= 0:
                    self.score_manager.save_score(self.score)
                    return 1

            self.player.update()
            self.attacks.update()
            self.enemies.update()

            self.render()


    def render(self):
        if self.background:
            self.window.blit(self.background, (0, 0))
        else:
            self.window.fill(BLACK)
        pygame.draw.rect(self.window, GRAY, (0, WIN_HEIGHT - 50, WIN_WIDTH, 50))
        self.draw_platforms()

        self.window.blit(self.player.image, self.player.rect)
        for attack in self.attacks:
            self.window.blit(attack.image, attack.rect)
        self.enemies.draw(self.window)
        self.draw_health_bar(10, 10, self.player.health, 100)
        self.draw_stage_score()
        pygame.display.flip()

    def draw_platforms(self):
        for platform in PLATFORMS:
            pygame.draw.rect(
                self.window, GRAY,
                (WIN_WIDTH * platform["x"],
                 WIN_HEIGHT * platform["y"],
                 WIN_WIDTH * platform["width"],
                 platform["height"])
            )
    def draw_health_bar(self, x, y, health, max_health):
        ratio = health / max_health
        pygame.draw.rect(self.window, RED, (x, y, 100, 20))
        pygame.draw.rect(self.window, BLUE, (x, y, 100 * ratio, 20))

    def draw_stage_score(self):
        font = pygame.font.SysFont('arial', 35)
        text = font.render(f'Score: {self.score}', True, WHITE)
        self.window.blit(text, (WIN_WIDTH/2 - text.get_width()/2, 20))

    def get_safe_enemy_position(self):
        safe_zone = 100
        player_radius = 150

        while True:
            x = random.randint(safe_zone, WIN_WIDTH - safe_zone)
            y = random.randint(safe_zone, WIN_HEIGHT - safe_zone - 50)

            enemy_rect = pygame.Rect(x - 25, y - 25, 50, 50)
            player_rect = pygame.Rect(
                self.player.rect.x - player_radius,
                self.player.rect.y - player_radius,
                self.player.rect.width + player_radius * 2,
                self.player.rect.height + player_radius * 2
            )

            if not enemy_rect.colliderect(player_rect):
                return Enemy(x, y)