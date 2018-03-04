A = [5,2,5,4,7,1,3]
def sort_array(A):
	sorting(A, 0, len(A)-1)
	return A

def sorting(A, low, high):
	if low<high:
		p = partition(A, low, high)
		sorting(A, low, p-1)
		sorting(A, p+1, high)
	
def find_pivot(A, low, high):
	mid = (low+high)//2
	pivot = high
	if A[low]<A[mid]:
		if A[mid]<A[high]:
			pivot = mid
	elif A[low]>=A[mid]:
		if A[high]>A[low]:
			pivot = low
	return pivot
		
def partition(A, low, high):
	pivotIndex = find_pivot(A, low, high)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low
	
	for i in range(low, high+1):
		if A[i]<pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]
	return border
		
print(sort_array(A))
