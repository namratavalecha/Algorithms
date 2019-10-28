RUN = 32

def insertion_sort(arr, left, right):
	for i in range(left+1, right+1):
		temp = arr[i]
		j = i-1
		while j>=left and arr[j]>temp:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = temp


def merge(arr, l, m, r):
	len1 = m-l+1
	len2 = r-m
	left = []
	right = []
	for i in range(len1):
		left.append(arr[l+i])
	for i in range(len2):
		right.append(arr[m+1+i])
	i, j, k = 0, 0, l
	while i<len1 and j<len2:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while i < len1:
		arr[k] = arr[i]
		i += 1
		k += 1
	while j<len2:
		arr[k] = arr[j]
		j += 1
		k += 1

def tim_sort(arr):
	n = len(arr)
	for i in range(0, n, RUN):
		insertion_sort(arr, i, min((i+31), (n-1)))

	size = RUN
	while size<n:
		for left in range(0, n, 2*size):
			mid = left+size-1
			right = min((left+2*size-1),(n-1))
			merge(arr, left, mid, right)
		size = 2*size

def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	tim_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)

# time complexity : O(nlogn) (worst)
# O(n) (best)