#!/bin/bash
set -ex

TRAVIS_TAG=0.1.14

if [[ -z "$TRAVIS_TAG" ]]; then
    echo "Not a tagged commit, quitting"
    exit 0
fi

pip install virtualenv --user
python -m virtualenv --python=python3 .venv
source .venv/bin/activate

pip install awscli twine
mkdir -p wheelhouse
aws s3 cp --recursive s3://games-wheels/atari-py/${TRAVIS_TAG} wheelhouse/
twine upload --verbose wheelhouse/atari_py*
