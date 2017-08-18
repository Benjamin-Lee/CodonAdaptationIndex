from setuptools import setup

setup(
    name = 'CAI',
    packages = ["CAI"],
    version = '0.1.7',
    description = 'Python implementation of codon adaptation index',
    author = 'Benjamin Lee',
    author_email = 'benjamin_lee@college.harvard.edu',
    url = 'https://github.com/Benjamin-Lee/CodonAdaptationIndex', # use the URL to the github repo
    classifiers = ["Intended Audience :: Science/Research",
                   "Topic :: Scientific/Engineering :: Bio-Informatics",
                   "Programming Language :: Python"],
    install_requires=['scipy'],
    license="MIT",
    use_2to3=True
)