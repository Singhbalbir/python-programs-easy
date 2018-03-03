var1 = 1
var2 = 1
number = int(input("Enter the number to print Fibonacci sequence upto: "))

while var2 <= number:
	print(var2, " ")
	temp = var2
	var2 = var1 + var2
	var1 = temp
	
	
