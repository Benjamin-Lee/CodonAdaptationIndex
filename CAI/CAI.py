from itertools import chain
import Bio.Data.CodonTable as ct
from scipy.stats import gmean
from collections import Counter

# get rid of Biopython warning
import warnings
from Bio import BiopythonWarning

warnings.simplefilter("ignore", BiopythonWarning)


def _synonymous_codons(genetic_code_dict):

    # invert the genetic code dictionary to map each amino acid to its codons
    codons_for_amino_acid = {}
    for codon, amino_acid in genetic_code_dict.items():
        codons_for_amino_acid[amino_acid] = codons_for_amino_acid.get(amino_acid, [])
        codons_for_amino_acid[amino_acid].append(codon)

    # create dictionary of synonymous codons
    # Example: {'CTT': ['CTT', 'CTG', 'CTA', 'CTC', 'TTA', 'TTG'], 'ATG': ['ATG']...}
    return {
        codon: codons_for_amino_acid[genetic_code_dict[codon]]
        for codon in genetic_code_dict.keys()
    }


_synonymous_codons = {
    k: _synonymous_codons(v.forward_table) for k, v in ct.unambiguous_dna_by_id.items()
}
_non_synonymous_codons = {
    k: {codon for codon in v.keys() if len(v[codon]) == 1}
    for k, v in _synonymous_codons.items()
}


def RSCU(sequences, genetic_code=11):
    r"""Calculates the relative synonymous codon usage (RSCU) for a set of sequences.

    RSCU is 'the observed frequency of [a] codon divided by the frequency
    expected under the assumption of equal usage of the synonymous codons for an
    amino acid' (page 1283).

    In math terms, it is

    .. math::

        \frac{X_{ij}}{\frac{1}{n_i}\sum_{j=1}^{n_i}x_{ij}}

    "where :math:`X` is the number of occurrences of the :math:`j` th codon for
    the :math:`i` th amino acid, and :math:`n` is the number (from one to six)
    of alternative codons for the :math:`i` th amino acid" (page 1283).

    Args:
        sequences (list): The reference set of sequences.
        genetic_code (int, optional): The translation table to use. Defaults to 11, the standard genetic code.

    Returns:
        dict: The relative synonymous codon usage.

    Raises:
        ValueError: When an invalid sequence is provided or a list is not provided.
    """

    if not isinstance(sequences, (list, tuple)):
        raise ValueError(
            "Be sure to pass a list of sequences, not a single sequence. "
            "To find the RSCU of a single sequence, pass it as a one element list."
        )

    # ensure all input sequences are divisible by three
    for sequence in sequences:
        if len(sequence) % 3 != 0:
            raise ValueError("Input sequence not divisible by three")
        if not sequence:
            raise ValueError("Input sequence cannot be empty")

    # count the number of each codon in the sequences
    sequences = (
        (sequence[i : i + 3].upper() for i in range(0, len(sequence), 3))
        for sequence in sequences
    )
    codons = chain.from_iterable(
        sequences
    )  # flat list of all codons (to be used for counting)
    counts = Counter(codons)

    # "if a certain codon is never used in the reference set... assign [its
    # count] a value of 0.5" (page 1285)
    for codon in ct.unambiguous_dna_by_id[genetic_code].forward_table:
        if counts[codon] == 0:
            counts[codon] = 0.5

    # determine the synonymous codons for the genetic code
    synonymous_codons = _synonymous_codons[genetic_code]

    # hold the result as it is being calulated
    result = {}

    # calculate RSCU values
    for codon in ct.unambiguous_dna_by_id[genetic_code].forward_table:
        result[codon] = counts[codon] / (
            (len(synonymous_codons[codon]) ** -1)
            * (sum((counts[_codon] for _codon in synonymous_codons[codon])))
        )

    return result


def relative_adaptiveness(sequences=None, RSCUs=None, genetic_code=11):
    r"""Calculates the relative adaptiveness/weight of codons.

    The relative adaptiveness is "the frequency of use of that codon compared to
    the frequency of the optimal codon for that amino acid" (page 1283).

    In math terms, :math:`w_{ij}`, the weight for the :math:`j` th codon for
    the :math:`i` th amino acid is

    .. math::

        w_{ij} = \frac{\text{RSCU}_{ij}}{\text{RSCU}_{imax}}

    where ":math:`\text{RSCU}_{imax}` [is] the RSCU... for the frequently used
    codon for the :math:`i` th amino acid" (page 1283).

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
        raise TypeError("Must provide either reference sequences or RSCU dictionary")

    # calculate the RSCUs if only given sequences
    if sequences:
        RSCUs = RSCU(sequences, genetic_code=genetic_code)

    # determine the synonymous codons for the genetic code
    synonymous_codons = _synonymous_codons[genetic_code]

    # calculate the weights
    weights = {}
    for codon in RSCUs:
        weights[codon] = RSCUs[codon] / max(
            (RSCUs[_codon] for _codon in synonymous_codons[codon])
        )

    return weights


def CAI(sequence, weights=None, RSCUs=None, reference=None, genetic_code=11):
    r"""Calculates the codon adaptation index (CAI) of a DNA sequence.


    CAI is "the geometric mean of the RSCU values... corresponding to each of the
    codons used in that gene, divided by the maximum possible CAI for a gene of
    the same amino acid composition" (page 1285).

    In math terms, it is

    .. math::

        \left(\prod_{k=1}^Lw_k\right)^{\frac{1}{L}}

    where :math:`w_k` is the relative adaptiveness of the :math:`k` th codon in
    the gene (page 1286).

    Args:
        sequence (str): The DNA sequence to calculate the CAI for.
        weights (dict, optional): The relative adaptiveness of the codons in the reference set.
        RSCUs (dict, optional): The RSCU of the reference set.
        reference (list): The reference set of sequences.

    Note:
        One of ``weights``, ``reference`` or ``RSCUs`` is required.

    Returns:
        float: The CAI of the sequence.

    Raises:
        TypeError: When anything other than one of either reference sequences, or RSCU dictionary, or weights is provided.
        ValueError: See :func:`RSCU` for details.
        KeyError: When there is a missing weight for a codon.

    Warning:
        Will return nan if the sequence only has codons without synonyms.
    """

    # validate user input
    if sum([bool(reference), bool(RSCUs)], bool(weights)) != 1:
        raise TypeError(
            "Must provide either reference sequences, or RSCU dictionary, or weights"
        )

    # validate sequence
    if not sequence:
        raise ValueError("Sequence cannot be empty")

    # make sure input sequence can be divided into codons. If so, split into list of codons
    if len(sequence) % 3 != 0:
        raise ValueError("Input sequence not divisible by three")
    sequence = sequence.upper()
    sequence = [sequence[i : i + 3] for i in range(0, len(sequence), 3)]

    # generate weights if not given
    if reference:
        weights = relative_adaptiveness(sequences=reference, genetic_code=genetic_code)
    elif RSCUs:
        weights = relative_adaptiveness(RSCUs=RSCUs, genetic_code=genetic_code)

    # create a list of the weights for the sequence, not counting codons without
    # synonyms -> "Also, the number of AUG and UGG codons are
    # subtracted from L, since the RSCU values for AUG and UGG are both fixed at
    # 1.0, and so do not contribute to the CAI." (page 1285)
    sequence_weights = []
    for codon in sequence:
        if codon not in _non_synonymous_codons[genetic_code]:
            try:
                sequence_weights.append(weights[codon])
            except KeyError:
                # ignore stop codons
                if codon in ct.unambiguous_dna_by_id[genetic_code].stop_codons:
                    pass
                else:
                    raise KeyError(
                        "Bad weights dictionary passed: missing weight for codon "
                        + str(codon)
                        + "."
                    )

    # return the geometric mean of the weights raised to one over the length of the sequence
    return float(gmean(sequence_weights))
