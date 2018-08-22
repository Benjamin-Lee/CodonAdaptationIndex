---
title: 'Python Implementation of Codon Adaptation Index'
tags:
  - Python
  - bioinformatics
  - computational biology
  - codon adaptation index
  - molecular biology
authors:
  - name: Benjamin Lee
    orcid: 0000-0002-7133-8397
    affiliation: "1"
affiliations:
 - name: School of Engineering and Applied Sciences, Harvard University
   index: 1
date: 4 June 2018
bibliography: paper.bib
---

# Summary

Amino acids, the building blocks of proteins, are encoded in DNA by triplets of
nucleotides called codons. Notably, the synonymous codons for an amino acid are
not used in equal proportions in coding DNA sequences. Rather, they exhibit a
bias which varies from organism to organism. The codon adaptation index (CAI) is
a measurement of this bias with respect to a set of reference genes [@Sharp1987]. It has been used in the context of heterologous protein expression
[@Grote2005], virus attenuation [@Eschke2018], and cotranslational protein
folding prediction [@Rodriguez2017].

`CAI` is a Python package for the efficient calculation of this metric, along
with the associated relative synonymous codon usage (RSCU) and relative
adaptiveness metrics. In addition, `CAI` includes a command line interface for
the calculation of CAI from FASTA files containing DNA sequences. For example,
to find the CAI of the sequence within `sequence.fasta` with respect to the
sequences within `reference.fasta`, one need only run:

```shell
$ CAI -s sequence.fasta -r reference.fasta
```

Similarly, using the Python API:

```python
>>> from CAI import CAI
>>> from Bio import SeqIO # to parse FASTA files
>>> reference = [seq.seq for seq in SeqIO.parse("reference.fasta", "fasta")]
>>> sequence = SeqIO.read("sequence.fasta", "fasta")
>>> CAI(sequence, reference=reference)
0.24948128951724224
```

In comparison to other Python implementations of the CAI metric [@Cock2009],
`CAI` features a CLI, supports multiple genetic codes, can yield the RSCU of
reference sets, and correctly handles the case of missing codons in the
reference set. Moreover, on a benchmark to determine the CAI of 100 genes
consisting of 3,000 random base pairs each with respect to highly expressed
genes in _Escherichia coli_, `CAI` performed 39.6% faster.

In conclusion, `CAI` is a significantly faster and more versatile method to
determine the CAI, RSCU, and relative adaptiveness of DNA sequences.



# Acknowledgements

The author would like to thank Paul Gamble, Karl Ni, and Todd Stavish for their
feedback on the manuscript and documentation of this project.

# References
