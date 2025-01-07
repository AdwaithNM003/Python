class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		area=self.length*self.breadth
		return area
	def perimeter(self):
		perimeter=2*(self.length+self.breadth)
		return perimeter
r1=Rectangle(20,12)
r2=Rectangle(15,8)
ar1=r1.area()
per1=r1.perimeter()
ar2=r2.area()
per2=r2.perimeter()
print("area of 1st rectangle",ar1)
print("perimeter of 1st rectangle",per1)
print("area of 2nd rectangle",ar2)
print("perimeter of 2nd rectangle",per2)
if ar1>ar2:
	print("1st rectangle area greater")
else:
	print("2nd rectangle area greater")
if per1>per2:
	print("1st rectangle perimeter greater")
else:
	print("2nd rectangle perimeter greater")


