input_file = "data.txt"
output_file = "gravedata.txt"

with open("data.txt", 'r', encoding='utf-8') as input_file, open("gravedata.txt", 'w', encoding='utf-8') as output_file:
    lines_grave = [line for line in input_file if "è" in line]
    output_file.writelines(lines_grave)


