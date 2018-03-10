# Uses python3
num = input()
var = [int(num)]
tokens = input().split()
high1 = 0
high1_index = 0
high2 = 0

for i in range(0, len(tokens)):
	if int(tokens[i])>high1:
		high1 = int(tokens[i])
		#print("high1 is: ", high1)
		high1_index = i
		#print("high1_index is: ", high1_index)

for j in range(0, len(tokens)):
	if j != high1_index:
		if int(tokens[j])>high2:
			high2 = int(tokens[j])
			#print("high2: ", high2)

print(high1*high2)
