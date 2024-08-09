# Get DNA sequences from input
dna_s = input("Enter DNA sequence s: ")
dna_t = input("Enter DNA sequence t: ")

# Store DNA sequences in dictionaries (if needed)
dict1 = {}
dict2 = {}

key1 = "dna_s"
key2 = "dna_t"

dict1[key1] = dna_s
dict2[key2] = dna_t

# Calculate the lengths of the DNA sequences
length_s = len(dna_s)
length_t = len(dna_t)

# Function to find all positions of dna_t in dna_s
def find_all_positions(dna_s, dna_t):
    positions = []
    for i in range(length_s - length_t + 1):  # Adjusted range to correctly slice the substring
        if dna_s[i:i+length_t] == dna_t:  # Corrected slicing to compare with dna_t
            positions.append(i + 1)  # Append 1-based index
    return positions

# Find and print all positions
positions = find_all_positions(dna_s, dna_t)
if positions:
    print(" ".join(map(str, positions)))
else:
    print("dna_t is not a substring of dna_s")
