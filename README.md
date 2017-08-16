# Python Codon Adaptation Index

An implementation of Sharp and Li's 1987 formulation of the codon adaption index.

## Reference
Sharp, P. M., & Li, W. H. (1987). The codon adaptation index--a measure of directional synonymous codon usage bias, and its potential applications. _Nucleic Acids Research_, 15(3), 1281–1295.

## Installation 
	pip install CAI
	
## Usage
### Simple Usage
The simple
```python

from CAI import CAI

print CAI("ATGGATTAC...", sequences=["ATGTTTGCTAAA", "ATGCGATACAGC",...])

```