print "Enter a list of numbers"
numz = raw_input('-->').split()
nums = [int(n) for n in numz]

end = len(nums) - 1

print "Start: ", nums
i = 0
while i != end:
	baby = nums[i]
	minindex = i
	j = i + 1
	while j < len(nums):
		if nums[j] < nums[minindex]:
			minindex = j
		j = j + 1
	if i != minindex:
		temp = nums[i]
		nums[i] = nums[minindex]
		nums[minindex] = temp
	print nums
		
	i = i + 1
