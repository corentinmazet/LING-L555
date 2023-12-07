from collections import defaultdict


#read file
with open('gravelist.txt', 'r', encoding='utf-8') as file:
	lines = file.readlines()

#convert lines to lowercase and then remove repeated lines
unique_lines = list(set(line.lower() for line in lines))

#create dictionary for frequency
frequency_dict = defaultdict(int)

#iterate through unique lines and count frequencies of each unique combination
for line in unique_lines:
	columns = line.strip().split('\t')
	if len(columns) == 3:
		key = f'{columns[1]} consonant(s) in {columns[2]} context'
		frequency_dict[key] += 1


#write the frequency list to file
with open('gravefrequency.txt', 'w', encoding='utf-8') as output_file:
	for key, value in frequency_dict.items():
		output_file.write(f'{key}: {value} instances\n')

