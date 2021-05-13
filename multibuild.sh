set -ex
export REPO_DIR=.
export BUILD_COMMIT=$TRAVIS_COMMIT
export PLAT=$TRAVIS_CPU_ARCH
export MB_PYTHON_VERSION=$PY_VER

git clone https://github.com/matthew-brett/multibuild && cd multibuild && cd ..
source multibuild/common_utils.sh
source multibuild/travis_steps.sh
before_install
build_wheel $REPO_DIR $PLAT
install_run $PLAT

