set -ex

pip3 install pytest
pip3 install .
pytest .

PYPLATFORM=`python3 -c "import distutils.util; print(distutils.util.get_platform())"`
pip3 wheel . --wheel-dir=/tmp/wheelhouse --build-option --plat-name=$PYPLATFORM
ls -lht /tmp/wheelhouse

export TRAVIS_TAG="0.1.2"
if [[ ! -z "$TRAVIS_TAG" ]]; then
    pip3 install --user twine
    python3 -m twine upload /tmp/wheelhouse/atari_py-*
fi

