def get_int(helpval="Give me a number:"):
	return (input(helpval))
	
age = get_int("Give me your age:")
name = get_int("Give me your name:")
num = get_int()

print (name+", you are "+str(age)+" years old! The number you have entered is : "+str(num))