import random
from selectionsort import randNum

def qwik(nums):
	l = 0
	r = len(nums) - 1
	def part(nums, l, r):
		i = l
		j = r
		pivot = nums[random.randint(l,r)]
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
		
	def qwikSort(nums, l, r):
		index = part(nums, l, r)
		if (l < index - 1):
			qwikSort(nums, l, index - 1)
		if (index < r):
			qwikSort(nums, index, r)
		return nums
	return qwikSort(nums, l, r)
		
nums = randNum(10, 0, 100)
print nums
print qwik(nums)
