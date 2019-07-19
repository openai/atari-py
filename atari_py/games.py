import os


SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    import atari_py_roms
    _games_dir = os.path.join(atari_py_roms.__path__[0], "atari_roms")
except ImportError:
    _games_dir = os.path.join(SCRIPT_DIR, "atari_roms")


def get_games_dir():
    return _games_dir


def get_game_path(game_name):
    path = os.path.join(_games_dir, game_name) + ".bin"
    if not os.path.exists(path):
        raise Exception('ROM is missing for %s, see https://github.com/openai/atari-py#roms for instructions' % (game_name,))
    return path

def list_games():
    files = os.listdir(_games_dir)
    return [os.path.basename(f).split(".")[0] for f in files]