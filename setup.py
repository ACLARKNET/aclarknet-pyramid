from setuptools import find_packages
from setuptools import setup

setup(
    name='aclarknet', 
    packages=find_packages(),
    install_requires=[
        'pyramid',
    ],
)
