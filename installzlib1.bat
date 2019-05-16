curl -O https://zlib.net/zlib1211.zip
unzip zlib1211.zip 
cp -r zlib-1.2.11 atari_py/ale_interface/src/zlib
cd atari_py/ale_interface/src/zlib
cmake .
cmake --build .

cd ../..
mkdir -p build
cp src/zlib/Debug/zlibstaticd.lib build/z.lib


