.PHONY: build clean

build:
	make -C atari_py/ale_interface build

clean:
	rm -rf dist atari_py.egg-info
	make -C atari_py/ale_interface clean

package_data:
	( echo "ale_interface/build/*.so" && echo "ale_interface/build/ale" && cd atari_py && git ls-files |grep -v \\.py$ ) > atari_py/package_data.txt

upload:
	make clean
	rm -rf dist
	python setup.py sdist
	twine upload dist/*
