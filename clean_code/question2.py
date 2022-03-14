'''
Version 1: Using a CSV library is kind of cheating, so this is the raw input method
'''

# PART A - open the file and read lines in to 2 dimensional data list
lines = open('supermarket_sales.csv').readlines()
# Use a list comprehension to remove line breaks
cleaned_lines = [line.rstrip() for line in lines]
# we will create a list of tuples, so initialize an empty list
data = []
for i,line in enumerate(cleaned_lines):
    #skip i == 0, the column header
    if i > 0:
        data.append(line.split(','))

# lets have a look at our data
print(data)  # looks good.
# NOTE 2 dimensions:  A list containg tuples is pythonic.  A list of lists is bad
# [(a,b,c),(d,e,f)] is a list of tuples vs. [[a,b,c],[d,e,f]] a list of lists - some peolple do this
# because they learned another language first before python and don't understand tuples

# PART B -- this is not the best way, but the easiest to understand.
# I'm using list comprehensions, and essential and basic tool in python

A_totals = [float(line[9]) for line in data if line[1] == 'A']
B_totals = [float(line[9]) for line in data if line[1] == 'B']
C_totals = [float(line[9]) for line in data if line[1] == 'C']

report = {"A":sum(A_totals),"B":sum(B_totals),"C":sum(C_totals)}
print(report)

# PART C
