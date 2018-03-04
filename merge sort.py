import sys
A = [5,2,5,4,7,1,3]
def sort_array(A):
	sorting(A, 0, len(A)-1)
	return A
	
def sorting(A, first, last):
	if first < last:
		middle = (first + last)//2
		sorting(A, first, middle)
		sorting(A, (middle+1), last)
		merge(A, first, middle, last)
	
def merge(A, first, middle, last):
	left_array = A[first:middle+1]
	right_array = A[(middle+1):last+1]
	left_array.append(sys.maxsize)
	right_array.append(sys.maxsize)
	i = j = 0
	for k in range(first, last+1):
		if left_array[i] <= right_array[j]:
			A[k] = left_array[i]
			i += 1
		else:
			A[k] = right_array[j]
			j += 1
	
print(sort_array(A))
			
