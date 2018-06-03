from itertools import chain
import Bio.Data.CodonTable as ct
from genetic_codes import genetic_codes
from scipy.stats.mstats import gmean
from collections import Counter

def _synonymous_codons(genetic_code_dict):

    # invert the genetic code dictionary to map each amino acid to its codons
    codons_for_amino_acid = {}
    for codon, amino_acid in genetic_code_dict.items():
        codons_for_amino_acid[amino_acid] = codons_for_amino_acid.get(amino_acid, [])
        codons_for_amino_acid[amino_acid].append(codon)

    # create dictionary of synonmyous codons
    # Example: {'CTT': ['CTT', 'CTG', 'CTA', 'CTC', 'TTA', 'TTG'], 'ATG': ['ATG']...}
    return {codon : codons_for_amino_acid[genetic_code_dict[codon]] for codon in genetic_code_dict.keys()}


def RSCU(sequences, genetic_code=11):
    """Calculates the relative synonymous codon usage (RSCU) for a set of sequences.

    RSCU is 'the observed frequency of [a] codon divided by the frequency
    expected under the assumption of equal usage of the synonymous codons for an
    amino acid' (page 1283).

    Args:
        sequences (list): The reference set of sequences.
        genetic_code (int, optional): The translation table to use. Defaults to 11, the standard genetic code.

    Returns:
        dict: The relative synonymous codon usage.

    Raises:
        ValueError: When an invalid sequence is provided.
    """

    # convert genetic code ID to dictionary
    genetic_code = ct.unambiguous_dna_by_id[genetic_code].forward_table

    # ensure all input sequences are divisible by three
    for sequence in sequences:
        if len(sequence) % 3 != 0:
            raise ValueError("Input sequence not divisible by three")
        if len(sequence) == 0:
            raise ValueError("Input sequence cannot be empty")

    # count the number of each codon in the sequences
    sequences = ((sequence[i:i+3].upper() for i in range(0, len(sequence), 3)) for sequence in sequences)
    codons = chain.from_iterable(sequences) # flat list of all codons (to be used for counting)
    counts = Counter(codons)

    # "if a certain codon is never used in the reference set... assign [its
    # count] a value of 0.5" (page 1285)
    for codon in genetic_code:
        if counts[codon] == 0:
            counts[codon] = 0.5

    # determine the synonymous codons for the genetic code
    synonymous_codons = _synonymous_codons(genetic_code)

    # hold the result as it is being calulated
    result = {}

    # calculate RSCU values
    for codon in genetic_code.keys():
        result[codon] = counts[codon] / ((len(synonymous_codons[codon]) ** -1) * (sum((counts[_codon] for _codon in synonymous_codons[codon]))))

    return result

def relative_adaptiveness(sequences=[], RSCUs={}, genetic_code=11):
    """Calculates the relative adaptiveness/weight of codons.

    The relative adaptiveness is "the frequency of use of that codon compared to
    the frequency of the optimal codon for that amino acid" (page 1283).

    Args:
        sequences (list, optional): The reference set of sequences.
        RSCUs (dict, optional): The RSCU of the reference set.
        genentic_code (int, optional): The translation table to use. Defaults to 11, the standard genetic code.

    Note:
        Either ``sequences`` or ``RSCUs`` is required.

    Returns:
        dict: A mapping between each codon and its weight/relative adaptiveness.

    Raises:
        ValueError: When neither ``sequences`` nor ``RSCUs`` is provided.
        ValueError: See :func:`RSCU` for details.
    """

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
        weights[codon] = RSCUs[codon] / max((RSCUs[_codon] for _codon in synonymous_codons[codon]))

    return weights

def CAI(sequence, weights={}, RSCUs={}, sequences=[], genetic_code=11):
    """Calculates the codon adaptation index (CAI) of a DNA sequence.


    CAI "the geometric mean of the RSCU values... corresponding to each of the
    codons used in that gene, divided by the maximum possible CAI for a gene of
    the same amino acid composition" (page 1285).

    Args:
        sequence (str): The DNA sequence to calculate the CAI for.
        weights (dict, optional): The relative adaptiveness of the codons in the reference set.
        RSCUs (dict, optional): The RSCU of the reference set.
        sequences (list): The reference set of sequences.

    Note:
        One of ``weights``, ``sequences`` or ``RSCUs`` is required.

    Returns:
        float: The CAI of the sequence.

    Raises:
        ValueError: When anything other than one of either reference sequences, or RSCU dictionary, or weights is provided.
        ValueError: See :func:`relative_adaptiveness` for details.
        KeyError: When there is a missing weight for a codon.
        ValueError: When ``sequence`` only contains codons without synonymous codons
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

    # remove last codon if stop codon
    try:
        genetic_codes[genetic_code][sequence[-1]]
    except KeyError:
        sequence = sequence[:-1]

    # generate weights if not given
    if sequences:
        weights = relative_adaptiveness(sequences=sequences, genetic_code=genetic_code)
    elif RSCUs:
        weights = relative_adaptiveness(RSCUs=RSCUs, genetic_code=genetic_code)

    # determine the synonymous codons in the genetic code
    synonymous_codons = _synonymous_codons(genetic_codes[genetic_code])

    # find codons without synonyms
    non_synonymous_codons = [codon for codon in synonymous_codons.keys() if len(synonymous_codons[codon]) == 1]

    # create a list of the weights for the sequence, not counting codons without
    # synonyms -> "Also, the number of AUG and UGG codons are
    # subtracted from L, since the RSCU values for AUG and UGG are both fixed at
    # 1.0, and so do not contribute to the CAI." (page 1285)
    try:
        sequence_weights = [weights[codon] for codon in sequence if codon not in non_synonymous_codons]
    except KeyError:
        raise KeyError("Bad weights dictionary passed: missing weight for codon.")

    # return the geometric mean of the weights raised to one over the length of the sequence
    try:
        return gmean(sequence_weights) ** ((len(sequence_weights)) ** -1)
    except ZeroDivisionError:
        raise ValueError("Sequence only contains codons without synonymous codons")
