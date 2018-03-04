A = [2,2,2,3]
def is_array_sorted(A):
	if all(A[i] == A[i+1] for i in range(len(A)-1)):
		return True
	else:
		return False
print(is_array_sorted(A))

