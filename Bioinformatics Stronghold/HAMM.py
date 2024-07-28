# Prompt the user for two different inputs
data1 = input("1st: ")
data2 = input("2nd: ")

# Initialize two empty dictionaries
dict1 = {}
dict2 = {}

# Define keys for each input
key1 = "seq1"
key2 = "seq2"

# Add the inputs to the dictionaries using the defined keys
dict1[key1] = data1
dict2[key2] = data2

ham = 0 

for base1, base2 in zip(data1, data2):
        if base1 != base2:
            ham += 1

# Print the dictionaries to verify the entries
# print("Dictionary 1:", dict1)
# print("Dictionary 2:", dict2)
print("The Hamming distance is : ", ham)