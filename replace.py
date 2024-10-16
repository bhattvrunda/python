import sys
myfile=open(sys.argv[1],'r+')
for line in myfile:
    modline=line.replace('misplet','misspelt')
    print(modline,file=myfile,end='')
myfile.close()
