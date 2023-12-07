#re helps dealing with regular expressions
import re


#define the count function
def count_consonants_after_è(word):
	#use a regular expression to find the position of "è" in the word
	match = re.search('[è]', word, flags=re.IGNORECASE)

	if match:
		è_index = match.start()

		#count the following consonants until the next vowel or end of word
		consonants_count = 0
		for cons in word[è_index + 1:]:
			if cons.lower() not in 'aàâeéèêiïîoôöuüûùyAÀÂEÉÈÊIÏÎOÔÖUÜÛÙY-':
				consonants_count += 1
			else:
				break  #stop counting

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
			for match in re.finditer('[è]', word, flags=re.IGNORECASE):
				è_index = match.start()
				consonants_count = count_consonants_after_è(word[è_index:])
				is_final = 'F' if è_index + consonants_count == len(word) - 1 else 'N'

				output_line = f"{word}\t{consonants_count}\t{is_final}\n"
				output_lines.append(output_line)
	#write in output file
	with open(output_file, 'w', encoding='utf-8') as f:
		f.writelines(output_lines)

#process the file gravedata and give output file gravelist based on the functions above
process_file('gravedata.txt', 'gravelist.txt')

