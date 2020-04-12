arrayElems = [1,2,3,5,7,8,9,12]
def binarySearch(low, high, elem):
	while(low<=high):
		mid = (low + high) / 2
		if(arrayElems[mid] < elem):
			low = mid + 1
		elif(arrayElems[mid] > elem):
			high = mid - 1
		else:
			return mid
	return -1


print(binarySearch(0,len(arrayElems), 12))