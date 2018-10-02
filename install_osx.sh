set -ex
PYTHON_VER=3.7.0
brew install wget
wget https://repo.continuum.io/miniconda/Miniconda3-${PYTHON_VER}-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
ln -s $HOME/miniconda/bin/pip $HOME/miniconda/bin/pip3
ln -s $HOME/miniconda/bin/python $HOME/miniconda/bin/python3
