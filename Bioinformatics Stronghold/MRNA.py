ex_protein = input() 

codon_table = {
    'F': 2, 'L': 6, 'I': 3, 'V': 4,
    'M': 1, 'S': 6, 'P': 4, 'T': 4,
    'A': 4, 'Y': 2, 'H': 2, 'N': 2,
    'D': 2, 'Q': 2, 'K': 2, 'E': 2,
    'C': 2, 'R': 6, 'G': 4, 'W': 1,
    'Stop': 3
}

def final_rnas(protein):
    total_mrnas = 1
    for amino_acids in protein:
        total_mrnas *= codon_table[amino_acids]
        total_mrnas %= 1000000
    total_mrnas *= codon_table['Stop']
    total_mrnas %= 1000000
    return total_mrnas

print(final_rnas(ex_protein))