length = int(input("Enter the height of the pyramid: "))
def pyramid(x):
	for i in range(x, 0, -1):
		for j in range(0, i):
			print(" ", end="")
		print("*"*(x-i+1))
pyramid(length)
	
