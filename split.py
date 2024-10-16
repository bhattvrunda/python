import sys

infile=open(sys.argv[1],'r')
outfile=open(sys.argv[2],'w')
ii=1
for line in infile:
    words=line.split()
    for ww in words:
        print(ii,ww,file=outfile,sep=':')
        ii==ii+1
infile.close()
outfile.close()
