# CAI.py: Python Codon Adaptation Index
## by [Benjamin Lee](mailto:benjamin_lee@college.harvard.edu)

An implementation of Sharp and Li's 1987 formulation of the codon adaption index.

## Reference
Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure of directional synonymous codon usage bias, and its potential applications. _Nucleic Acids Research_, 15(3), 1281–1295.

## Installation 
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

To calculate the RSCU without calculating the CAI, you can use `RSCU()`. `RSCU()`s only required parameter a list of sequences.

Similarly, to calculate the weights of a reference set, you can use `relative_adaptiveness()`. `relative_adaptiveness()` takes either a list of sequences as the `sequences` parameter or a dictionary of RSCUs as the `RSCUs` parameter. 

### Other Genetic Codes

All functions in CAI support an optional `genetic_code` parameter, which is set by default to 1 (the standard genetic code). You may set it to any genetic code within [gc.prt](/gc.prt). 

## Contributing
Feel free to contribute, open issues, or let me know about bugs. Anything is welcome!
