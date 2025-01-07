#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator	to compare the area of 2 rectangles.
class Rectangle:
	def __init__(self,length,breadth):
		self.__len=length
		self.__brea=breadth
	def area(self):
		return self.__len*self.__brea
	def __lt__(self,obj2):
		print("Area of rectangle 1 is: ",self.area())
		print("Area of rectangle 2 is: ",obj2.area())
		if(self.area()<obj2.area()):
			print("Rectangle 2 has greater area")
		elif(self.area()>obj2.area()):
			print("Rectangle 1 has greater area")
		else:
			print("Rectangles are equal")
	
length=float(input("Enter length of rectangle: "))
breadth=float(input("Enter breadth of rectangle: ")) 	
r1=Rectangle(length,breadth)
length2=float(input("Enter length of rectangle2: "))
breadth2=float(input("Enter breadth of rectangle2: ")) 	
r2=Rectangle(length2,breadth2)
#comparison between objects
r1 < r2		#function call
