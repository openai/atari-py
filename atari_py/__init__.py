from .ale_python_interface import *
import os

def _game_dir():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "atari_roms")

def get_game_path(game_name):
    return os.path.join(_game_dir(), game_name) + ".bin"

def list_games():
    files = os.listdir(_game_dir())
    return [os.path.basename(f).split(".")[0] for f in files]

# default to only logging errors
ALEInterface.setLoggerMode(ALEInterface.Logger.Error)
