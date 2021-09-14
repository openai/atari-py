import sys

from .ale_python_interface import *
from .games import get_game_path, list_games

print(
    "[NOTICE] atari-py is deprecated in favor ale-py "
    "and will no longer receive further maintenance or critical updates. "
    "ale-py is fully backwards compatible with atari-py. "
    "If you're using Gym, you can simply upgrade via pip install -U gym[atari]"
    file=sys.stderr,
)


# default to only logging errors
ALEInterface.setLoggerMode(ALEInterface.Logger.Error)
