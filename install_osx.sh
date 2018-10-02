set -ex
PYTHON_VER=3.7.0
curl https://repo.continuum.io/miniconda/Miniconda3-${PYTHON_VER}-MacOSX-x86_64.sh -o ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
ln -s $HOME/miniconda/bin/pip $HOME/miniconda/bin/pip3
python --version
