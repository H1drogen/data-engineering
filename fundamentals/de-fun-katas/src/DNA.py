
def dna_pair(dna_string):
    dna_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    answer = []
    for base in dna_string:
        answer.append([base, dna_pairs[base]])
    return answer