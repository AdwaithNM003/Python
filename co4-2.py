class bank:
	def __init__(self):
		self.accno=int(input("Enter account number: "))
		self.accname=input("Enter account name: ")
		self.acctype=input("Enter ifsc: ")
		self.accbal=0
	def depo(self):
		money=int(input("enter amount to be deposited: "))
		self.accbal=self.accbal+money
	def dispdetails(self):
		print("acc number: ",self.accno)
		print("acc name: ",self.accname)
		print("acc type: ",self.acctype)
		print("acc balance: ",self.accbal)
	def withdraw(self):
		amount=int(input("enter amount to be withdrawn: "))
		if amount>self.accbal:
			print("Balance not sufficient")
		elif self.accbal==0:
			print("Account balance is empty")
		else:
			print("money withdrawn!!")
			self.accbal=self.accbal-amount
			print("Money withdrawn is ",amount)
b1=bank()
while(True):
	print("\n1.Deposit\n2.withdraw\n3.display details\n4.exit\n")
	ch=int(input("Enter your choice: "))
	if ch==1:
		b1.depo()
	elif ch==2:
		b1.withdraw()
	elif ch==3:
		b1.dispdetails()
	elif ch==4:
		print("Thank you ..exiting..")
		break;
	else:
		print("Invalid choice..")

