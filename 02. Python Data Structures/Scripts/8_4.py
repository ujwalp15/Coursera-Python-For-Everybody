## Assignment 8.4

# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

fname = raw_input("Enter file name: ")
path = 'E:/Coursera/Python-for-Everybody-Coursera/Python Data Structures/'
filename = path + fname

try:
    fh = open(fname)
except:
    print 'The following file doesn''t exist:',fname
    exit()

lst = list()
for line in fh:
    newline = line.split()
    m = len(newline)
    len_range = range(m)
    for i in len_range:
        value = newline[i]
        if value not in lst:
        	lst.append(value)
lst.sort()
print lst