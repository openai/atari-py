set -ex
export REPO_DIR=.
export BUILD_COMMIT=$TRAVIS_COMMIT
export PLAT=x86_64
export MB_PYTHON_VERSION=$PY_VER
export MB_ML_VER=2014
if [[ $TRAVIS_CPU_ARCH == "arm64" ]]
then
  export PLAT=aarch64
  export DOCKER_TEST_IMAGE=multibuild/xenial_arm64v8
fi

git clone https://github.com/matthew-brett/multibuild && cd multibuild && git checkout 45d97819e7d39dd2264b2c3cd353c26c4e1ebb74 && cd ..
source multibuild/common_utils.sh
source multibuild/travis_steps.sh
before_install
build_wheel $REPO_DIR $PLAT
install_run $PLAT

