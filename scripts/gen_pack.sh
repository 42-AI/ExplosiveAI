#! /bin/bash


# TODO argument -> src
rm -rf *.egg-info/ build/ dist/
pip uninstall -y StyleMirror
python3 setup.py bdist_wheel
pip install dist/StyleMirror-0.1.0-py3-none-any.whl% 