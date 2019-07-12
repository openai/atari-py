**Status:** Maintenance (expect bug fixes and minor updates)

# atari_py

[![Build Status](https://travis-ci.org/openai/atari-py.svg?branch=master)](https://travis-ci.org/openai/atari-py)

A packaged and slightly-modified version of [https://github.com/bbitmaster/ale_python_interface](https://github.com/bbitmaster/ale_python_interface).

## Supported Systems

atari-py supports Linux and Mac OS X with Python 3.5, 3.6, and 3.7.  Binaries for those platforms are published to [PyPI](https://pypi.org/project/atari-py/)

We also have binaries for Windows, but compiling from source on Windows or using the binaries is not officially supported.

## Installation

To install via pip, run:

```pip install atari-py```
That *should* install a correct binary verison for your OS. If that does not work (or if you would like get the latest-latest
version, or you just want to tinker with the code yourself) see next paragraph. 

## Installation from source

  -  make sure you have `git`, `cmake` and `zlib1g` system packages installed 
  -  clone the repo
  -  run `pip install -e .`

