Python Codon Adaptation Index
=============================
|DOI| |Docs| |Travis| |CodeFactor|

An implementation of `Sharp and Li's 1987
formulation <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC340524/pdf/nar00247-0410.pdf>`_
of the `codon adaption index
<https://en.wikipedia.org/wiki/Codon_Adaptation_Index>`_.

Installation
------------

This module is available from PyPi and can be downloaded with the following command::

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

Contributing
------------

Feel free to contribute, open issues, or let me know about bugs. Anything is
welcome!

Citation
--------

Benjamin Lee. (2017). Python Implementation of Codon Adaptation Index. *Zenodo*.
`http://doi.org/10.5281/zenodo.843854 <http://doi.org/10.5281/zenodo.843854>`_

JOSS citation coming soon.

Contact
-------

I'm available for contact at
`benjamin_lee@college.harvard.edu <mailto:benjamin_lee@college.harvard.edu>`_.

Reference
---------

Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure of
directional synonymous codon usage bias, and its potential applications.
*Nucleic Acids Research*, 15(3), 1281–1295.

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.843854.svg
	:target: https://doi.org/10.5281/zenodo.843854

.. |Docs| image:: https://readthedocs.org/projects/cai/badge/?version=latest
	:target: https://cai.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |Travis| image:: https://travis-ci.org/Benjamin-Lee/CodonAdaptationIndex.svg?branch=master
	:target: https://travis-ci.org/Benjamin-Lee/CodonAdaptationIndex

.. |CodeFactor| image:: https://www.codefactor.io/repository/github/benjamin-lee/codonadaptationindex/badge/master
	:target: https://www.codefactor.io/repository/github/benjamin-lee/codonadaptationindex/overview/master
