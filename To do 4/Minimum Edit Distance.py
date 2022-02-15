# Calculating Minimum edit distance of a word.
def print_2d(record):
    '''
    For printing 2-D List.
    ```
    Input: 2-D List
    ```
    '''
    for i in record:
        for j in i:
            print(f' {j}', end=' ')
        print()

word1 = input('Enter Actual word: ')
word2 = input('Enter word to transform: ')
l1 = len(word1) + 2
l2 = len(word2) + 2
record = []
# Creating and initializing new Lists of given input size
for i in range(l1):
    record.append([])
    for j in range(l2):
       record[i].append(0)

r_word1 = word1[::-1]           # it is to inverse the string

record[-2][0] = '#'; record[-1][1] = '#'; record[-1][0] = ' '

# This loop is printing word in most left vertical column
for i in range(len(r_word1)):
    record[i][0] = r_word1[i]

# This loop is printing word in most lower vertical column
for i in range(len(word2)):
    record[-1][i+2] = word2[i]

# Here we're printing counting in second column in reverse order
j = 0
for i in range(l1-2,-1,-1):
    record[j][1] = i
    j += 1
# Here we're printing counting in second last row in order
for i in range(l2-1):
    record[-2][i+1] = i

for i in range(l1-3,-1,-1):
    for j in range(2, l2):
        # print(i, j, end='\t')
        diag = int(record[i+1][j-1])
        left = int(record[i+1][j])
        down = int(record[i][j-1])
        if record[i][0] != record[-1][j]:
            diag += 2
        d = min(diag, left + 1, down + 1)
        record[i][j] = d

print_2d(record)