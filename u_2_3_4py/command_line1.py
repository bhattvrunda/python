import sys
myfile=open(sys.argv[0])
for line in myfile:
    print(line,end='')
myfile.close()
