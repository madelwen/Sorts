import math
from selectionsort import randNum
	
def zort(numList):
	if len(numList) == 1:
		return numList
	mid = len(numList)//2
	left = numList[:mid]
	right = numList[mid:]
	sortedLeft = zort(left)
	sortedRight = zort(right)
	return merge(sortedLeft, sortedRight)
		
def merge(list1, list2):
	sortList = []
	i = 0
	j = 0
	while i < len(list1) or j < len(list2):
		if i == len(list1):
			sortList.append(list2[j])
			j = j + 1
		elif j == len(list2):
			sortList.append(list1[i])
			i = i + 1
		else: 
			if list1[i] < list2[j]:
				sortList.append(list1[i])
				i = i + 1
			else:
				sortList.append(list2[j])
				j = j + 1
	return sortList

numList = randNum(10, 0, 100)
print numList
print zort(numList)
	
