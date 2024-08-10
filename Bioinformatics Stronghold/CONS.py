from collections import defaultdict, Counter

# Οι ακολουθίες DNA
data = """ """


# Διαχωρισμός των γραμμών
lines = data.splitlines()

# Δημιουργία λεξικού για να αποθηκεύσουμε τις ακολουθίες
sequences = defaultdict(str)

# Διάσχιση των γραμμών και προσθήκη των ακολουθιών στο λεξικό
current_key = None
for line in lines:
    if line.startswith(">"):
        current_key = line
    else:
        sequences[current_key] += line

# Μήκος των ακολουθιών
length = len(next(iter(sequences.values())))

# Αρχικοποίηση της συμβολοσειράς συναίνεσης και του πίνακα προφίλ
consensus = ""
profile = {'A': [0] * length, 'C': [0] * length, 'G': [0] * length, 'T': [0] * length}

# Διασχίζουμε κάθε στήλη του πίνακα
for i in range(length):
    # Παίρνουμε όλα τα στοιχεία της i-στης στήλης
    column = [seq[i] for seq in sequences.values()]
    
    # Υπολογίζουμε το πιο συχνό στοιχείο στη στήλη
    most_common = Counter(column).most_common(1)[0][0]
    
    # Προσθέτουμε το πιο συχνό στοιχείο στη συμβολοσειρά συναίνεσης
    consensus += most_common
    
    # Ενημερώνουμε τον πίνακα προφίλ
    for nucleotide in profile.keys():
        profile[nucleotide][i] = column.count(nucleotide)

# Εκτύπωση της συμβολοσειράς συναίνεσης
print("Consensus string:", consensus)

# Εκτύπωση του πίνακα προφίλ
for nucleotide in "ACGT":
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")
