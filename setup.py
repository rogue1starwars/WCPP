"""
This is the setup module for the WCPP package.

This module contains the setup configuration for setuptools,
which is used to package the project for distribution.

"""

from setuptools import setup

setup(
    name="wcpp",
    version="1.0.0",
    install_requires=[
        "crc",
        "pytest",
    ],
    packages=["wcpp"],
    package_dir={"wcpp": "wcpp"},
)
