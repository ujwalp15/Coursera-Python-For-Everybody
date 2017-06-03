## Assignment 4.6

# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)

def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + (r * 1.5 * (h - 40))

h = float(raw_input("Enter Hours:"))
r = float(raw_input("Enter Rate:"))
p = computepay(h,r)
print p