def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		merge_sort(left)
		merge_sort(right)
		i=j=k=0
		while i < len(left) and j<len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i = i+1
			else:
				arr[k] = right[j]
				j = j+1
			k = k+1

		while i<len(left):
			arr[k] = left[i]
			i = i+1
			k = k+1

		while j<len(right):
			arr[k] = right[j]
			j = j+1
			k = k+1



def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	merge_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)

# time complexity: O(nlogn)