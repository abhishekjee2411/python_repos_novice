x = range(2,20)
print (len(x))
i = 0
while (i < len(x)):
	print (x[i])
	i += 1
	
print ("Printing the elements in a different manner!")
for elem in x:
	print (elem)
	
print ("Printing the divisors of an entered number!")
dividend = int(input("Please enter a number whose divisors you wish to list:"))
i = 1
divisor = []
while (i <= dividend):
	if (dividend%i == 0):
		print (i,"divides",dividend)
		divisor.append(i)
	i += 1
print ("The dividend ",dividend,"has ",len(divisor),"elements!")
for elem in divisor:
	print (elem)
print (divisor)