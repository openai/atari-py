#!/bin/bash
set -ex

if [ $(uname) == 'Linux' ] || [ $(uname) == 'Darwin' ]; then
    ./multibuild.sh
else
    ./win_build.sh
fi
