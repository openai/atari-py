set -ex

pip3 install pytest
pip3 install .
pytest .

PYPLATFORM=`python3 -c "import distutils.util; print(distutils.util.get_platform())"`
pip3 wheel . --wheel-dir=/tmp/wheelhouse --build-option --plat-name=$PYPLATFORM
ls -lht /tmp/wheelhouse

