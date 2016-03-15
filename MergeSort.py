import math
from selectionsort import randNum

#def mergeSort(numList, lo, hi):
	# print "In merge sort with lo: %d and hi: %d" % lo hi
#	if lo < hi:
#		mid = (hi+lo)/2
#	numList = merge(mergeSort(numList, lo, mid), mergeSort(numList, mid+1, hi))
#	return numList

#def randNum(i, mi, ma):
	#return [random.randint(mi, ma) for _ in xrange(i)]
	
def sort(numList):
	print "NumList: %s" % numList
	if len(numList) == 1:
		return numList
	mid = len(numList)//2
	left = numList[:mid]
	print "left: %s" % left
	right = numList[mid:]
	print "right: %s" % right
	sortedLeft = sort(left)
	sortedRight = sort(right)
	return merge(sortedLeft, sortedRight)
		
def merge(list1, list2):
	print "Merging list1: %s" % list1
	print "and list2: %s" % list2
	sortList = []
	i = 0
	j = 0
	while i < len(list1) or j < len(list2):
		#print "i: %d" % i 
		#print "len(list1): %d" % len(list1)
		if i == len(list1):
			sortList.append(list2[j])
		elif j == len(list2):
			sortList.append(list1[i])
		else: 
			if list1[i] < list2[j]:
			#print "enter comparison 1"
				sortList.append(list1[i])
			#print "appended list1[i]"
				i = i + 1
			#print "i is: %d" % i
			else:
			#print "enter comparison 2"
				sortList.append(list2[j])
			#print "appended list2[j]"
				j = j + 1
			#print "j is: %d" % j
	#if i == len(list1) - 1:
		#sortList.append(list1[i])
		#print "appended last element of list1"
	#elif j == len(list2) - 1:
		#sortList.append(list2[j])
		#print "appended last element of list2"
	print "Sorted list before return: %s" % sortList
	return sortList

numList = randNum(10, 0, 100)
print sort(numList)
	
