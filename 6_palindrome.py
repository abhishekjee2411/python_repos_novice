str1 = input("Enter a string for palindrome check:")
lt = len(str1)
print ("The string you have entered is :",str1)
print ('Length of the string :',lt)
rc = 0
#-----------------------------------------------------------------------#
print ("Checking palindrome for spaces!")
i = 0
spc = 0
while (i < lt):
	if (str1[i] == ' '):
		print ("Blank space encountered!")
		spc += 1
	else:
		print ("Character encountered!")
		print (str1[i])
	i += 1
print ("There is/are",spc,"space(s) in the string!")
#-----------------------------------------------------------------------#
print ("Eliminating spaces now!")
i=0
str2 = ''

while (i < lt):
	if (str1[i] != ' '):
		str2 = str2+(str1[i])
	i += 1
print ("The compressed string is :",str2)
lt2 = len(str2)
print ("Length of the string :",lt2)
#-----------------------------------------------------------------------#
print ("Checking the evenness of the string!")
rc = 0
if (lt2%2 != 0):
	print ("Palindrome contains odd number of characters!")
	mid = lt2/2
	i = 0
	j = lt2 - 1
	while (i < mid and j > mid):
		if (str2[i] == str2[j]):
			i += 1
			j -= 1
		else:
			rc = 1
			break
else:
	print ("Palindrome contains even number of characters!")
	mid = lt2/2
	i = 0
	j = lt2 - 1
	while (i < mid and j >= mid):
		if (str2[i] == str2[j]):
			i += 1
			j -= 1
		else:
			rc = 1
			break
#-----------------------------------------------------------------------#
if (rc == 1):
	print ("Entered string",str1,"is not a palindrome!")
else:
	print ("Congratulations! Your string",str1,"is a palindrome!")