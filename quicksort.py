import math
from selectionsort import randNum

def part(nums, l, r):
	i = l
	j = r
	pivot = nums[(l+r)/2]
	while i <= j:
		while nums[i] < pivot:
			i = i + 1
		while nums[j] > pivot:
			j = j - 1
		if i <= j:
			tmp = nums[i]
			nums[i] = nums[j]
			nums[j] = tmp
			i = i + 1
			j = j - 1
	return i
	
def qwik(nums, l, r):
	index = part(nums, l, r)
	if (l < index - 1):
		qwik(nums, l, index - 1)
	if (index < r):
		qwik(nums, index, r)
	return nums
		
nums = randNum(10, 0, 100)
print nums
print qwik(nums, 0, len(nums)-1)