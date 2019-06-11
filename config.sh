#!/bin/bash
function pre_build {
    set -ex
    build_zlib
    pip install cmake
}

function run_tests {
    pip install gym
    python -c "import gym; gym.make('Pong-v4')"
    pip install pytest
    pytest --pyargs atari_py.tests
}

