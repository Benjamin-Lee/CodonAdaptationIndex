from __future__ import print_function

""" Modified from code licensed as below:

                 Biopython License Agreement

Permission to use, copy, modify, and distribute this software and its
documentation with or without modifications and for any purpose and
without fee is hereby granted, provided that any copyright notices
appear in all copies and that both those copyright notices and this
permission notice appear in supporting documentation, and that the
names of the contributors or copyright holders not be used in
advertising or publicity pertaining to distribution of the software
without specific prior permission.

THE CONTRIBUTORS AND COPYRIGHT HOLDERS OF THIS SOFTWARE DISCLAIM ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL THE
CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY SPECIAL, INDIRECT
OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
OR PERFORMANCE OF THIS SOFTWARE.

Helper script to update Codon tables from the NCBI.
These tables are based on parsing the NCBI file:
ftp://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt
This script is used to update genetic_codes.py
Note that the NCBI sometimes revise the older tables,
so don't just add new tables - replace all of them
and check for any differences in the old tables.
"""

import re

print("#################################################################", file=open("genetic_codes.py", "w+"))
print("# Start of auto-generated output from generate_genetic_codes.py #", file=open("genetic_codes.py", "a"))
print("#################################################################", file=open("genetic_codes.py", "a"))
print("", file=open("genetic_codes.py", "a"))
print("", file=open("genetic_codes.py", "a"))
print("genetic_codes = {", file=open("genetic_codes.py", "a"))

for line in open("gc.prt").readlines():
    if line[:2] == " {":
        names = []
        code_id = None
        aa = None
        start = None
        bases = []
    elif line[:6] == "  name":
        names.append(re.search('"([^"]*)"', line).group(1))
    elif line[:8] == "    name":
        names.append(re.search('"(.*)$', line).group(1))
    elif line == ' Mitochondrial; Mycoplasma; Spiroplasma" ,\n':
        names[-1] = names[-1] + " Mitochondrial; Mycoplasma; Spiroplasma"
    elif line[:4] == "  id":
        code_id = int(re.search('(\d+)', line).group(1))
    elif line[:10] == "  ncbieaa ":
        aa = line[12:12 + 64]
    elif line[:10] == "  sncbieaa":
        start = line[12:12 + 64]
    elif line[:9] == "  -- Base":
        bases.append(line[12:12 + 64])
    elif line[:2] == " }":
        assert names != [] and code_id is not None and aa is not None
        assert start is not None and bases != []
        if len(names) == 1:
            names.append(None)
        print("    {}: {{".format(code_id), file=open("genetic_codes.py", "a"))
        s = "    "
        for i in range(64):
            if aa[i] != "*":
                t = "'%s%s%s': '%s'," % (bases[0][i], bases[1][i],
                                          bases[2][i], aa[i])
                if len(s) + len(t) > 75:
                    print("    ", s, file=open("genetic_codes.py", "a"), sep="")
                    s = "    " + t
                else:
                    s += t
        print("    %s }," % s, file=open("genetic_codes.py", "a"))
        codons = [bases[0][i] + bases[1][i] + bases[2][i]
                  for i in range(64) if aa[i] == "*"]
        codons = [bases[0][i] + bases[1][i] + bases[2][i]
                  for i in range(64) if start[i] == "M"]
        print("", file=open("genetic_codes.py", "a"))
    elif line[:2] == "--" or line in ("\n", "}\n", 'Genetic-code-table ::= {\n'):
        pass
    else:
        raise Exception("Unparsed: " + repr(line))

print("}", file=open("genetic_codes.py", "a"))
print("", file=open("genetic_codes.py", "a"))
print("###############################################################", file=open("genetic_codes.py", "a"))
print("# End of auto-generated output from generate_genetic_codes.py #", file=open("genetic_codes.py", "a"))
print("###############################################################", file=open("genetic_codes.py", "a"))
