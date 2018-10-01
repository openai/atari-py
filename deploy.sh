set -ex
pip install --user twine
python -m twine upload /tmp/wheelhouse/atari_py-*

