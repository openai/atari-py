#!/bin/bash
set -ex

if [[ -z "$TRAVIS_TAG" ]]; then
    echo "Not a tagged commit, quitting"
    exit 0
fi

pip install awscli twine
mkdir -p wheelhouse
aws s3 cp s3://games-wheels/atari-py/atari_py-${TRAVIS_TAG}-*
twine upload --verbose wheelhouse/atari_py*
