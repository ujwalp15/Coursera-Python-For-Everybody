## Assignment 5.2

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate 
# message and ignore the number

largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    
    # Handle extreme cases
    if num == "done" : break
    #print num  
    try:
        intg = int(num)        
    except:
        print "Invalid input"
        continue
        
    # Do the work
    if largest is None or intg > largest:
        largest = intg
    if smallest is None or intg < smallest:
        smallest = intg

print "Maximum is", largest
print "Minimum is", smallest