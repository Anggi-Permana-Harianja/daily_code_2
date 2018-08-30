'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

list_nums = [1, 2, 3, 4, 5]
result = []

for i in range(len(list_nums)):
	tmp = list_nums[i]
	for j in range(len(list_nums)):
		tmp *= list_nums[j]
	tmp /= pow(list_nums[i], 2)
	result.append(int(tmp))

print(result) 
	

'''
follow-up question: what if you cant use division?
'''
list_num = [1, 2, 3, 4, 5]
result = []
tmp = 1

for i in range(len(list_nums)):
	for j in range(len(list_nums)):
		if list_nums[j] != list_nums[i]:
			tmp *= list_nums[j]
	result.append(tmp)
	tmp = 1

print(result)
