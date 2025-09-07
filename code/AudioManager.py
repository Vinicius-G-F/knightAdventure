import pygame
from code.Consts import AUDIO_PATHS

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None
        self.volume = 0.5
        self.sounds = {}

        self.load_sounds()

    def play_music(self, track_name, loops=-1):
        if track_name in AUDIO_PATHS:
            try:
                pygame.mixer.music.load(AUDIO_PATHS[track_name])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play(loops)
                self.current_track = track_name
            except Exception as e:
                print(f"Erro ao carregar música: {e}")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)

    def load_sounds(self):
        for sound_name in ['attack_sound', 'jump_sound', 'enemy_dying_sound']:
            try:
                self.sounds[sound_name] = pygame.mixer.Sound(AUDIO_PATHS[sound_name])
                self.sounds[sound_name].set_volume(self.volume)
            except:
                print(f"Erro ao carregar efeito: {sound_name}")

    def play_sound(self, sound_name, loops=0):
        if sound_name in self.sounds:
            self.sounds[sound_name].play(loops=loops)