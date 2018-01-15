def create_list():
	a = []
	inp = ''
	while (inp != '#'):
		inp = input("Enter a number:")
		a.append(inp)

	del a[len(a) -1]	
	return a

def rem_duplicates(n):
	b = set(n)
	return b

list_orig = create_list()
print ("Your original list:")
print (list_orig)
list_final = rem_duplicates(list_orig)
print ("Your processed list, or set:")
print (list_final)
print ("The length of the processed list (set) is:")
print (len(list_final))
list = list(list_final)
print ("The list of the set:")
print (list)
