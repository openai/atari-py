#!/bin/bash
function pre_build {
    set -ex
    build_zlib
    pip install cmake
}

function run_tests {
    python -c "import atari_py; ale = atari_py.ALEInterface(); ale.loadROM(atari_py.get_game_path('tetris'))"
    pip install pytest
    pytest --pyargs atari_py.tests
}

