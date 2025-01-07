#Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time.
class time():
	 __hour=0
	 __min=0
	 __sec=0
	 def __init__(self,__hour,__min,__sec):
	 	self.__hour=__hour
	 	self.__min=__min
	 	self.__sec=__sec
	 	self.normalise()
	 def normalise(self):
	 	if self.__sec>=60:
	 		self.__min+=self.__sec//60
	 		self.__sec=self.__sec%60
	 	if self.__min>=60:
	 		self.__hour+=self.__min//60
	 		self.__min=self.__min%60
	 		
	 	#self.time()
	 #def time(self):
	 #	print("first time is ",self.__hour,"s ",self.__min,"s ",self.__sec,"s)
	 def __str__(self):
	 	return f"{self.__hour:02} hours :{self.__min:02} minutes :{self.__sec:02} seconds "
	 	
	 def __add__(self,other):
		 newhr=self.__hour+other.__hour
		 newmin=self.__min+other.__min
		 newsec=self.__sec+other.__sec
		 return time(newhr,newmin,newsec)

hr=int(input("Enter hour: "))
mint=int(input("Enter minute: "))
sec=int(input("Enter seconds: "))
t1=time(hr,mint,sec)
print("Time is ",hr," hours ",mint," minutes ",sec," seconds")
print()
print()
hr=int(input("Enter hour: "))
mint=int(input("Enter minute: "))
sec=int(input("Enter seconds: "))
t2=time(hr,mint,sec)
print("Time is ",hr," hours ",mint," minutes ",sec," seconds")
print()
print()
#operator overloading
t3 = t1 + t2
print("Combined times is ",t3)


