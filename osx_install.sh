set -ex
# already present in Travis
# brew install cmake

pip3 install pytest
pip3 install .
pytest .

pip3 wheel . --wheel-dir=/tmp/wheelhouse
ls -lht /tmp/wheelhouse

