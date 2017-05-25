#Fergus Farrell
#Etude 9 - Harmonious Numbers

import math


def calculation(num):
    divisor = int(math.sqrt(num))
    total = 0
    for i in range(2, divisor + 1):
        if num % i == 0:
            secondNum = num / i
            if secondNum != i:
                total = total + secondNum
            total = total + i
    return total


Numbers = {}
Maximum = 2000000

for i in range(2, Maximum):
    numOne = calculation(i)
    numTwo = calculation(numOne)

    if Numbers.get(numOne) == None:
        if numOne != i and numTwo == i:
            if numOne < numTwo:
                Numbers[numOne] = numTwo
                print numOne, numTwo
            else:
                Numbers[numTwo] = numOne
                print numTwo, numOne