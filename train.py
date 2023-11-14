#Open conllu file
fd = open('wiki.conllu', 'r')

m={}
n={}

print('#P\tcount\ttag\tform')

for line in fd.readlines():
	if '\t' not in line:
		continue
	row = line.split()
	form = row[1]
	tag = row[3]
	if form not in m:
		m[form]={}
	if tag not in m[form]:
		m[form][tag]=0
	m[form][tag] += 1

	if tag not in n:
		n[tag]=0
	n[tag] += 1

totaln = 0

for tag in n:
	totaln += n[tag]

for tag in n:
	proban = n[tag]/totaln
	print('%.2f\t%s\t%s\t%s'%(proban, n[tag], tag, '_'))

for form in m:
	totalm = 0
	for tag in m[form]:
		totalm += m[form][tag]
	for tag in m[form]:
		probam = m[form][tag]/totalm
		print('%.2f\t%s\t%s\t%s'%(probam, totalm, tag, form)) 


#print ('%s\t%s\t%s\t%s\ts‰'(proba, COUNT, TAG, FORM))


