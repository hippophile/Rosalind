input_string = input()

input_numbers = input()


num1, num2, num3, num4 = input_numbers.split()
num1 = int(num1)
num2 = int(num2) + 1 
num3 = int(num3)
num4 = int(num4) + 1 

part1 = input_string[num1:num2]
part2 = input_string[num3:num4]

result = part1 + " " + part2

print(result)
