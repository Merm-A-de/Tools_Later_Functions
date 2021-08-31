def fib():
	a = 1
	b = 2
	for i in range (1,25):
		a, b = b, a+b
		print(a)
	
fib()
