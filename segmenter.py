import sys

for s in sys.stdin.readlines():
	s_replace = s.replace('. ', '.\n')
	print(s_replace)
