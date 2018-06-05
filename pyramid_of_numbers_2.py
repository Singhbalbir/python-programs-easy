length = int(input("enter the height of the pyramid: "))
var = 1
def pyramid(x,y):
	for i in range(0, x):
		for j in range(0, i+1):
			print(j+1, end="")
		print()
pyramid(length, var)

	
