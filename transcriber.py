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
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	row = line.split('\t')
	newstring = row[1]
	for lat,cyr in table.items():
		#start here next time
		newstring = newstring.replace(lat,cyr)
	row[9]='CYR = ' + newstring
	print('\t'.join(row))



	# if there are not 10 cells, skip the line
	#if len(row) != 10:
	#	continue
	# the form is the value of the second cell
	#form = row[1]
	#
	#for z in form
	#	table[cyr]
	#	print('%d\t %s\t_\t_\t_\t_\t_\t_\t_\t_"IPA="%s'%(i+1, t))
