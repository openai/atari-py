set -ex
# already present in Travis
# brew install cmake

pip3 install pytest
pytest .

pip wheel . --wheel-dir=/tmp/wheelhouse
ls -lht /tmp/wheelhouse

