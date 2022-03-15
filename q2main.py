import csv

#import sys

#global itemsArray
itemsArray = []
totals_dict ={}
smData =[]

def read_data(filename):
    with open(filename) as csvfile:
      next (csvfile)
      for line in csvfile:
        return list(csv.reader(csvfile))


def branch_totals(itemsArray):
    #totals_dict = {}
    A_totals = [float(line[9]) for line in itemsArray if line[1] == 'A']
    totals_dict["A"]=sum(A_totals)
    B_totals = [float(line[9]) for line in itemsArray if line[1] == 'B']
    totals_dict["B"]=sum(B_totals)
    C_totals = [float(line[9]) for line in itemsArray if line[1] == 'C']
    totals_dict["C"]=sum(C_totals)
    return totals_dict


def report_dict(data):
    def total(items,branch,custType):
        sub_totals = [float(row[9]) for row in items if row[1]==branch and row[3] == custType]
        return round(sum(sub_totals),4)


    dict = {
        'A': {'Normal':total(smData,"A","Normal"), 'Member':total(smData,"A","Normal")},
        'B': {'Normal':total(smData,"B","Normal"), 'Member':total(smData,"B","Normal")},
        'C': {'Normal':total(smData,"C","Normal"), 'Member':total(smData,"C","Normal")}
    }
    return dict

smData = read_data('supermarket_sales.csv')
totals = branch_totals(smData)
print("-"*75,"\n")
print(totals_dict)
print("-"*75,"\n")
from pprint import pprint
pprint(report_dict(smData))
# So now that you have a nice dict, it should be elementary to use it to print a
# human readalbe report by accessing nested keys
dict = report_dict(smData)

print(f"""
Totals by Branch and Customer Type:
----------------------------------------------
Branch A: Normal ${dict['A']['Normal']}, Member ${dict['A']['Member']}
Branch B: Normal ${dict['B']['Normal']}, Member ${dict['B']['Member']}
Branch C: Normal ${dict['C']['Normal']}, Member ${dict['C']['Member']}
""")

def main():
    smData = read_data('supermarket_sales.csv')
    totals = branch_totals(smData)
    dict = report_dict(smData)
