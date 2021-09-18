from Bio.SeqUtils.CodonUsage import CodonAdaptationIndex

cai = CodonAdaptationIndex()

# https://github.com/yanlinlin82/EMBOSS/blob/master/emboss/data/CODONS/Eyeastcai.cut

Eyeastcai_cut = """\
TAG 	*	     0.040      0.170	1
TGA 	*	     0.040      0.170	1
TAA 	*	     0.920      3.820	22
GCG 	A	     0.000      0.000	0
GCA 	A	     0.010      1.040	6
GCC 	A	     0.240     22.420	130
GCT 	A	     0.750     71.610	411
TGC 	C	     0.070      0.520	3
TGT 	C	     0.930      6.610	39
GAT 	D	     0.360     19.640	112
GAC 	D	     0.640     34.940	202
GAG 	E	     0.020      1.220	5
GAA 	E	     0.980     52.670	305
TTT 	F	     0.100      3.300	19
TTC 	F	     0.900     29.200	168
GGA 	G	     0.000      0.170	1
GGG 	G	     0.000      0.350	2
GGC 	G	     0.020      1.560	9
GGT 	G	     0.970     79.610	459
CAT 	H	     0.200      4.350	25
CAC 	H	     0.800     17.730	102
ATA 	I	     0.000      0.000	0
ATT 	I	     0.460     26.070	149
ATC 	I	     0.540     31.110	181
AAA 	K	     0.120     11.120	65
AAG 	K	     0.880     84.130	483
CTC 	L	     0.000      0.000	1
CTG 	L	     0.000      0.170	1
CTT 	L	     0.000      0.350	2
CTA 	L	     0.030      2.430	14
TTA 	L	     0.100      7.470	42
TTG 	L	     0.860     62.400	359
ATG 	M	     1.000     18.950	109
AAT 	N	     0.050      1.910	11
AAC 	N	     0.950     36.160	208
CCG 	P	     0.000      0.000	0
CCC 	P	     0.010      0.350	2
CCT 	P	     0.040      1.740	10
CCA 	P	     0.950     36.680	211
CAG 	Q	     0.000      0.000	1
CAA 	Q	     1.000     26.590	153
CGA 	R	     0.000      0.000	0
CGC 	R	     0.000      0.000	0
CGG 	R	     0.000      0.000	0
AGG 	R	     0.000      0.170	1
CGT 	R	     0.120      7.650	43
AGA 	R	     0.870     54.580	314
TCG 	S	     0.000      0.170	1
AGT 	S	     0.010      0.700	4
AGC 	S	     0.020      1.040	6
TCA 	S	     0.020      1.220	7
TCC 	S	     0.380     22.940	133
TCT 	S	     0.560     33.720	192
ACG 	T	     0.000      0.170	1
ACA 	T	     0.010      0.350	2
ACT 	T	     0.470     25.900	151
ACC 	T	     0.520     28.680	164
GTA 	V	     0.000      0.000	0
GTG 	V	     0.010      0.700	5
GTC 	V	     0.450     40.150	231
GTT 	V	     0.540     48.500	278
TGG 	W	     1.000      8.170	47
TAT 	Y	     0.060      1.560	10
TAC 	Y	     0.940     24.680	141"""

w = {}
for line in Eyeastcai_cut.splitlines():
    trip, aa, we, fr, x = line.split()
    w[trip] = float(we)

cai.set_cai_index(w)

S = "CGACGCCGGCGACGCCGGCGACGCCGGCGACGCCGG"
S = "ATGATGATGATGATGATGATGATGATGATG"

cai.cai_for_gene(S)

import CAI

CAI.CAI(S, weights=w)




