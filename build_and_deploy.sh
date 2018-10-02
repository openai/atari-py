set -ex

pip install pytest
pip install .
pytest .

if [[ ! -z "$TRAVIS_TAG" ]]; then
    
    PYPLATFORM=$(python3 get_platform.py)
    pip install twine
    python setup.py bdist_wheel --plat-name=$PYPLATFORM

    if [[ ! -z "$DEPLOY_SDIST" ]]; then
        python setup.py sdist       
    fi
    twine upload dist/*
fi

