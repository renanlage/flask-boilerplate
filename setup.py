import sys
from setuptools import setup, find_packages

if 'upload' in sys.argv or 'register' in sys.argv:
    raise Exception("403 - Forbidden")

setup(
    name='project',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/renanlage/flask-boilerplate',
    license='MIT',
    author='Renan Lage',
    author_email='renanlage@gmail.com'
)
