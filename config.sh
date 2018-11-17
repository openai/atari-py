#!/bin/bash
function pre_build {
    set -ex
    get_cmake
    build_zlib
    pip install .
    pip install pytest
    pytest .
}

function run_tests {
    python -c "import gym; gym.make('Pong-v4')"
}

