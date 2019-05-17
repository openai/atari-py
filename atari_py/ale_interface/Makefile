.PHONY: build clean

build:
	mkdir -p build && cd build && cmake -DCMAKE_GENERATOR_PLATFORM=x64 .. && cmake --build . && cp Debug/ale_c.dll .l

clean:
	rm -rf build
