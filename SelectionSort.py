import random

def randNum(i, min, max):
	randNumList = []
	for x in range(0,i):
		rand = random.randint(min,max)
		print rand
		randNumList.append(rand)
	return randNumList

print "How many numbers should we sort?"
listLen = int(raw_input('-->'))

print "Enter a number minimum"
minNum = int(raw_input('-->'))

print "Enter a number maximum"
maxNum = int(raw_input('-->'))

nums = randNum(listLen, minNum, maxNum)

print "Start: ", nums

for i in range(len(nums)):
	minindex = i
	for j in range(i+1,len(nums)):
		if nums[j] < nums[minindex]:
			minindex = j
	temp = nums[i]
	nums[i] = nums[minindex]
	nums[minindex] = temp
	print nums
	
