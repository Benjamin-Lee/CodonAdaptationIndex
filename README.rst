Python Codon Adaptation Index
=============================
|DOI| |Docs| |Travis| |CodeFactor| |PyPI|

An implementation of `Sharp and Li's 1987
formulation <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC340524/pdf/nar00247-0410.pdf>`_
of the `codon adaption index
<https://en.wikipedia.org/wiki/Codon_Adaptation_Index>`_.

Installation
------------

This module is available from PyPI and can be downloaded with the following command::

	$ pip install CAI

To install the latest development version::

	$ pip install git+https://github.com/Benjamin-Lee/CodonAdaptationIndex.git

.. _quickstart:

Quickstart
----------

Finding the CAI of a sequence is easy::

	>>> from CAI import CAI
	>>> CAI("ATG...", reference=["ATGTTT...", "ATGCGC...",...])
	0.24948128951724224

Similarly, from the command line::

	$ CAI -s sequence.fasta -r reference_sequences.fasta
	0.24948128951724224

Determining which sequences to use as the reference set is left to the user,
though the `HEG-DB <http://genomes.urv.cat/HEG-DB/>`_ is a great resource of
highly expressed genes.

Contributing and Getting Support
--------------------------------

If you encounter any issues using CAI, feel free to `create an issue
<https://github.com/Benjamin-Lee/CodonAdaptationIndex/issues>`_.

To contribute to the project, please `create a pull request
<https://github.com/Benjamin-Lee/CodonAdaptationIndex/pulls>`_. For more
information on how to do so, please look at GitHub's `documentation on pull
requests <https://help.github.com/articles/about-pull-requests>`_.

Citation
--------

Lee, B. D. (2018). Python Implementation of Codon Adaptation Index. *Journal of
Open Source Software, 3*(30), 905. `https://doi.org/10.21105/joss.00905
<https://doi.org/10.21105/joss.00905>`_

```
@article{Lee2018,
  doi = {10.21105/joss.00905},
  url = {https://doi.org/10.21105/joss.00905},
  year  = {2018},
  month = {oct},
  publisher = {The Open Journal},
  volume = {3},
  number = {30},
  pages = {905},
  author = {Benjamin D. Lee},
  title = {Python Implementation of Codon Adaptation Index},
  journal = {Journal of Open Source Software}
}
```

Contact
-------

I'm available for contact at
`benjamin_lee@college.harvard.edu <mailto:benjamin_lee@college.harvard.edu>`_.

Reference
---------

Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure of
directional synonymous codon usage bias, and its potential applications.
*Nucleic Acids Research*, 15(3), 1281–1295.

.. |DOI| image:: http://joss.theoj.org/papers/8adf6bd9fd6391d5343d15ea0b6b6525/status.svg
	:target: http://joss.theoj.org/papers/8adf6bd9fd6391d5343d15ea0b6b6525

.. |Docs| image:: https://readthedocs.org/projects/cai/badge/?version=latest
	:target: https://cai.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |Travis| image:: https://travis-ci.org/Benjamin-Lee/CodonAdaptationIndex.svg?branch=master
	:target: https://travis-ci.org/Benjamin-Lee/CodonAdaptationIndex

.. |CodeFactor| image:: https://www.codefactor.io/repository/github/benjamin-lee/codonadaptationindex/badge/master
	:target: https://www.codefactor.io/repository/github/benjamin-lee/codonadaptationindex/overview/master

.. |PyPI| image:: https://img.shields.io/pypi/v/CAI.svg
	:target: https://pypi.org/project/CAI/
