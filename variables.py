# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

import numpy as np

# Resolution
HEIGHT, WIDTH = 900, 1600
WIDTH_HF = WIDTH // 2
HEIGH_HF = HEIGHT // 2
FPS = 30
PIXEL = 10
MAPS = 8
# Var
PLAYER_X = 1.5
PLAYER_Y = 5
PLAYER_ANG = 0
PLAYER_SP = 0.004
PLAYER_ROT = 0.002
PLAYER_SZ = 60
SENSITIVITY = 0.0003
MOVEMENT = 40
LEFT_BORDER = 100
RIGHT_BORDER = WIDTH - LEFT_BORDER
# Data
FOV = np.pi / 3
FOV_HF = FOV/2
CASTED_RAYS = WIDTH // 2
HALF_RAYS = CASTED_RAYS // 2
DELTA_ANG = FOV / CASTED_RAYS
STEP_ANG = FOV / CASTED_RAYS
SCALE = WIDTH // CASTED_RAYS
MAX_DEPTH = 20
DISTANCE = WIDTH_HF / np.tan(FOV_HF)
# Texture
TEXTURE_SZ = 256
TEXTURE_HF = TEXTURE_SZ // 2
FLOOR_CLR = (105, 105, 105)
