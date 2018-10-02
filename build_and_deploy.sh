set -ex

python --version
python -m pip install pytest
python -m pip install .
pytest .

if [[ ! -z "$TRAVIS_TAG" ]]; then
    
    PYPLATFORM=$(python3 get_platform.py)
    python -m pip install --user twine
    python -m twine upload /tmp/wheelhouse/atari_py-*

    python setup.py bdist_wheel --plat-name=$PYPLATFORM

    if [[ ! -z "$DEPLOY_SDIST" ]]; then
        python setup.py sdist       
        python -m twine upload dist/*
    fi
fi

