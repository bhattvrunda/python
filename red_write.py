import sys
infile=open(sys.argv[0],'r')
outfile=open(sys.argv[1],'w')
for line in infile:
    print(line,file=outfile,end='')
infile.close()
outfile.close()
