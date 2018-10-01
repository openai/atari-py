set -ex
pip3 install --user twine
python3 -m twine upload /tmp/wheelhouse/atari_py-*

