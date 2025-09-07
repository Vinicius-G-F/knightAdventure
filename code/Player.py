import pygame

from code import AudioManager
from code.Consts import BLUE, WIN_WIDTH, WIN_HEIGHT, PLATFORMS, CHARACTER_IMAGE_RIGHT, CHARACTER_IMAGE_LEFT


class Player(pygame.sprite.Sprite):
    def __init__(self, audio_manager: AudioManager):
        super().__init__()
        self.image_right = pygame.image.load(CHARACTER_IMAGE_RIGHT)
        self.image_right = pygame.transform.scale(self.image_right, (80, 80))
        self.image_left = pygame.image.load(CHARACTER_IMAGE_LEFT)
        self.image_left = pygame.transform.scale(self.image_left, (80, 80))

        self.facing_right = True
        self.image = self.image_right

        self.rect = self.image.get_rect()
        self.rect.width = 40
        self.rect.center = (WIN_WIDTH // 4, WIN_HEIGHT // 2)

        self.audio_manager = audio_manager

        self.speed = 5
        self.jump_power = 18
        self.velocity_y = 0
        self.on_ground = False
        self.health = 100
        self.attack_cooldown = 0

    def update(self):
        # Reset horizontal movement
        dx = 0
        dy = 0

        # Horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= self.speed
            self.look_left()
        if keys[pygame.K_RIGHT]:
            dx += self.speed
            self.look_right()

        # Jump (only when on ground)
        if keys[pygame.K_z] and self.on_ground:
            self.audio_manager.play_sound('jump_sound')
            self.velocity_y = -self.jump_power
            self.on_ground = False

        # Apply gravity
        self.velocity_y += 0.8
        if self.velocity_y > 10:
            self.velocity_y = 10
        dy += self.velocity_y

        # Update position (x first)
        self.rect.x += dx

        # Keep player on screen horizontally
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

        # Update vertical position
        self.rect.y += dy

        # Reset ground state before checking collisions
        self.on_ground = False

        # Platform collision check
        platforms = tuple(
            pygame.Rect(
                WIN_WIDTH * platform["x"],
                WIN_HEIGHT * platform["y"],
                WIN_WIDTH * platform["width"],
                platform["height"]
            )
            for platform in PLATFORMS
        )


        for platform in platforms:
            # Check if player is falling onto platform from above
            if (self.velocity_y > 0 and  # Player is moving downward
                    self.rect.colliderect(platform) and  # Overlapping with platform
                    self.rect.bottom < platform.centery):  # Player's feet above platform center

                self.rect.bottom = platform.top + 10  # Snap to platform surface
                self.on_ground = True
                self.velocity_y = 0
                break  # Only need to land on one platform

        # Main floor collision (keep this as backup)
        if not self.on_ground and self.rect.bottom > WIN_HEIGHT - 50 + 10:
            self.rect.bottom = WIN_HEIGHT - 50 + 10
            self.on_ground = True
            self.velocity_y = 0

        # Attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def attack(self):
        if self.attack_cooldown == 0:
            self.attack_cooldown = 20  # Tempo de cooldown
            self.audio_manager.play_sound('attack_sound')
            return True
        return False

    def look_right(self):
        self.image = self.image_right
        self.facing_right = True

    def look_left(self):
        self.image = self.image_left
        self.facing_right = False