'''
Question 2
'''
import csv

def read_data(filename):
    with open(filename) as csvfile:
      next (csvfile)
      for line in csvfile:
        return list(csv.reader(csvfile))


def branch_totals(itemsArray):
    totals_dict = {}
    A_totals = [float(line[9]) for line in itemsArray if line[1] == 'A']
    totals_dict["A"]=sum(A_totals)
    return totals_dict



def report_dict(data):
    def total(items,branch,custType):
        sub_totals = [float(row[9]) for row in items if row[1]==branch and row[3] == custType]
        return round(sum(sub_totals),4)

    # Building a dict to use later for printing report
    dict = {
        'A': {'Normal':total(smData,"A","Normal"), 'Member':total(smData,"A","Member")},
        'B': {'Normal':total(smData,"B","Normal"), 'Member':total(smData,"B","Member")},
        'C': {'Normal':total(smData,"C","Normal"), 'Member':total(smData,"C","Member")}
    }
    return dict

smData = read_data('supermarket_sales.csv')
totals = branch_totals(smData)
# print out the branch totals
from pprint import pprint
pprint(totals)

# make report by making hierarchical dict and then accessing nested keys 
dict = report_dict(smData)

print(f"""
Totals by Branch:
-----------------
Branch A: Normal ${dict['A']['Normal']}, Member ${dict['A']['Member']}
Branch B: Normal ${dict['B']['Normal']}, Member ${dict['B']['Member']}
Branch B: Normal ${dict['C']['Normal']}, Member ${dict['C']['Member']}
etc.
""")
