import pygame
from code.Consts import BLACK, WHITE, WIN_WIDTH, WIN_HEIGHT, YELLOW, BACKGROUNDS
from code.ScoreManager import ScoreManager


class Score:
    def __init__(self, window):
        self.high_scores = [
            {"name": "Player1", "score": 1500},
            {"name": "Player2", "score": 1200},
            {"name": "Player3", "score": 800}
        ]
        self.window = window

        try:
            self.background = pygame.image.load(BACKGROUNDS['score']).convert_alpha()
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
            self.draw_scores(self.window)
            pygame.display.flip()

    def draw_scores(self, window):
        # Título
        title_font = pygame.font.SysFont('arial', 50)
        title = title_font.render('HIGH SCORES', True, WHITE)
        window.blit(title, (WIN_WIDTH // 2 - title.get_width() // 2, 50))

        # Scores
        font = pygame.font.SysFont('arial', 30)
        score_manager = ScoreManager()
        score_list = score_manager.get_top_scores(3)
        for i in range(len(score_list)):
            score_text = f"{i + 1}º. {score_list[i]['score']} points."
            text_surface = font.render(score_text, True, WHITE)
            window.blit(text_surface,
                        (WIN_WIDTH // 2 - text_surface.get_width() // 2,
                         180 + i * 40))

        footer_font = pygame.font.SysFont('arial', 25)
        footer = footer_font.render('Press ESC or ENTER to return', True, WHITE)
        window.blit(footer, (WIN_WIDTH // 2 - footer.get_width() // 2, WIN_HEIGHT - 50))