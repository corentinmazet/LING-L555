#read cyrillicCODE.txt
fd = open('cyrillic.tsv', 'r')

import sys

#Create table
table = {}

for line in fd.readlines():
	if line.strip() == '':
		continue
	(lat,cyr)=line.strip().split('\t')
	table[lat]=cyr

#Replace last column
# for each of the lines of input
for line in sys.stdin.readlines(): 
	# strip any excess newlines
	line = line.strip('\n')
	# sent_ID
	if '# sent_ID' in line:
		print()
		print(line)
	if '# text' in line:
		print(line)
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	row = line.split('\t')
	newstring = row[1]
	for lat,cyr in table.items():
		newstring = newstring.replace(lat,cyr)
	row[9]='CYR =' + newstring
	print('\t'.join(row))
