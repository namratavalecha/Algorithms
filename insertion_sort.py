
def insertion_sort(arr):
	for j in range(1, len(arr)):
		key = arr[j]
		i = j-1
		while i>=0 and arr[i]>key:
			arr[i+1] = arr[i]
			i = i-1
		arr[i+1] = key
	return(arr)

def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end = " ")

arr = [12,55,35,45,22,100,3,1,0,23]
print("Array before sorting:")
print_array(arr)
insertion_sort(arr)
print("\nArray after sorting:")
print_array(arr)

# time complexity: O(n^2)

