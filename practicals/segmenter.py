from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

import sys

for s in sys.stdin.readlines():
	s_replace = s.replace('. ', '.\n')
	l = s_replace.splitlines()
	for ln in l:
		if ln.strip()=='':
			continue
		print(ln)
