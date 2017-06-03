## Assignment 10.2

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
path = 'E:/Coursera/Python-for-Everybody-Coursera/Python Data Structures/'
filename = path + name
handle = open(name)

email_d = dict()

# constructing dictionary with value
for line in handle:
    if not line.startswith("From "): continue
    line_split = line.split()[5].split(':')
    email_d[line_split[0]] = email_d.get(line_split[0],0) + 1

# Constructing final list for output
lst = list()

for key,val in email_d.items():
    lst.append( (key, val) )

lst.sort()

# Printing ordered keys
for key, val in lst:
    print key, val
