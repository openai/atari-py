#!/bin/bash
set -ex

# TRAVIS_TAG=0.1.14

if [[ -z "$TRAVIS_TAG" ]]; then
    echo "Not a tagged commit, quitting"
    exit 0
fi

pip install virtualenv --user
python -m virtualenv --python=python3 .venv
source .venv/bin/activate

pip install awscli twine
mkdir -p wheelhouse
env
# ugh something in awscli does not work on travis we'll download objects via curl
# aws s3 cp --recursive s3://games-wheels/atari-py/${TRAVIS_TAG} wheelhouse/
SUFFIXES="-manylinux1_x86_64.whl -win_amd64.whl -macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl"
# SUFFIXES="-manylinux1_x86_64.whl"
PY_VERS="-cp36-cp36m -cp37-cp37m"
URLPREFIX="https://s3-us-west-2.amazonaws.com/games-wheels/atari-py/${TRAVIS_TAG}/atari_py-${TRAVIS_TAG}"

cd wheelhouse
for s in $SUFFIXES; do
  for p in $PY_VERS; do
    curl -O ${URLPREFIX}${p}${s}
  done;
done

twine upload --verbose atari_py*
