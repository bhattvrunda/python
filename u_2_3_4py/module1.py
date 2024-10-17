import math
def isPrime(n):
    if n%2==0:
        return False
    for i in range(3,1+int(math.sqrt(n)),2):
        if n%i==0:
            return False
    else:
        return True
for n in range(3,100+1):
    if isPrime(n):print(n,end=',')
print()
