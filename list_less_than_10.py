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
