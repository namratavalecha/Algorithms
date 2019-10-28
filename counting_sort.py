def counting_sort(arr):
	n = len(arr)
	biggest = max(arr)
	smallest = min(arr)
	range_ = biggest-smallest+1
	count = [0 for i in range(range_)]
	output = [0 for i in range(n)]
	for i in range(n):
		count[arr[i]-smallest] +=1

	for i in range(1,len(count)):
		count[i] += count[i-1]

	for i in range(n-1,-1,-1):
		output[count[arr[i]-smallest]-1] = arr[i]
		count[arr[i]-smallest] -=1

	for i in range(0,n):
		arr[i]=output[i]


def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	counting_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)
# time complexity : O(n+k)