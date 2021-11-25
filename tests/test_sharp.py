from CAI import CAI
import pytest
import math

"""
The CAI is calculated for the E. coli rpsU gene given as an example on 
page 1285 in Sharp 1987. This sequence is available from 
Genbank (NC_000913 REGION: 3210781..3210996).

atg ccg gta att aaa gta cgtgaaaacgagccgttcgacgtagctctgcgtcgctt
    ||| ||| ||| ||| |||
   .CCG.GTA.ATT.AAA.GTA.

caagcgttcctgcgaaaaagcaggtgttctggcggaagttcgtcgtcgtgagttctatgaaa
aaccgactaccgaacgtaagcgcgctaaagcttctgcagtgaaacgtcacgcgaagaaactg
gctcgcgaaaacgcacgccgcactcgtctgtactaa
"""



def test_sharp1987_fig():
    sharp_table_1 = """\
    AA Tri RSCUe we RSCUy wy
    Phe TTT 0.456 0.296 0.203 0.113
    Phe TTC 1.544 1.000 1.797 1.000
    Leu TTA 0.106 0.020 0.601 0.117
    Leu TTG 0.106 0.020 5.141 1.000
    Leu CTT 0.225 0.042 0.029 0.006
    Leu CTC 0.198 0.037 0.014 0.003
    Leu CTA 0.040 0.007 0.200 0.039
    Leu CTG 5.326 1.000 0.014 0.003
    Ile ATT 0.466 0.185 1.352 0.823
    Ile ATC 2.525 1.000 1.643 1.000
    Ile ATA 0.008 0.003 0.005 0.003
    Met ATG 1.000 1.000 1.000 1.000
    Val GTT 2.244 1.000 2.161 1.000
    Val GTC 0.148 0.066 1.796 0.831
    Val GTA 1.111 0.495 0.004 0.002
    Val GTG 0.496 0.221 0.039 0.018
    Ser TCT 2.571 1.000 3.359 1.000
    Ser TCC 1.912 0.744 2.327 0.693
    Ser TCA 0.198 0.077 0.122 0.036
    Ser TCG 0.044 0.017 0.017 0.005
    Pro CCT 0.231 0.070 0.179 0.047
    Pro CCC 0.038 0.012 0.036 0.009
    Pro CCA 0.442 0.135 3.776 1.000
    Pro CCG 3.288 1.000 0.009 0.002
    Thr ACT 1.804 0.965 1.899 0.921
    Thr ACC 1.870 1.000 2.063 1.000
    Thr ACA 0.141 0.076 0.025 0.012
    Thr ACG 0.185 0.099 0.013 0.006
    Ala GCT 1.877 1.000 3.005 1.000
    Ala GCC 0.228 0.122 0.948 0.316
    Ala GCA 1.099 0.586 0.044 0.015
    Ala GCG 0.796 0.424 0.004 0.001
    Tyr TAT 0.386 0.239 0.132 0.071
    Tyr TAC 1.614 1.000 1.868 1.000
    His CAT 0.451 0.291 0.394 0.245
    His CAC 1.549 1.000 1.606 1.000
    Gln CAA 0.220 0.124 1.987 1.000
    Gln CAG 1.780 1.000 0.013 0.007
    Asn AAT 0.097 0.051 0.100 0.053
    Asn AAC 1.903 1.000 1.900 1.000
    Lys AAA 1.596 1.000 0.237 0.135
    Lys AAG 0.404 0.253 1.763 1.000
    Asp GAT 0.605 0.434 0.713 0.554
    Asp GAC 1.395 1.000 1.287 1.000
    Glu GAA 1.589 1.000 1.968 1.000
    Glu GAG 0.411 0.259 0.032 0.016
    Cys TGT 0.667 0.500 1.857 1.000
    Cys TGC 1.333 1.000 0.143 0.077
    Trp TGG 1.000 1.000 1.000 1.000
    Arg CGT 4.380 1.000 0.718 0.137
    Arg CGC 1.561 0.356 0.008 0.002
    Arg CGA 0.017 0.004 0.008 0.002
    Arg CGG 0.017 0.004 0.008 0.002
    Ser AGT 0.220 0.085 0.070 0.021
    Ser AGC 1.055 0.410 0.105 0.031
    Arg AGA 0.017 0.004 5.241 1.000
    Arg AGG 0.008 0.002 0.017 0.003
    Gly GGT 2.283 1.000 3.898 1.000
    Gly GGC 1.652 0.724 0.077 0.020
    Gly GGA 0.022 0.010 0.009 0.002
    Gly GGG 0.043 0.019 0.017 0.004"""
    
    
    we = {}
    for line in sharp_table_1.splitlines()[1:]:
        _, cdn,_ , w, *_ = line.split()
        we[cdn] = float(w)
    
    rpsU = ("atgccggtaattaaagtacgtgaaaacgagccgttcgacgtagctctgcgtcgctt"
            "caagcgttcctgcgaaaaagcaggtgttctggcggaagttcgtcgtcgtgagttct"
            "atgaaaaaccgactaccgaacgtaagcgcgctaaagcttctgcagtgaaacgtcac"
            "gcgaagaaactggctcgcgaaaacgcacgccgcactcgtctgtactaa")

    assert math.isclose(CAI(rpsU, weights=we), 
                            0.7260113974828158)
    
    
    
    
    
    
    

