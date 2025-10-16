import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../Data"))

CONFIG_PATH = os.path.join(DATA_DIR, "config.json")
PLAYER_PATH = os.path.join(DATA_DIR, "player.json")