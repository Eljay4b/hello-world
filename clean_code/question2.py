'''
PART A:
[10 pts] Write a Python function that reads the Supermarket Sales data into a 2 dimensional structure.

Note: The first line of the CSV contains the column headings, therefore it should not be stored in the 2 dimensional data list. You can skip the first line of the data file

Peder: Using a CSV library is kind of cheating, so this is the raw input method
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
'''
PART B
 [5 pts] Write a function to receive the Supermarket Sales list (that you created in the previous question) and return the total sales (the sum of column Total) of the branches as a dictionary
  The returned information should look like (the numbers given below may not be correct): {"A": 123456.123, "B": 234567.567, "C": 345678.9987}
'''
#Peder's notes: this is not the best way, but the easiest to understand.
# I'm using list comprehensions

A_totals = [float(line[9]) for line in data if line[1] == 'A']
B_totals = [float(line[9]) for line in data if line[1] == 'B']
C_totals = [float(line[9]) for line in data if line[1] == 'C']

report = {"A":sum(A_totals),"B":sum(B_totals),"C":sum(C_totals)}
print(report)

''' PART C
c) to receive the Supermarket Sales list and return an object (maybe a list or a dictionary) containing the total number of sales per Branch and per Customer Type.
The returned information can be either one of the below choices or another (The numbers given below may not be correct):)

a dictionary like {"A": {"Member": 230, "Normal": 351}, "B": {"Member": 123, "Normal": 117}, "C": {"Member": 335, "Normal": 18}}

a list like [ [230, 351], [123, 117], [335, 18]] You need to consider the best structure to return since you will be displaying this information in a human-readable format in the following question.
'''
# code here

'''
PART D
 [5 pts] Write a Python program to do the following:
Call the function you wrote in a) to read the data file Call the function you wrote in b) to calculate the total sales information and display the information on the screen Call the function you wrote in c) to calculate the total number of sales per Branch and per Customer Type and display the information on the screen Note: While displaying the information on the screen, the outputs should be human-readable and understandable (e.g. column headings, row names)
'''
# code here
