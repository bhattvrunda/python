import math
for n in range(3,100+1):
    print(n,'',end='')
    if n%2==0:
        print("composite")
        continue
    for i in range (3,1+int(math.sqrt(n)),2):
        if n%i==0:
            print("composite")
            break
        else:
            print("prime")
