print "Enter a list of numbers"
numz = raw_input('-->').split()
nums = [int(n) for n in numz]

end = len(nums) - 1

print "Start: ", nums

for i in range(len(nums)):
	baby = nums[i]
	minindex = i
	for j in range(i+1,len(nums)):
		if nums[j] < nums[minindex]:
			minindex = j
	if i != minindex:
		temp = nums[i]
		nums[i] = nums[minindex]
		nums[minindex] = temp
	print nums
