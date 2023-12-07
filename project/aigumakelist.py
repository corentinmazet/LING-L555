#re helps dealing with regular expressions
import re


#define the count function
def count_consonants_after_é(word):
	#use a regular expression to find the position of "é" in the word
	match = re.search('[é]', word, flags=re.IGNORECASE)

	if match:
		é_index = match.start()

		#count the following consononants until the next vowel or end of word
		consonants_count = 0
		for cons in word[é_index + 1:]:
			if cons.lower() not in 'aàâeéèêiïîoôöuüûùyAÀÂEÉÈÊIÏÎOÔÖUÜÛÙY-':
				consonants_count += 1
			else:
				break  # Stop counting after the next vowel

		return consonants_count
	else:
		return None
 
#define the processing function
def process_file(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as f:
		lines = f.readlines()

	#remove lines that start w #
	lines = [line for line in lines if not line.startswith('#')]

	output_lines = []
	
	
	#reformat
	for line in lines:
		columns = line.strip().split('\t')
		if len(columns) >= 2:
			word = columns[1]

			#final or non-final
			for match in re.finditer('[é]', word, flags=re.IGNORECASE):
				é_index = match.start()
				consonants_count = count_consonants_after_é(word[é_index:])
				is_final = 'F' if é_index + consonants_count == len(word) - 1 else 'N'

				output_line = f"{word}\t{consonants_count}\t{is_final}\n"
				output_lines.append(output_line)
	#write in output file
	with open(output_file, 'w', encoding='utf-8') as f:
		f.writelines(output_lines)

#process the file aigudata and output aigulist based on the functions above
process_file('aigudata.txt', 'aigulist.txt')

