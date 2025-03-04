# this is a setup.py file of my project called OOP18. the source code is in src

from setuptools import setup, find_packages

setup(
    name='OOP18',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
