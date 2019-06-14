set -ex
choco install --yes python3 --version $PY_VER
export PYROOT=/c/Python${PY_VER//./}
export PATH=$PYROOT:$PYROOT/Scripts:$PATH
pip install cmake pytest
./installzlib.bat
mkdir -p atari_py/ale_interface/build

cd atari_py/ale_interface/build
cmake -DCMAKE_GENERATOR_PLATFORM=x64 ..
cmake --build .
cp Debug/ale_c.dll ../
cd ../../../

pip install wheel && pip wheel . -w wheelhouse --no-deps -vvv
ls wheelhouse/atari_py* 
rm -rf atari_py*
pip install $(ls wheelhouse/atari_py*)
pytest --pyargs atari_py.tests

