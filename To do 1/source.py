import  codecs
tokens = dict()
f = codecs.open('text.txt','r','UTF-8')
# print(f.read())         # reading all file content
for x in f:
    lst = x.split(' ')
    for t in lst:
        if t not in tokens:
            tokens[t] = 1
        else:
            tokens[t] += 1
f.close()
f = codecs.open('Result.txt', 'w', 'UTF-8')
f.write('Count\t\tWords\n')
for x, y in tokens.items():
    f.write(str(y))
    f.write('\t\t')
    f.write(x)
    f.write('\n')