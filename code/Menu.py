import pygame.image
from pygame.font import Font
from pygame import Surface, Rect

from code.Consts import BLACK, WHITE, WIN_WIDTH, MENU_OPTIONS, BLUE, YELLOW, BACKGROUNDS, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.menu_selected = 0
        try:
            self.menu_back = pygame.image.load(BACKGROUNDS['menu']).convert_alpha()
            self.menu_back = pygame.transform.scale(self.menu_back, (WIN_WIDTH, WIN_HEIGHT))
        except:
            self.menu_back = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.menu_selected == (len(MENU_OPTIONS) - 1):
                            self.menu_selected = 0
                        else:
                            self.menu_selected = (self.menu_selected + 1)
                    if event.key == pygame.K_UP:
                        if self.menu_selected == 0:
                            self.menu_selected = (len(MENU_OPTIONS) - 1)
                        else:
                            self.menu_selected = (self.menu_selected - 1)
                    if event.key == pygame.K_RETURN:
                        return self.menu_selected
            if self.menu_back:
                self.window.blit(self.menu_back, (0, 0))
            else:
                self.window.fill(BLACK)

            self.menu_text(60, "Knight", BLUE, ((WIN_WIDTH / 2), 50) )
            self.menu_text(60, "Adventure", BLUE, ((WIN_WIDTH / 2), 100))
            for i in range(len(MENU_OPTIONS)):
                if self.menu_selected == i:
                    self.menu_text(28, MENU_OPTIONS[i], YELLOW, ((WIN_WIDTH / 2), 250 + (i * 40)))
                else:
                    self.menu_text(28, MENU_OPTIONS[i], WHITE, ((WIN_WIDTH / 2), 250 + (i*40)))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: (int, int, int), text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='arial', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
