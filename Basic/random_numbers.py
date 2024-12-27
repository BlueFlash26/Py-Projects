'''
from random import randint

def random_numbers(initail: int, final: int):
    randomNumbers = []

    while len(randomNumbers) < 10:
        randomNumber = randint(initail, final)
        if randomNumber not in randomNumbers:
            randomNumbers.append(randomNumber)
        else:
            continue
    
    for number in randomNumbers:
        print(number, end=" ")
    print(*randomNumbers)

random_numbers(1, 100)
'''

import numpy as np

randomNumbers = np.random.randint(1, 100, 10)
print(*randomNumbers) 