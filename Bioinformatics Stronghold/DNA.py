input_string = input()

letter_count = {}

for letter in input_string :

    if letter in letter_count :
        letter_count[letter] += 1

    else :
        letter_count[letter] = 1

for letter, count in letter_count.items():
    print(f"{letter} {count}")