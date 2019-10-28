def insertion_sort(b):
	for i in range(1, len(b)):
		key = b[i]
		j = i-1
		while j>=0 and b[j]>key:
			b[j+1] = b[j]
			j -= 1
		b[j+1] = key
	return b


def bucket_sort(x):
	arr = []
	slot_num = 10
	for i in range(slot_num):
		arr.append([])
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
	for i in range(slot_num):
		arr[i] = insertion_sort(arr[i])
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x


def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [0.12,0.55,0.35,0.45,0.22,0.15,0.03,0.01,0.00,0.23]
	print("Array before sorting:")
	print_array(arr)
	arr = bucket_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)


# time complexity: O(n+k) (average)
# O(n^2) (worst case)