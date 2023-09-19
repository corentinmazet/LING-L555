import sys

punctuation = ['.', '"', ';', ',', '?', '!', ':', '(', ')', '...', '\n']

for s in sys.stdin.readlines():
	inp = s
	for p in punctuation:
		inp = inp.replace(p, ' '+p+' ')
	replace_space = inp.replace(' ', '\n')
	print(replace_space)


