import math
def getAllPrimes(maxn):
    global AllPrimes
    for n in range(3,maxn+1):
        if n % 2==0:
            continue
        for i in range(3,1+int(math.sqrt(n)),2):
            if n%i==0:
                break
            else:
                AllPrimes.append(n)
AllPrimes=[]
getAllPrimes(100)
print(AllPrimes)
getAllPrimes(50)
print(AllPrimes)
