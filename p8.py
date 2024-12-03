import sys
myfile=open(sys.argv[1],"r") 
data=myfile.read()
print(data)
file=open(sys.argv[2],"w+")

file.write(data+"New data enter into file")


file.seek(0)

newdata=file.read()
print("\n")
print("new file data read")
print("\n")
print(newdata)

file.close()
myfile.close()