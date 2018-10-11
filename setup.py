from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CAI',
    packages=["CAI"],
    version='1.0.3',
    description='Python implementation of codon adaptation index',
    long_description=long_description,
    author='Benjamin Lee',
    author_email='benjamin_lee@college.harvard.edu',
    url='https://github.com/Benjamin-Lee/CodonAdaptationIndex', # use the URL to the github repo
    classifiers=["Intended Audience :: Science/Research",
                 "Topic :: Scientific/Engineering :: Bio-Informatics",
                 "Programming Language :: Python"],
    install_requires=['scipy', 'biopython', 'click>=7'],
    tests_require=["pytest"],
    setup_requires=['pytest-runner'],
    license="MIT",
    use_2to3=True,
    python_requires='>=3.4',
    entry_points={'console_scripts': ['CAI=CAI.cli:cli']},
)
