#!/bin/bash
set -ex

# TRAVIS_TAG=0.2.6

if [[ -z "$TRAVIS_TAG" ]]; then
    echo "Not a tagged commit, quitting"
    exit 0
fi

pip install virtualenv --user
python -m virtualenv --python=python3 .venv
source .venv/bin/activate

pip install awscli twine
# make and deploy source archive
python setup.py sdist
twine upload --verbose dist/atari*

# get the wheels generated at the previous stages and upload them as well 
mkdir -p wheelhouse
env
# ugh something in awscli does not work on travis we'll download objects via curl
# aws s3 cp --recursive s3://games-wheels/atari-py/${TRAVIS_TAG} wheelhouse/
SUFFIXES="-manylinux_2_17_aarch64.manylinux2014_aarch64.whl -manylinux_2_17_x86_64.manylinux2014_x86_64.whl -win_amd64.whl -macosx_10_12_x86_64.whl"
# SUFFIXES="-manylinux1_x86_64.whl"
PY_VERS="-cp36-cp36m -cp37-cp37m -cp38-cp38m -cp39-cp39m"
URLPREFIX="https://s3-${AWS_DEFAULT_REGION}.amazonaws.com/${S3_BUCKET}/${S3_PREFIX}atari-py/${TRAVIS_TAG}/atari_py-${TRAVIS_TAG}"

cd wheelhouse
for s in $SUFFIXES; do
  for p in $PY_VERS; do
    curl -O -f ${URLPREFIX}${p}${s} || echo "${URLPREFIX}${p}${s} not found"
  done;
done

twine upload --verbose atari*
