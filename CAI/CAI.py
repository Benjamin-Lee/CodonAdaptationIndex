from itertools import chain
from genetic_codes import genetic_codes
from scipy.stats.mstats import gmean

def _synonymous_codons(genetic_code_dict):

    # invert the genetic code dictionary to map each amino acid to its codons
    codons_for_amino_acid = {}
    for codon, amino_acid in genetic_code_dict.iteritems():
        codons_for_amino_acid[amino_acid] = codons_for_amino_acid.get(amino_acid, [])
        codons_for_amino_acid[amino_acid].append(codon)

    # create dictionary of synonmyous codons
    # Example: {'CTT': ['CTT', 'CTG', 'CTA', 'CTC', 'TTA', 'TTG'], 'ATG': ['ATG']...}
    return {codon : codons_for_amino_acid[genetic_code_dict[codon]] for codon in genetic_code_dict.keys()}


def RSCU(sequences, genetic_code=1):
    """
    Take a list of sequences in a reference set and an optional genetic code ID
    and returns the RSCU ('the observed frequency of [a] codon divided by the
    frequency expected under the assumption of equal usage of the synonymous codons
    for an amino acid' (page 1283)) as a dictionary
    """

    # convert genetic code ID to dictionary 
    genetic_code = genetic_codes[genetic_code]

    # ensure all input sequences are divisible by three
    for sequence in sequences:
        if len(sequence) % 3 != 0:
            raise ValueError("Input sequence not divisible by three")
        if len(sequence) == 0:
            raise ValueError("Input sequence cannot be empty")

    # count the number of each codon in the sequences
    sequences = [[sequence[i:i+3].upper() for i in range(0, len(sequence), 3)] for sequence in sequences]
    codons = list(chain.from_iterable(sequences)) # flat list of all codons (to be used for counting)
    counts = {i: codons.count(i) for i in genetic_code.keys()}

    # "if a certain codon is never used in the reference set... assign [it] a value of 0.5" (page 1285)
    for codon in counts:
        if counts[codon] == 0:
            counts[codon] = 0.5

    # determine the synonymous codons for the genetic code
    synonymous_codons = _synonymous_codons(genetic_code)
    
    # hold the result as it is being calulated
    result = {}

    # calculate RSCU values
    for codon in genetic_code.keys():
        result[codon] = counts[codon] / ((len(synonymous_codons[codon]) ** -1) * (sum([counts[_codon] for _codon in synonymous_codons[codon]])))

    return result

def relative_adaptiveness(sequences=[], RSCUs={}, genetic_code=1):

    # ensure user gave only and only one input
    if sum([bool(sequences), bool(RSCUs)]) != 1:
        raise ValueError("Must provide either reference sequences or RSCU dictionary")

    # calculate the RSCUs if only given sequences
    if sequences:
        RSCUs = RSCU(sequences, genetic_code=genetic_code)

    # determine the synonymous codons for the genetic code
    synonymous_codons = _synonymous_codons(genetic_codes[genetic_code])

    # calculate the weights
    weights = {}
    for codon in RSCUs:
        weights[codon] = RSCUs[codon] / max([RSCUs[_codon] for _codon in synonymous_codons[codon]])

    return weights

def CAI(sequence, weights=[], RSCUs=[], sequences=[], genetic_code=1):
    """
    takes a DNA sequence and either the reference sequences, an RSCU dictionary, or
    a weights dictionary and returns the codon adaption index for the sequence
    """

    # validate user input
    if sum([bool(sequences), bool(RSCUs)], bool(weights)) != 1:
        raise ValueError("Must provide either reference sequences, or RSCU dictionary, or weights")

    # validate sequence
    if not sequence:
        raise ValueError("Sequence cannot be empty")

    # make sure input sequence can be divided into codons. If so, split into list of codons
    if len(sequence) % 3 != 0:
        raise ValueError("Input sequence not divisible by three")
    sequence = [sequence[i:i+3].upper() for i in range(0, len(sequence), 3)]

    # generate weights if not given
    if sequences:
        weights = relative_adaptiveness(sequences=sequences, genetic_code=genetic_code)
    elif RSCUs:
        weights = relative_adaptiveness(RSCUs=RSCUs, genetic_code=genetic_code)

    # determine the synonymous codons in the genetic code
    synonymous_codons = _synonymous_codons(genetic_codes[genetic_code])

    # find codons without synonyms
    non_synonymous_codons = [codon for codon in synonymous_codons.keys() if len(synonymous_codons[codon]) == 1]

    # create a list of the weights for the sequqence, not counting codons without synonyms (page 1285)
    try:
        sequence_weights = [weights[codon] for codon in sequence if codon not in non_synonymous_codons]
    except KeyError, e:
        raise KeyError("Bad weights dictionary passed: missing weight for codon " + str(e))

    # return the geometric mean of the weights raised to one over the length of the sequence
    try: 
        return gmean(sequence_weights) ** ((len(sequence_weights)) ** -1)
    except ZeroDivisionError:
        raise ValueError("Sequence only contains codons without synonymous codons")