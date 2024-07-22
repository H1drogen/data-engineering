from src.DNA import dna_pair


def test_dna_works_with_empty_string():
    assert dna_pair('') == []

def test_dna_works_with_single_string():
    assert dna_pair('A') == [['A', 'T']]

def test_dna_works_with_multiple_string():
    assert dna_pair('ATCG') == [['A', 'T'], ['T', 'A'], ['C', 'G'], ['G', 'C']]