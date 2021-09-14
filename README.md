**Status:** Deprecated (don't expect bug fixes or other updates)

Notice: `atari-py` is fully deprecated and no future updates, bug fixes or releases will be made.
Please use the official [Arcade Learning Environment](https://github.com/mgbellemare/Arcade-Learning-Environment) Python package (`ale-py`) instead;
it is fully backwards compatible with all `atari-py` code.


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

## ROMs

In order to import ROMS, you need to download `Roms.rar` from the [Atari 2600 VCS ROM Collection](http://www.atarimania.com/rom_collection_archive_atari_2600_roms.html) and extract the `.rar` file.  Once you've done that, run:

`python -m atari_py.import_roms <path to folder>`

This should print out the names of ROMs as it imports them.  The ROMs will be copied to your `atari_py` installation directory.

## Installation from source

  -  make sure you have `git`, `cmake`, `zlib1g`, and, on Linux, `zlib1g-dev` system packages installed 
  -  clone the repo
  -  run `pip install -e .`

## Included ROMs

The following non-commercial ROMs are included with atari-py for testing purposes:

* Tetris26 by Colin Hughes
