input_file = "data.txt"
output_file = "aigudata.txt"

with open("data.txt", 'r', encoding='utf-8') as input_file, open("aigudata.txt", 'w', encoding='utf-8') as output_file:
    lines_aigu = [line for line in input_file if "é" in line]
    output_file.writelines(lines_aigu)

