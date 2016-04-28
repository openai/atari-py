# atari_py

[![Build Status](https://travis-ci.org/openai/atari-py.svg?branch=master)](https://travis-ci.org/openai/atari-py)

A packaged and slightly-modified version of [https://github.com/bbitmaster/ale_python_interface](https://github.com/bbitmaster/ale_python_interface).

## Installation

To install via pip, run:

```pip install atari-py```

Alternatively, you can install using setuptools using:

```python setup.py install```

You can also trigger a build of the C++ code via `make`, and then add
this repo to your `PYTHONPATH`:

```export PYTHONPATH=/path/to/atari-py:$PYTHONPATH```

### Common issues

- Make sure you have `cmake` installed. On OSX, you probably want
  `brew install cmake`.
