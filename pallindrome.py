def isPallindrome(bstring):
    blen=len(bstring)
    first=bstring[:blen//2]
    second=bstring[(blen+1)//2:]
    if first==second[::-1]:
        return True
    return False
first="0"
second="01"
i=0
while i<10:
    if i>=2 and isPalindrome(first[:-2]):
        print(first[:-2]+"is a palindrome")
    first,second=second,second+first
    i=i+1
    
