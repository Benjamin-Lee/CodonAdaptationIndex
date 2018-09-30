Usage
=====

Basic Usage
-----------

As covered in :ref:`quickstart`, the basic :func:`~CAI.CAI` function is fast and
easy. Simply import it and get to your science. Note that it also plays nicely
with `Biopython Seq objects <https://biopython.org/wiki/Seq>`_::

    >>> from CAI import CAI
    >>> from Bio.Seq import Seq
    >>> CAI(Seq("AAT"), reference=[Seq("AAC")])
    0.5

The CLI is equally easy to use. For example, to find the CAI of the `native GFP
gene
<https://github.com/Benjamin-Lee/CodonAdaptationIndex/blob/master/example_seqs/gfp.fasta>`_
with respect to the `highly expressed genes in *E. coli*
<https://github.com/Benjamin-Lee/CodonAdaptationIndex/blob/master/example_seqs/ecol.heg.fasta>`_,
only one command is required::

    $ CAI -r example_seqs/ecol.heg.fasta -s example_seqs/gfp.fasta
    0.3753543123685772

.. note::

   Both ``CAI`` and ``cai`` are valid commands.

Advanced Usage
--------------

If you have already computed the weights or RSCU values of the reference set,
you can supply :func:`~CAI.CAI` with one or the other as arguments. They must be
formatted as a dictionary and contain values for every codon.

To calculate RSCU without calculating CAI, you can use :func:`~CAI.RSCU`. :func:`~CAI.RSCU`'s only
required argument is a list of sequences.

Similarly, to calculate the weights of reference sequences, you can use
:func:`~CAI.relative_adaptiveness`. :func:`~CAI.relative_adaptiveness` takes either a list of
sequences as the ``sequences`` parameter or a dictionary of RSCUs as the ``RSCUs``
parameter.

.. Warning:: If you are computing large numbers of CAIs with the same reference
    sequences, first calculate their weights with :func:`~CAI.relative_adaptiveness`
    and then pass that to :func:`~CAI.CAI` to eliminate redundant computation.

So, to modify the example in :ref:`quickstart`::

    >>> from CAI import CAI, relative_adaptiveness
    >>> sequences=["ATGTTT...", "ATGCGC...",...]
    >>> weights = relative_adaptiveness(sequences=sequences)
    >>> CAI("ATG...", weights=weights)
    0.24948128951724224

These are exactly equivalent::

    >>> assert CAI("ATG...", weights=weights) == CAI("ATG...", reference=sequences)
    True

except the former will be faster if you're using the same weights repeatedly.

Other Genetic Codes
-------------------

All functions in CAI support an optional ``genetic_code`` parameter, which is set
by default to 11 (the standard genetic code).

In the CLI, there is an optional "-g" parameter that changes the genetic code::

	$ CAI -s sequence.fasta -r reference_sequences.fasta -g 22
	0.25135779681923687
