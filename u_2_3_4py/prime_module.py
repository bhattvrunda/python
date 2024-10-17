import prime_module
for n in range(3,50+1):
    if prime_module.isPrime(n):print(n,end=',')
print()
myprime=prime_module.isPrime
if myprime(22):
    print(22)
else:
    print("22 is composite")
from prime_module import*
if isPrime(23):
    print(23)
else:
    print("23 is composite")
