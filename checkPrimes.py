import math

lower = 900
upper = 1000

def isPrime(number):
    if number < 2:
        return false
    castedSqrtOfPrime = int(math.sqrt(number))
    for i in range(2, castedSqrtOfPrime + 1):
        if number % i == 0:
            return false
    return true