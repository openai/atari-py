set -ex

pip3 install pytest
pip3 install .
pytest .

PYPLATFORM=`python3 -c "import distutils.util; print(distutils.util.get_platform())"`
pip3 wheel . --wheel-dir=/tmp/wheelhouse --build-option --plat-name=$PYPLATFORM
ls -lht /tmp/wheelhouse

if [[ ! -z "$TRAVIS_TAG" ]]
do
    pip3 install twine
    twine upload /tmp/wheelhouse/atari_py-*
done

