import pygame
from pygame import Surface, Rect
from code.Consts import BLACK, WHITE, WIN_WIDTH, WIN_HEIGHT, BACKGROUNDS


class HowToPlay:
    def __init__(self, window):
        self.window = window
        try:
            self.arrows_img = pygame.image.load('assets/setas.jpg').convert_alpha()
            self.arrows_img = pygame.transform.scale(self.arrows_img, (200, 200))
        except:
            self.arrows_img = None

        # background
        try:
            self.background = pygame.image.load(BACKGROUNDS['how_to_play']).convert_alpha()
            self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))
        except:
            self.background = None


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        return 1

            if self.background:
                self.window.blit(self.background, (0, 0))
            else:
                self.window.fill(BLACK)

            self.draw_controls()
            pygame.display.flip()

    def draw_controls(self):
        title_font = pygame.font.SysFont('arial', 50)
        title = title_font.render('HOW TO PLAY', True, WHITE)
        self.window.blit(title, (WIN_WIDTH//2 - title.get_width()//2, 50))

        if self.arrows_img:
            self.window.blit(self.arrows_img,
                           (WIN_WIDTH//2 - self.arrows_img.get_width()//2, 120))

        font = pygame.font.SysFont('arial', 30)
        controls = [
            "Movement: Arrow Keys",
            "Jump: Z Key",
            "Attack: X Key",
            "Pause: ESC Key",
            "",
            "Press ENTER or ESC to return"
        ]

        for i, text in enumerate(controls):
            text_surface = font.render(text, True, WHITE)
            self.window.blit(text_surface,
                           (WIN_WIDTH//2 - text_surface.get_width()//2,
                            350 + i * 40))