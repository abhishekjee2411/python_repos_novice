a = [1,1,2,3,5,8,13,21,34,55,89]
print ("Length of the list is : ",len(a))

print ("Printing all the elements of the list:")
i = 0
while (i < len(a)):
	print (a[i])
	i += 1

print ("Printing all elements less than 5:")
i = 0
while (i < len(a)):
	if a[i] < 5: print (a[i]," is less than 5")
	i += 1

print ("Transferring all the elements less than 5 into a new list")
i = 0
j = 0
b = [] 						#creating an empty list named "b"
while (i < len(a)):
	if a[i] < 5:
		b.append(a[i])
		j += 1
	i += 1

print ("Printing the new list")
i=0
print ("The length of the new list is : ",len(b))
while (i < len(b)):
	print (b[i])
	i += 1

print ("Printing a selective list:")
lim = int(input("Enter a limit value:"))
i = 0
while (i < lim):
	print (a[i])
	i += 1