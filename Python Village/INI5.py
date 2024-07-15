with open("Dataset.txt", "r") as file:
    lines = file.readlines()

for index in range(1, len(lines), 2):
    print(lines[index].strip())
