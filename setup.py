#!/usr/bin/env python
from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="vedge_detector",
    version="0.0.1",
    description="VEdge detector model",
    author="Martin Rogers",
    author_email="marrog@bas.ac.uk",
    url="https://github.com/MartinSJRogers/VEdge_Detector",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
)