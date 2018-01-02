def fibonacci_gen(x):
	fib_list = []
	fib_list.append(1)
	fib_list.append(1)
	print (fib_list)
	i = 2
	while (i < x):
		fib_list.append(fib_list[(i-1)] + fib_list[(i-2)])
		i += 1
	return (fib_list)
	
cnt = int(input("How many Fibonacci numbers do you want in your list? : "))
fib = fibonacci_gen(cnt)
print ("Your Fibonacci sequence:")
print (fib)