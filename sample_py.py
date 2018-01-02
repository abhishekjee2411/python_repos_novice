def get_input_val(helpvalue):
	return (input(helpvalue))
	
name = get_input_val("Enter your name:")
age = get_input_val("Enter your age:")
print (name+", you are "+str(age)+" years old")