#!/bin/bash
set -ex

if [ $(uname) == 'Linux' ]; then
    ./multibuild.sh
    exit 0
fi

if [ $(uname) == 'Darwin' ]; then
    ./multibuild.sh
    exit 0
fi
./win_build.sh
