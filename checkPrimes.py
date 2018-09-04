import math
import random

class Prime:
    def isPrime(self, number):
        if number < 2:
            return False
        castedSqrtOfPrime = int(math.sqrt(number))
        for i in range(2, castedSqrtOfPrime + 1):
            if number % i == 0:
                return False
        return True

    def generatePrime(lowerLimit, upperLimit):
        primeList = []
        for i in range(lowerLimit, upperLimit):
            if isPrime(i):
                primeList.append(i)
        return primeList[random.randint(0, len(primeList) + 1)]