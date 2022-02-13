# Calculating Minimum edit distance of a word.
def print_2d(record):
    for i in record:
        for j in i:
            print(j, end=' ')
        print()

word1 = input('Enter Actual word: ')
word2 = input('Enter word to transform: ')
l1 = len(word1) + 2
l2 = len(word2) + 2
record = []
for i in range(l1):
    record.append([])
    for j in range(l2):
       record[i].append(0)
r_word1 = word1[::-1]           # it is to inverse the string
for i in range(len(r_word1)):
    record[i][0] = r_word1[i]

for i in range(len(word2)):
    record[-1][i+2] = word2[i]

record[-2][0] = '#'; record[-1][1] = '#'; record[-1][0] = ' '

for i in range(0,l1-2):
    record[i][1] = i

print_2d(record)