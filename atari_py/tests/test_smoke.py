import atari_py

def test_smoke():
    pong_path = atari_py.get_game_path('pong')
    ale = atari_py.ALEInterface()
    ale.loadROM(pong_path)
    action_set = ale.getMinimalActionSet()
    ale.act(action_set[0])
