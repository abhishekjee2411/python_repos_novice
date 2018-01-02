def check_primality(x):
	i = 1
	ctr = 0
	if (x == 0):
		return ("Neither Prime Nor Composite")
	while (i < x):
		if (x%i == 0):
			ctr += 1
		i += 1
	if (ctr > 1):
		return ("Not Prime")
	else:
		return ("Prime!")
		
num = int(input("Enter a number that you wish to check for primality:"))
res = check_primality(num)
print (res)