from CAI import RSCU
import pytest


def test_sum():
    # The sum of the RSCUs should be equal to the number of codons
    assert abs(sum(RSCU(["AAC"]).values()) - len(RSCU(["AAC"]))) < 0.0001
    assert abs(sum(RSCU(["AACGATACGGCACGT"]).values()) - len(RSCU(["AAC"]))) < 0.0001


def test_rscu():
    assert RSCU(["AAC"]) == {
        "AAA": 1.0,
        "AAC": 1 / (0.5 * (1 + 0.5)),
        "AAG": 1.0,
        "AAT": 0.5 / (0.5 * (1 + 0.5)),
        "ACA": 1.0,
        "ACC": 1.0,
        "ACG": 1.0,
        "ACT": 1.0,
        "AGA": 1.0,
        "AGC": 1.0,
        "AGG": 1.0,
        "AGT": 1.0,
        "ATA": 1.0,
        "ATC": 1.0,
        "ATG": 1.0,
        "ATT": 1.0,
        "CAA": 1.0,
        "CAC": 1.0,
        "CAG": 1.0,
        "CAT": 1.0,
        "CCA": 1.0,
        "CCC": 1.0,
        "CCG": 1.0,
        "CCT": 1.0,
        "CGA": 1.0,
        "CGC": 1.0,
        "CGG": 1.0,
        "CGT": 1.0,
        "CTA": 1.0,
        "CTC": 1.0,
        "CTG": 1.0,
        "CTT": 1.0,
        "GAA": 1.0,
        "GAC": 1.0,
        "GAG": 1.0,
        "GAT": 1.0,
        "GCA": 1.0,
        "GCC": 1.0,
        "GCG": 1.0,
        "GCT": 1.0,
        "GGA": 1.0,
        "GGC": 1.0,
        "GGG": 1.0,
        "GGT": 1.0,
        "GTA": 1.0,
        "GTC": 1.0,
        "GTG": 1.0,
        "GTT": 1.0,
        "TAC": 1.0,
        "TAT": 1.0,
        "TCA": 1.0,
        "TCC": 1.0,
        "TCG": 1.0,
        "TCT": 1.0,
        "TGC": 1.0,
        "TGG": 1.0,
        "TGT": 1.0,
        "TTA": 1.0,
        "TTC": 1.0,
        "TTG": 1.0,
        "TTT": 1.0,
    }


def test_str_arg():
    # raise an error if given a string
    with pytest.raises(ValueError):
        RSCU("AAA")


def test_seq():
    # make sure module works on Bio.Seq objects
    from Bio.Seq import Seq

    assert RSCU([Seq("AGC")]) == RSCU(["AGC"])
    assert RSCU([Seq("AACGATACGGCACGT")]) == RSCU(["AACGATACGGCACGT"])


def test_multiple_seqs():
    # multiple sequences should be identical to their concatenation
    assert RSCU(["AAC", "ATC"]) == RSCU(["AACATC"])
    assert RSCU(["AAC", "ATC", "AACGATACGGCACGT"]) == RSCU(["AACATCAACGATACGGCACGT"])


def test_stop_codon():
    # stop codons should be equivalent to an empty string since they don't have RSCUs
    assert RSCU(["TAA"]) == RSCU(["TAG"]) == RSCU(["   "])
