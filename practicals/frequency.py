import sys

vocab = {} # dict to store frequency list

# for each of the lines of input
for line in sys.stdin.readlines(): 
    # strip any excess newlines
    line = line.strip('\n')
    # if there is no tab character, skip the line
    if '\t' not in line:
        continue
    # make a list of the cells in the row
    row = line.split('\t')
    # if there are not 10 cells, skip the line
    if len(row) != 10:
        continue
    # the form is the value of the second cell
    form = row[1]
    # if we haven't seen it yet, set the frequency count to 0
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1

# print out the frequency list
for w in vocab:
    print('%d\t%s' % (vocab[w], w))

# Define a new list called freq, for frequency
freq = []

# For each of the words in the vocabulary variable
for w in vocab:
    # Add a pair of (frequency, word) to the frequency list
    freq.append((vocab[w], w))
# Reverse sort the list, i.e. in descending order of frequency
freq.sort(reverse=True)

# Print out the first 4 elements from the list
#print(freq[0:4])

# Open the file freq.txt in write mode
fd = open('freq.txt', 'w')
# For each of the items in the frequency list 
for (f, w) in freq:
    # Write out the frequency and the word to the file
    # separated by the tab character
    fd.write('%d\t%s\n' % (f, w))
# Close the file
fd.close()  
