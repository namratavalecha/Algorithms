def shell_sort(arr):
	n = len(arr)
	gap = n//2
	while gap>0:
		for i in range(gap, n):
			temp = arr[i]
			j = i
			while j>=gap and arr[j-gap]>temp:
				arr[j] = arr[j-gap]
				j-=gap
			arr[j] = temp
		gap//=2


def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	shell_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)

# time complexity: O(n^2)
