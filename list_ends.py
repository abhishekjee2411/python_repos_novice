def list_ends(x):
	y = []
	y.append(x[0])
	y.append(x[len(x) -1])
	return y

x = [1,2,3,4,5,6,7,8,9,10]
z = list_ends(x)

print (z)

print ("Printing a user-created list!")

print ("We are going to create a list with as many numbers as you enter!")
print ("Once you are done entering the numbers, enter 'N' to mark the end of your list!")
i = 'N'
list = []
while (i == 'N' or i == 'n'):
	x = int(input("Enter a number:"))
	list.append(x)
	i = input("Do you wish to terminate (Y/N) ?")

print ("Your list is : ",list)
z = list_ends(list)
print ("The ends of your list are : ",z)