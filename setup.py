
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""

from setuptools import setup
from setuptools import find_packages
from os import path
import re

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = []
with open("requirements.txt", encoding="utf-8") as f:
    for line in f.readlines():
        install_requires.append(re.split(r"(<|>|=)=", line)[0])

setup(name="CAI",
      use_scm_version={"write_to": "src/CAI/_version.py"},
      packages=find_packages("src"),
      package_dir={"": "src"},
      description="Python implementation of codon adaptation index",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Benjamin Lee",
      author_email="benjamin_lee@college.harvard.edu",
      url="https://github.com/Benjamin-Lee/CodonAdaptationIndex",
      install_requires=install_requires,
      setup_requires=["setuptools_scm"],
      license="MIT",
      # use_2to3=True,
      python_requires=">=3.7",
      entry_points={"console_scripts": ["CAI=CAI.cli:cli"]},
      classifiers=["Intended Audience :: Science/Research",
                   "Topic :: Scientific/Engineering :: Bio-Informatics",
                   "Programming Language :: Python", ], )
