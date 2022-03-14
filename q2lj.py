#q2a
import csv

#global itemsArray
itemsArray = []

with open('supermarket_sales.csv') as csvfile:
  next (csvfile)
  for line in csvfile:
    itemsArray = list(csv.reader(csvfile))


#q2b

aArray =[]
bArray =[]
cArray =[]

tDict ={}

for i in range(0,len(itemsArray)):

  if itemsArray[i][1]=="A":
    aArray.append (float(itemsArray[i][9]))
    tDict.update({"A":round(sum(aArray),4)})
  elif itemsArray[i][1]=="B":
    bArray.append (float(itemsArray[i][9]))
    tDict.update({"B":round(sum(bArray),4)})
  elif itemsArray[i][1]=="C":
    cArray.append (float(itemsArray[i][9]))
    tDict.update({"C":round(sum(cArray),4)})

#print(sum(aArray))
#print(sum(bArray))
#print(sum(cArray))

for i in sorted (tDict):
  print((i,tDict[i]), end ="")

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
