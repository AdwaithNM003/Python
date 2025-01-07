f=open("textfile1.txt","r")
g=open("abc.txt","w")
line=f.readlines()
for i in range(0,len(line)):
	if i%2==0:
		g.write(line[i])
g=open("abc.txt","r")
print(g.read())
f.close()
g.close()
	
	#print(line[i])
#for i in range(0,len(line)):
	


