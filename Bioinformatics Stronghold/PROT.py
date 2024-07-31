# rna_to_protein.py

# Import the Seq class from the Bio.Seq module in the Biopython library
from Bio.Seq import Seq

def translate_rna_to_protein(rna_sequence):
    """
    Translates an RNA sequence into a protein sequence.
    
    Args:
        rna_sequence (str): A string representing the RNA sequence.
    
    Returns:
        str: The translated protein sequence.
    """
    # Create an RNA sequence object using the input string
    rna_seq = Seq(rna_sequence)
    
    # Translate the RNA sequence to a protein sequence.
    # The 'to_stop=True' parameter ensures translation stops at the first stop codon.
    protein_seq = rna_seq.translate(to_stop=True)
    
    # Convert the protein sequence object to a string and return it
    return str(protein_seq)

if __name__ == "__main__":
    """
    The main block of the script.
    This block only executes when the script is run directly, not when imported as a module.
    """
    # Define a sample RNA sequence for testing
    sample_rna = "AUGCCUCCCGCAGAAU"
    
    # Call the function to translate the RNA sequence to a protein sequence
    protein_string = translate_rna_to_protein(sample_rna)
    
    # Print the resulting protein sequence
    print(protein_string)
