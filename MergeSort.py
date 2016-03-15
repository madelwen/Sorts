import math

#def mergeSort(numList, lo, hi):
	# print "In merge sort with lo: %d and hi: %d" % lo hi
#	if lo < hi:
#		mid = (hi+lo)/2
#	numList = merge(mergeSort(numList, lo, mid), mergeSort(numList, mid+1, hi))
#	return numList
	
def sort(numList):
	print numList
	if len(numList) == 1:
		return numList
	mid = len(numList)//2
	left = numList[:mid]
	print "left: %s" % left
	right = numList[mid:]
	print "right: %s" % right
	sort(left)
	sort(right)
	merge(left, right)
		
def merge(list1, list2):
	print "Merging list1: %s" % list1
	print "and list2: %s" % list2
	sortList = []
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		print "i: %d" % i 
		print "len(list1): %d" % len(list1)
		if list1[i] < list2[j]:
			print "enter comparison 1"
			sortList.append(list1[i])
			print "appended list1[i]"
			i = i + 1
			print "i is: %d" % i
		else:
			print "enter comparison 2"
			sortList.append(list2[j])
			print "appended list2[j]"
			j = j + 1
			print "j is: %d" % j
	if i == len(list1) - 1:
		sortList.append(list1[i])
		print "appended last element of list1"
	elif j == len(list2) - 1:
		sortList.append(list2[j])
		print "appended last element of list2"
	print "Sorted list before return: %s" % sortList
	return sortList

numList = [9, 1, 3, 5, 2, 7]
print sort(numList)
	
