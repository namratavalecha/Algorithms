def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
	if n==1:
		print("Move disk 1 from " + from_rod + " to " + to_rod)
		return
	tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk " + str(n) + " from " + from_rod + " to " + to_rod)
	tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)


if __name__ == '__main__':
	tower_of_hanoi(3, 'A', 'C', 'B')


# T(n) = 2*T(n-1) + 1
# T(n) = 2^n