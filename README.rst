Python Codon Adaptation Index
=============================
|DOI| |Docs|

An implementation of Sharp and Li's 1987 formulation of the `codon adaption
index <https://en.wikipedia.org/wiki/Codon_Adaptation_Index>`_.

Installation
------------

This module is available from PyPi and can be downloaded with the following command::

	$ pip install CAI

Usage
-----

Simple Usage
************

The simplest way to calculate the CAI of a sequence is to call `CAI()` with the
sequence as the first (required) argument and with the `sequences` argument
included. The sequences argument is a list of reference sequences::

	>>> from CAI import CAI
	>>> CAI("ATGGATTAC...", sequences=["ATGTTTGCTAAA", "ATGCGATACAGC",...])

Determining which sequences to use as the reference set is left to the user.

Advanced Usage
**************

If you have already computed the weights or RSCU values of the reference set,
you can supply :func:`~CAI.CAI` with one or the other as arguments. They must be
formatted as a dictionary and contain values for every codon.

.. note:: If you are computing large numbers of CAIs with the same reference sequences,
	first calculate their weights and then pass that to :func:`~CAI.CAI` to
	eliminate redundant computation.

To calculate RSCU without calculating CAI, you can use :func:`~CAI.RSCU`. :func:`~CAI.RSCU`'s only
required argument is a list of sequences.

Similarly, to calculate the weights of reference sequences, you can use
:func:`~CAI.relative_adaptiveness`. :func:`~CAI.relative_adaptiveness` takes either a list of
sequences as the ``sequences`` parameter or a dictionary of RSCUs as the ``RSCUs``
parameter.

Other Genetic Codes
*******************

All functions in CAI support an optional ``genetic_code`` parameter, which is set
by default to 11 (the standard genetic code).


Contributing
------------

Feel free to contribute, open issues, or let me know about bugs. Anything is
welcome!

Citation
--------

Benjamin Lee. (2017). Python Implementation of Codon Adaptation Index. *Zenodo*.
`http://doi.org/10.5281/zenodo.843854 <http://doi.org/10.5281/zenodo.843854>`_

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
