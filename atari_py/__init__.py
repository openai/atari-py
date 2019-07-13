from .ale_python_interface import *
from .games import get_game_path, list_games

# default to only logging errors
ALEInterface.setLoggerMode(ALEInterface.Logger.Error)
