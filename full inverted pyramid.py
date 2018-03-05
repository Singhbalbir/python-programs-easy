length = int(input("Enter the height of the pyramid: "))
def pyramid(x):
	for i in range(0, x+1):
		for j in range(0, i):
			print(" ", end="")
		print("*"*((2*(x-i+1))-1), end="")
		for k in range(0, i):
			print(" ", end="")
		print()
pyramid(length)
	
