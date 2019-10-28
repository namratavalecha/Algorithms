def selection_sort(arr):
	for i in range(0, len(arr)-1):
		min = i

		for j in range(i+1, len(arr)):
			if arr[min]>arr[j]:
				min = j

		if min != i:
			temp = arr[min]
			arr[min] = arr[i]
			arr[i] = temp

def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")

arr = [12,55,35,45,22,100,3,1,0,23]
print("Array before sorting:")
print_array(arr)
selection_sort(arr)
print("\nArray after sorting:")
print_array(arr)

# time complexity: O(n^2)
