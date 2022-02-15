# Task to do
## Minimum Edit Distance
The minimum edit distance between two strings is defined as the minimum number of editing operations
- Insertion
- Deletion
- Substitution

The cost for these operations are:
- Insertion : 1
- Deletion : 1
- Substitution : 2

**Sample input:** 
```
Enter Actual word: DAUD      
Enter word to transform: SAUD
```
**Sample output:** 
```
D  4  5  4  3  2 
U  3  4  3  2  3
A  2  3  2  3  4
D  1  2  3  4  3
#  0  1  2  3  4
   #  S  A  U  D
```
*Here 2 in the top right corner of the matrix is the minimum edit distance.*

---