#-------------------------------------------------------------#
print ("------------------------------------------------------------")
#-------------------------------------------------------------#

nbr = int(input("Enter a number: "))
if (nbr%2 == 0):
	print ("The number is even!")
	if (nbr%4 == 0):
		print ("It is also a multiple of 4!")
	else:
		print ("It is not a multiple of 4!")
else:print ("The number is odd!")

#-------------------------------------------------------------#
print ("------------------------------------------------------------")
#-------------------------------------------------------------#

print ("Checking number 1 (check)'s divisibility by number 2 (num)!")
check = int(input("Enter a number (check): "))
num = int(input("Enter another number (num): "))

if (check%num == 0):
	print("The number "+str(check)+" is divisible by "+str(num)+"!")
else:
	print("The number "+str(check)+" is not divisible by "+str(num)+"!")
	
#-------------------------------------------------------------#
print ("------------------------------------------------------------")
#-------------------------------------------------------------#
