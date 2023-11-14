import sys

counter_lines = 0
counter_token = 1
counter_character = 0
counter_consonants = 0
counter_vowels = 0

for c in sys.stdin.read():
	if c == '\n':
		counter_lines = counter_lines + 1
	if c == ' ':
		counter_token = counter_token + 1
	counter_character = counter_character + 1
	if c in 'zrtypqsdfghjklmwxcvbnZRTYPQSDFGHJKLMWXCVBN':
		counter_consonants = counter_consonants + 1
	if c in 'aeiouAEIOUÀÈÌÒÙÁÉÍÓÚÜàèìòùáéíóúü':
		counter_vowels = counter_vowels + 1

print(counter_lines)
print(counter_token)
print(counter_character)
print(counter_consonants)
print(counter_vowels)
print(counter_vowels/counter_token)
