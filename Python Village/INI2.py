user_input = input("Give 2 numbers : ")

num1, num2 = user_input.split()

num1 = int(num1)
num2 = int(num2)

def square_hypotenuse(a,b):
    c = (a*a) + (b*b)
    print(c)

square_hypotenuse(num1, num2)