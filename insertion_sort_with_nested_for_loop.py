A = [5,2,5,4,7,1,3]
def sort_array(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				j -= 1
			else:
				break
	return A

print(sort_array(A))
