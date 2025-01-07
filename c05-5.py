import csv
abc=[{'Name' :'Adwaith','rollno': 3,'Year':'MCA'},
{'Name' :'Adwa','rollno': 31,'Year':'MCA'},
{'Name' :'Achu','rollno': 32,'Year':'MCA'}]
fields=['Name','rollno','Year']
with open("dict.csv","w") as f:
 csvw=csv.DictWriter(f,fieldnames=fields)
 csvw.writeheader()
 csvw.writerows(abc)
with open("dict.csv","r") as f:
 csvr=csv.DictReader(f)
 for row in csvr:
 	print(row)
 
 
