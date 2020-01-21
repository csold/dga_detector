from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Classifies domains into legit or dga',
    author='Chris Old',
    license='MIT',
    entry_points={
        'console_scripts': ['dga-cli=src.cli:main']
    }
)
