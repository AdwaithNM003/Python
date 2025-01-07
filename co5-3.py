import csv
f=open("samplecsv.csv","r")
lines=csv.reader(f)
li=[i for i in lines]
abc=[]
for x in range(len(li)):
 abc[x]=li[x]
for y in abc:
 print(y)

