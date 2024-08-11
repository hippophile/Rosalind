import numpy as np 

user_input = input()

num1, num2 = user_input.split()

n = int(num1)
m = int(num2)

def Rabbits(n, m):
    pop = np.zeros([n + 1, m], dtype =np.int64)
    pop[1][0] = 1

    for month in range(2, pop.shape[0]):
        for age in range(0, pop.shape[1]):
            if age == 0:
                pop[month][age] = np.sum(pop[month - 1, 1:])
            else:
                pop[month][age] = pop[month - 1][age - 1]
            

    return np.sum(pop[n])

result = Rabbits(n, m)
print(result)
