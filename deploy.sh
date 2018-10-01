set -ex
pip install --user twine
twine upload /tmp/wheelhouse/atari_py-*

