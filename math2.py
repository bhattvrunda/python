import math
def isPrime(n):
    if n%2==0:
        print("composite")
    return
    for i in range(3,1+int(math.sqrt(n)),2):
        if n%i==0:
            print("composite")
            break
        else:
            print("Prime")

for n in range(3,100+1):
    print(n,'',end='')
    isPrime(n)
