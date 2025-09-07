#Audios
AUDIO_PATHS = {
    'menu_music': 'assets/audio/menu_music.mp3',
    'stage_music': 'assets/audio/stage_music.mp3',
    'attack_sound': 'assets/audio/attack.mp3',
    'jump_sound': 'assets/audio/jump.wav',
    'enemy_dying_sound': 'assets/audio/enemy_dying.ogg',
}
# Back
BACKGROUNDS = {
    'menu': 'assets/background/back.png',
    'stage': 'assets/background/forest_back_550_x_400.png',
    'score': 'assets/background/bg5.jpg',
    'how_to_play': 'assets/background/cavernous.png'
}
# Character frames
CHARACTER_IMAGE_RIGHT = 'assets/character/winged_warrior_right.png'
CHARACTER_IMAGE_LEFT = 'assets/character/winged_warrior_left.png'

# Config
WIN_WIDTH=800
WIN_HEIGHT=600
GAME_NAME="Knight Adventure"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

#Menu
MENU_OPTIONS = ('New Game',
                'How to play',
                'Score',
                'Exit')
# Platforms
PLATFORMS = (
    {"x": 0.15, "y": 0.65, "width": 0.2, "height": 25},  # left
    {"x": 0.68, "y": 0.65, "width": 0.2, "height": 25},  # right
    {"x": 0.415, "y": 0.4, "width": 0.2, "height": 25}   # middle
)

# Clock
FPS = 60