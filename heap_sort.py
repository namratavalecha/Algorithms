def heapify(arr, n, i):
	largest = i
	l = 2*i+1
	r = 2*i+2

	if l<n and arr[l]>arr[i]:
		largest = l
	if r<n and arr[r]>arr[largest]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)

def heap_sort(arr):
	n = len(arr)
	for i in range(n, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)


def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	heap_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)


# time complexity: O(nlogn)