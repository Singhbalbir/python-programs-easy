length = int(input("Enter the height of the pyramid: "))
def pyramid(x):
	for i in range(0, x):
		for j in range(0, i+1):
			print("*", end="")
		print("\r")
pyramid(length)
	
