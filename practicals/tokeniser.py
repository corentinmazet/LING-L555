import sys

counter = 0

for ln in sys.stdin.readlines():
	if ln.strip () == '':
		continue
	counter = counter + 1
	#ln = ln.strip()
	print('# sent_ID =', counter)
	print('# text =', ln, end="\n")
	punctuationleft = ['\u2019']
	punctuationboth = ['.', '"', ';', ',', '?', '!', ':', '(', ')', '...']
	inp = ln
	for p in punctuationleft:
		inp = inp.replace(p, ''+p+' ')
	for p in punctuationboth:
		inp = inp.replace(p, ' '+p+' ')
	s = inp.split(' ')
	for i, t in enumerate(s):
		if t.strip () == '':
			continue
		print('%d\t %s\t_\t_\t_\t_\t_\t_\t_\t_'%(i+1, t))

	print()
