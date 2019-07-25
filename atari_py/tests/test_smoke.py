import atari_py
import numpy as np

def test_smoke():
    game_path = atari_py.get_game_path('tetris')
    ale = atari_py.ALEInterface()
    ale.loadROM(game_path)
    action_set = ale.getMinimalActionSet()

    # Test stepping
    ale.act(action_set[0])

    # Test screen capture
    (screen_width,screen_height) = ale.getScreenDims()
    arr = np.zeros((screen_height, screen_width, 4), dtype=np.uint8)
    ale.getScreenRGB(arr)

if __name__ == '__main__':
    print('smoke test')
    test_smoke()
    print('done!')
