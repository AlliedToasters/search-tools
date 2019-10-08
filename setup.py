from setuptools import find_packages, setup
import sys

requirements = [
    'numpy',
    'pandas',
    'pyspark'
]

setup(
    name='search-tools',
    version="0.0.1",
    author="Michael Klear",
    author_email='michael.klear@nike.com',
    url='https://github.nike.com/SNAPE/search-tools',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)