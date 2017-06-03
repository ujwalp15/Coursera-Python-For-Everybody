## Assignment 9.4

# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email_d = dict()

for line in handle:
    if not line.startswith("From "): continue
    line_split = line.split()
    email_d[line_split[1]] = email_d.get(line_split[1],0) + 1

maxcount = None
maxemail = None

for email,count in email_d.items():
    if maxcount is None or count > maxcount:
        maxemail = email
        maxcount = count
print maxemail, maxcount
