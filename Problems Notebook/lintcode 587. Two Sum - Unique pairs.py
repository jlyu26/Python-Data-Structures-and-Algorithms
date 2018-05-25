# 587. Two Sum - Unique pairs

# Description
# Given an array of integers, find how many unique pairs in the array such that their 
# sum is equal to a specific target number. Please return the number of pairs.

# Example
# Given nums = [1,1,2,45,46,46], target = 47
# return 2

# 1 + 46 = 47
# 2 + 45 = 47

# 思路1：先sort, 再相向双指针

class Solution:
	"""
	@param nums: an array of integer
	@param target: An integer
	@return: An integer
	"""
	def twoSum6(self, nums, target):
		# write your code here
		nums.sort()

		start_hash = {}
		count = 0

		start = 0
		end = len(nums) - 1
		while start < end:
			if nums[start] + nums[end] == target:
				if nums[start] in start_hash:
					start += 1
					end -= 1
				else:
					count += 1
					start_hash[nums[start]] = True
					start += 1
					end -= 1
			elif nums[start] + nums[end] < target:
				start += 1
			elif nums[start] + nums[end] > target:
				end -= 1

		return count