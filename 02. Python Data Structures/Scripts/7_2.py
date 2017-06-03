## Assignment 7.2

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and 
# produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# when you are testing enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
path = 'E:/Coursera/Python-for-Everybody-Coursera/Python Data Structures/'
filename = path + fname

try:
    fh = open(fname)
except:
    print 'The following file doesn''t exist:',fname
    exit()

total = 0
count = 0    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    m = len(line)
    pos = line.find(':')
    num = float(line[pos+1:m])
    total = total + num
    count = count + 1
print 'Average spam confidence:', total / count