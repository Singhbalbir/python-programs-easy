length = int(input("enter the height of the pyramid: "))
num = 65
def pyramid(x):
	for i in range(0, x):
		for j in range(0, i+1):
			print(chr(num+i), end="")
		print()
pyramid(length)
			

	
