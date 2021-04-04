class bankaccount:
	def __init__(self,balance):
		self.balance = balance
	def deposit(self):
		amount = float(input("\nEnter amount to be Deposited: "))
		self.balance += amount
		print("Amount Deposited:",amount)
		print("\nThank you! Visit us Again.....")
	def withdraw(self):
		amount = float(input("\nEnter amount to be Withdrawn: "))
		if self.balance >= amount:
			self.balance -= amount
			print("Amount Withdrawn:",amount)
			print("\nThank you! Visit us Again.....")
		else:
			print("NOTE: You have Insufficient balance in your Account.")
			print("\nThank you! Visit us Again.....")
	def display(self):
		print("\nAvailable Balance=",self.balance)
		print("Thank you! Visit us Again.....")

print("\n<<<------ WELCOME TO PB BANK ------>>>\n")
acc_no=[1101,1102,1103,1104,1105,1106]
acc_name=["piyush","shyam","sita","ram","gita","raju"]
acc = int(input("Account No:"))
for i in range(len(acc_no)):
	try :
		if (acc == acc_no[i]):
			print("Account Holder Name:",acc_name[i])
			if i == 0:
				ba=bankaccount(1284300)
			if i == 1:
				ba=bankaccount(45000)
			if i == 2:
				ba=bankaccount(120575)
			if i == 3:
				ba=bankaccount(85040)
			if i == 4:
				ba=bankaccount(10500)

	except :
		print("Check your Acc No.\nThanks for visiting!")

print("INSTRUCTIONS:\nPress 1 to Deposit Money\nPress 2 to Withdraw Money\nPress 3 to check Balance\nPress O to Exit\n")
while 1:
	ch=int(input("Choice:"))
	if ch==1:
		ba.deposit()
	if ch==2:
		ba.withdraw()
	if ch==3:
		ba.display()
	if ch==0:
		break
