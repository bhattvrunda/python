import sys
myfile=open(sys.argv[0],'r+')
for line in myfile:
    modline=line.replace('mispelt','miispelt')
    curoff=myfile.tell()
    myfile.seek(curoff-len(line))
    print(modline,file=myfile,end='')
    myfile.close()
