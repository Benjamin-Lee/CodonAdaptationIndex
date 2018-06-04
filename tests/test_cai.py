from CAI import CAI, RSCU, relative_adaptiveness
import pytest
import math

def test_bad_args():
    # make sure bad arguments raise errors
    with pytest.raises(TypeError):
        CAI("AAC") # no reference data
    with pytest.raises(TypeError):
        CAI("AAC", sequences=["AAC"], RSCUs=RSCU(["AAC"]))

def test_cai():
    # first, make sure all arguments get the same result
    assert CAI("AAC", sequences=["AAC"]) == CAI("AAC", RSCUs=RSCU(["AAC"])) == CAI("AAC", weights=relative_adaptiveness(sequences=["AAC"])) == 1.0

    # check other sequences
    assert CAI("AAT", sequences=["AAC"]) == 0.5
    assert CAI("AATAAT", sequences=["AAC"]) == 0.5
    assert CAI("AAT"*100, sequences=["AAC"]) == 0.5

def test_only_non_synonymous():
    assert math.isnan(CAI("ATG", sequences=["AAC"]))

def test_stop_codon():
    # stop codons don't count for CAI
    assert CAI("AAT", sequences=["AAC"]) == CAI("AATTAA", sequences=["AAC"]) == CAI("TAAAAT", sequences=["AAC"])

def test_alternate_genetic_code():
    # the differing stop codon
    assert CAI("AATTGA", sequences=["AAC"]) != CAI("AATTGA", sequences=["AAC"], genetic_code=10)
