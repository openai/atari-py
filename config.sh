#!/bin/bash
function pre_build {
    set -ex
    build_zlib
    pip install .
    pip install pytest
    pytest .
}

function run_tests {
    echo "Hello world with box2d-py"
}

