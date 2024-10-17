def findFactors(n):
    factors=[]
    for f in range(1,n):
        if n%f==0:
            factors.append(f)
    return factors
