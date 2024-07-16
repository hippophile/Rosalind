dna_string = input()

step00 = dna_string.replace("A", "#")
step01 = step00.replace("T", "A")
step02 = step01.replace("#", "T")

step03 = step02.replace("C", "#")
step04 = step03.replace("G", "C")
final_dna = step04.replace("#", "G")

rev_dna = final_dna[::-1]

print("\n")

print(rev_dna)