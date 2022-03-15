#q2a
import csv

import sys

#global itemsArray
itemsArray = []

def read_data(filename):
    with open(filename) as csvfile:
      next (csvfile)
      for line in csvfile:
        return list(csv.reader(csvfile))

#q2b
#print(smData)

def branch_totals(itemsArray):
    totals_dict = {}
    A_totals = [float(line[9]) for line in itemsArray if line[1] == 'A']
    totals_dict["A"]=sum(A_totals)
    return totals_dict



def report_dict(data):
    def total(items,branch,custType):
        sub_totals = [float(row[9]) for row in items if row[1]==branch and row[3] == custType]
        return round(sum(sub_totals),4)

    # now that we have a reusable method, we can build our report dict
    dict = {
        'A': {'Normal':total(smData,"A","Normal"), 'Member':total(smData,"A","Normal")},
        'B': {'Normal':total(smData,"B","Normal"), 'Member':total(smData,"B","Normal")},
        'C': {'Normal':total(smData,"C","Normal"), 'Member':total(smData,"C","Normal")}
    }
    return dict

smData = read_data('supermarket_sales.csv')
totals = branch_totals(smData)
from pprint import pprint
pprint(report_dict(smData))





sys.exit()



#input('A', 105651.399)('B', 106197.672)('C', 110568.7065)
#sys.exit()
outputb = '''
Totals by Branch:
Branch A: 105651.399
Branch B: 106197.672
Branch C: 110568.7065
'''
print(outputb)

'''
part c
Totals by branch and customer type


Plan A
br| C Type  | Total
A | Normal | 3585
A | Member |
B | Normal
B | Member
C | Normal
C | Member


{"A": 123456.123, "B": 234567.567, "C": 345678.9987}

#q2c
#Q2C (list version)
aArrayM =[]
bArrayM =[]
cArrayM =[]
aArrayN =[]
bArrayN =[]
cArrayN =[]

tList =[]

for i in range(0,len(itemsArray)):

  if itemsArray[i][1]=="A" and itemsArray[i][3]== "Member":
    aArrayM.append (itemsArray[i][9])
    tList.insert(len(tList),(A,str(sum(aArrayM))))
  elif itemsArray[i][1]=="A" and itemsArray[i][3]== "Normal":
    aArrayN.append (itemsArray[i][9])
    tList.insert(len(tList),(A,str(sum(aArrayN))))
  elif itemsArray[i][1]=="B" and itemsArray[i][3]== "Member":
    bArrayM.append (itemsArray[i][9])
    tList.insert(len(tList),(B,str(sum(bArrayM)))
  elif itemsArray[i][1]=="B" and itemsArray[i][3]== "Normal":
    bArrayN.append (itemsArray[i][9])
    tList.insert(len(tList),(B,str(sum(bArrayN)))
  elif itemsArray[i][1]=="C" and itemsArray[i][3]== "Member":
    cArrayM.append (itemsArray[i][9])
    tList.insert(len(tList),(C,str(sum(cArrayM))))
  elif itemsArray[i][1]=="C" and itemsArray[i][3]== "Normal":
    cArrayN.append (itemsArray[i][9])
    tList.insert(len(tList),(C,str(sum(cArrayN))))

print(tList)
'''
