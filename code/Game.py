import pygame
import sys
from code.Consts import WIN_WIDTH, WIN_HEIGHT, GAME_NAME
from code.HowToPlay import HowToPlay
from code.AudioManager import AudioManager
from code.Score import Score
from code.Stage import Stage
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.running = True
        self.audio_manager = AudioManager()

    def run(self):
        self.audio_manager.play_music('menu_music')
        while self.running:
            menu = Menu(self.window)
            menu_option = menu.run()
            if menu_option == 0:
                self.audio_manager.stop_music()
                self.audio_manager.play_music('stage_music')
                stage = Stage(self.window, self.audio_manager)
                stage_return = stage.run()
                if stage_return == 0:
                    self.running = False
                    continue
                if stage_return == 1:
                    self.audio_manager.stop_music()
                    self.audio_manager.play_music('menu_music')
                    continue
            if menu_option == 1:
                how_to_play = HowToPlay(window=self.window)
                how_to_play.run()
            if menu_option == 2:
                score = Score(window=self.window)
                score_return = score.run()
                if score_return == 0:
                    self.running = False
                    continue
                if score_return == 1:
                    continue
            if menu_option == 3:
                self.running = False
        pygame.quit()
        sys.exit()
