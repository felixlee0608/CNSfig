#! /usr/bin/env python
import sys
if len(sys.argv) < 2:
	print (f"python {sys.argv[0]} infa > outfile")
	sys.exit()
seq={}
with open(sys.argv[1],'r') as f:
	for line in f.readlines():
		if line.startswith('>'):
			seqName = line.replace('\n', '')
			seq[seqName]=[]
		else:
			seq[seqName].append(line.strip('\n'))

for k, v in seq.items():
	seq[k] = ''.join(v)
	leng = len(seq[k])
	k = k.replace('>','').split(' ')[0];
	len2 = "{:.2f}".format(leng/10**6); 
	print (f"{k}\t{leng}\t{len2}")	
