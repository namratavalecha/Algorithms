def counting_sort(arr, exp1):
	n = len(arr)
	output = [0]*(n)
	count = [0]*(10)
	for i in range(0,n):
		index = (arr[i]//exp1)
		count[ (index)%10 ] += 1
	for i in range(1,10):
		count[i] += count[i-1]

	i = n-1
	while i>=0:
		index = (arr[i]//exp1)
		output[count[(index)%10]-1] = arr[i]
		count[(index)%10] -= 1
		i -= 1

	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

def radix_sort(arr):
	max1 = max(arr)
	exp = 1
	while max1//exp > 0:
		counting_sort(arr, exp)
		exp *= 10

def print_array(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=" ")


if __name__ == '__main__':
	arr = [12,55,35,45,22,100,3,1,0,23]
	print("Array before sorting:")
	print_array(arr)
	radix_sort(arr)
	print("\nArray after sorting:")
	print_array(arr)

# O(d*(n+b))
# d = O(log(k)/log(b))
# overall time complexity: O((n+b)*log(k)/log(b))
# for k<= n^c ==> O(nlog(n)/log(b))
# for b=n ==> O(n)