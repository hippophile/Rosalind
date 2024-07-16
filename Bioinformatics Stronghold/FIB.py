user_input = input(" ")

num1, num2 = user_input.split()

months = int(num1)
k = int(num2)

def Rabbits(months, k):
    if months == 1:
        return 1
    elif months == 2:
        return 1
    
    prod_pairs = 1
    new_borns = 1

    for i in range(3, months + 1):
        current = new_borns + (prod_pairs * k)

        prod_pairs = new_borns

        new_borns = current

    return new_borns
    
result = Rabbits(months, k)
print(result)