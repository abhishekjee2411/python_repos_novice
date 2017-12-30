a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = range(1,14)

print (a)
print (b)
i = 0
while (i < len(b)):
	print (b[i])
	i += 1

i=0
b_ = []
while (i < len(b)):
	b_.append(b[i])
	i += 1

print (b_)

print ("Comparing the two lists and creating a new list containing the elements common to both!")
i = 0
j = 0
c = []

for i in a:
	for j in b:
		if i == j:
			c.append(i)

print (c)

print ("Sprucing up the new list by removing any duplicates!")
c_ = set(c)
print ("The new list is : ")
print (c_)
