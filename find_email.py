import re

text="My department email id is rupesh@cse.iitm.ac.in.This is what I use for all the official purpose.During phd i used rupesh)something@gmail.com,when gmail was not around rupesh_something@usa.net
regex=r'\w+@\w+'
email=re.findall(regex,text.lower())
print(email)
