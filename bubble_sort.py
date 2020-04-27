

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp


def bubble_sort(array):
	for i in range(len(array)):
		for j in range(len(array)-1, i, -1):
			if array[j-1] > array[j]:
				swap(array, j-1, j)
	return array
	

if __name__ == "__main__":
	print(bubble_sort([5,4,8,10,6,3,2,1]))