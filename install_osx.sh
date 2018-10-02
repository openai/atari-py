set -ex
CONDA_VER=3.7.0
curl https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-MacOSX-x86_64.sh -o ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
ln -s $HOME/miniconda/bin/pip $HOME/miniconda/bin/pip3
export PATH="$HOME/miniconda/bin:$PATH"
python --version
