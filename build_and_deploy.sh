set -ex

python3 -m pip install pytest
python3 -m pip install .
python3 -m pytest .

if [[ ! -z "$TRAVIS_TAG" ]]; then
    
    PYPLATFORM=$(python3 get_platform.py)
    python3 -m pip install --user twine
    python3 -m twine upload /tmp/wheelhouse/atari_py-*

    python3 setup.py bdist_wheel --plat-name=$PYPLATFORM

    if [[ ! -z "$DEPLOY_SDIST" ]]; then
        python3 setup.py sdist       
        python3 -m twine upload dist/*
    fi
fi

