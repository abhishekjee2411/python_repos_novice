teststring = "my   name is aj"
test2 = teststring.split(" ")
print (test2)
test3 = teststring.split()
print (test3)
test4 = " ".join(test3)
print (test4)
print (len(test4))
print (test4[0])
print (test4[-1])

print ("Printing a sentence in reverse order!")

def rev_string(x):
	y = x.split()
	l = len(y)