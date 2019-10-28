def bubble_sort(arr):
	for i in range(0, len(arr)):
		swapped = False
		for j in range(0, len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if swapped == False:
			break

def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	bubble_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)

# time complexity: O(n^2) - worst and average case
# O(n) - best case