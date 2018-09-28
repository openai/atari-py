set -ex
# already present in Travis
# brew install cmake

PYPLATFORM=`python -c "import distutils.util; print(distutils.util.get_platform())"`
pip wheel . --wheel-dir=/tmp/wheelhouse --build-option --plat-name=$PYPLATFORM
