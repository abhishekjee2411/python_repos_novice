str = input("Enter a string for palindrome check:")
str2 = str[::-1]
if (str == str2):
	print ("String is a palindrome!")
else:
	print ("String is not a palindrome!")

