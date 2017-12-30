# Python Codon Adaptation Index
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.843854.svg)](https://doi.org/10.5281/zenodo.843854)

An implementation of Sharp and Li's 1987 formulation of the codon adaption index.

## Reference
Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure of directional synonymous codon usage bias, and its potential applications. _Nucleic Acids Research_, 15(3), 1281–1295.

## Installation 
This module is available from PyPi and can be downloaded with the following command:

	pip install CAI
	
## Usage
### Simple Usage
The simplest way to calculate the CAI of a sequence is to call `CAI()` with the sequence as the first (required) argument and with the `sequences` argument included. The sequences argument is a list of reference sequences. Determining which sequences to use as the reference set is left to the user.

```python

from CAI import CAI

print CAI("ATGGATTAC...", sequences=["ATGTTTGCTAAA", "ATGCGATACAGC",...])

```
### Advanced Usage
If you have already computed the weights or RSCU values of the reference set, you can supply `CAI()` with one or the other as arguments. They must be formatted as a dictionary and contain values for every codon.

**_N.B._ if you are computing large numbers of CAIs with the same reference sequences, first calculate their weights and then pass that to `CAI()` to eliminate redundant computation.**

To calculate RSCU without calculating CAI, you can use `RSCU()`. `RSCU()`'s only required argument is a list of sequences.

Similarly, to calculate the weights of reference sequences, you can use `relative_adaptiveness()`. `relative_adaptiveness()` takes either a list of sequences as the `sequences` parameter or a dictionary of RSCUs as the `RSCUs` parameter. 

### Other Genetic Codes

All functions in CAI support an optional `genetic_code` parameter, which is set by default to 1 (the standard genetic code). You may set it to any genetic code within [gc.prt](/gc.prt). 

## API Reference
### `RSCU(sequences, genetic_code=1)`

Argument  | Details
--------- | -------
sequences | List of DNA sequence strings. Required.
genetic_code | Integer containing the genetic code ID. Optional.

#### Output
A dictionary containing every codon as the key and its RSCU as the value.

### `relative_adaptiveness(sequences=[], RSCUs={}, genetic_code=1)`

Argument  | Details
--------- | -------
sequences | List of DNA sequence strings. Optional.
RSCUs | Dictionary of RSCU values for each codon. Optional.
genetic_code | Integer containing the genetic code ID. Optional.

#### Note
One of `sequences` or `RSCUs` is required. 

#### Output
A dictionary containing every codon as the key and its weight as the value.

### `CAI(sequence, weights=[], RSCUs=[], sequences=[], genetic_code=1)`

Argument  | Details
--------- | -------
sequence | String of DNA sequence to calculate CAI for. Required.
weights | Dictionary of weight values for each codon. Optional.
RSCUs | Dictionary of RSCU values for each codon. Optional.
sequences | List of DNA sequence strings. Optional.
genetic_code | Integer containing the genetic code ID. Optional.

#### Note
One of `sequences`, `RSCUs`, or `weights` is required.

#### Output
A float of the CAI of the sequence.

## Contributing
Feel free to contribute, open issues, or let me know about bugs. Anything is welcome!

## Citation 
Benjamin Lee. (2017). Python Implementation of Codon Adaptation Index. _Zenodo_. http://doi.org/10.5281/zenodo.843854

## Contact
I'm available for contact at [benjamin_lee@college.harvard.edu](mailto:benjamin_lee@college.harvard.edu).
