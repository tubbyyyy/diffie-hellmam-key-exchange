from checkPrimes import Prime

***OPEN WORLD***
primeNumber = Prime().generatePrime(100000, 1000000) #prime number is generated
generateNumber = Prime().generatePrimitiveRoots(primeNumber) #a primitive root based on that prime number is selected

***Alice***
secretKeyAlice = random.randint(0, 1000000)
A = pow(generateNumber, secretKeyAlice) % primeNumber #using the public varibles & alices' key, another key is generated
#B is recieved by Alice from Bob
finalKeyAlice = pow(B, secretKeyAlice) % primeNumber
#final calulation is achieved using data exchange and secret key to achieve identical cipher

***Bob***
secretKeyBob = random.randint(0, 1000000)
B = pow(generateNumber, secretKeyBob) % primeNumber #using the public varibles & bobs' key, another key is generated
#A is recieved by Bob from Alice
finalKeyBob = pow(A, secretKeyBob) % primeNumber
#final calulation is achieved using data exchange and secret key to achieve identical cipher

(finalKeyAlice == finalKeyBob) is True
#(generateNumber^secreyKeys % primeNumber) is calculated such that neither secretKeyAlice or secretKeyBob can be retrieved by pulling apart A or B
#to do so would take up (10^really big) time