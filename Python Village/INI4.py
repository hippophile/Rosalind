user_input = input("Give 2 numbers : ")

num1, num2 = user_input.split()

a = int(num1)
b = int(num2)

odd_sum = 0

if a % 2 == 1:
    for i in range(a, b+1 , 2):
        odd_sum += i
else:
    for i in range(a+1, b+1, 2):
        odd_sum += i

print(odd_sum)