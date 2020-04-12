import time
import random

def findMin(aList):
	minElem = aList[0]
	for elem in aList:
		if elem < minElem:
			elem = minElem
	return minElem