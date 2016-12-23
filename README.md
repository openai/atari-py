# atari_py

[![Build Status](https://travis-ci.org/openai/atari-py.svg?branch=master)](https://travis-ci.org/openai/atari-py)

A Windows-MSYS2-MinGW compatible version of [https://github.com/openai/ale_python_interface](https://github.com/openai/ale_python_interface).

## Installation

1) Install MSYS2 and follow post-install instructions: [https://msys2.github.io/](https://msys2.github.io/)

2) Install MSYS2 packages (via MSYS terminal):

```pacman -S base-devel mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake```

3) Append to current Windows User PATH: ";C:\msys64\mingw64\bin;C:\msys64\usr\bin"

i.e. Start->right-click Computer->Properties->Advanced System Settings->Environment Variables->edit User variables PATH

4) Install Xming: [https://sourceforge.net/projects/xming/])(https://sourceforge.net/projects/xming/)
    Add a new windows PATH variable (same method as #3): Name=DISPLAY, Value=:0

Or just remember to set it in your cmd.exe environment:

```set DISPLAY=:0```

5) Install atari-py and OpenAI Gym

```git clone https://github.com/rybskej/atari-py```

```cd atari-py```

```make && python setup.py install && pip install "gym[atari]"```

You can also just build the C++ code via `make`, and then add
this repo to your `PYTHONPATH`:

```set PYTHONPATH="C:\path\to\atari-py:$PYTHONPATH"```

### Common issues

