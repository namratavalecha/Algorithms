def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return(i+1)


def quick_sort(arr, low, high):
	if low<high:
		pi = partition(arr, low, high)
		quick_sort(arr, low, pi-1)
		quick_sort(arr, pi+1, high)


def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	quick_sort(arr, 0, len(arr)-1)
	print("\nArray after sorting:")
	print_array(arr)


# time complexity: O(nlogn) (for best and average case)
# O(n^2) (for worst case)

