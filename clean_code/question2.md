### Question 2 Instructions

a) [10 pts] Write a Python function that reads the Supermarket Sales data into a 2 dimensional structure.

Note: The first line of the CSV contains the column headings, therefore it should not be stored in the 2 dimensional data list. You can skip the first line of the data file

b) [5 pts] Write a function to receive the Supermarket Sales list (that you created in the previous question) and return the total sales (the sum of column Total) of the branches as a dictionary
  The returned information should look like (the numbers given below may not be correct): {"A": 123456.123, "B": 234567.567, "C": 345678.9987}

c) [5 pts] Write a function to receive the Supermarket Sales list and return an object (maybe a list or a dictionary) containing the total number of sales per Branch and per Customer Type.
The returned information can be either one of the below choices or another (The numbers given below may not be correct):)
a dictionary like {"A": {"Member": 230, "Normal": 351}, "B": {"Member": 123, "Normal": 117}, "C": {"Member": 335, "Normal": 18}} a list like [ [230, 351], [123, 117], [335, 18]] You need to consider the best structure to return since you will be displaying this information in a human-readable format in the following question.

d) [5 pts] Write a Python program to do the following:
Call the function you wrote in a) to read the data file Call the function you wrote in b) to calculate the total sales information and display the information on the screen Call the function you wrote in c) to calculate the total number of sales per Branch and per Customer Type and display the information on the screen Note: While displaying the information on the screen, the outputs should be human-readable and understandable (e.g. column headings, row names)
