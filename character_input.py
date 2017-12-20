name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
times = int(input("Enter the number of times you wish your message(s) to be printed: "))
byear = 2017 - age
i = 1
while (i <= times):
	print ("Dear "+name+", you are "+str(age)+" years old!")
	print ("You were born in the year "+str(byear))
	print ("You will turn 100 in the year "+str(byear + 100))
	print (times*"Done\n")
	i = i + 1
print ("Thank you! Visit again!")
