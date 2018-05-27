# 533. Two Sum - Closest to target

# Given an array nums of n integers, find two integers in nums such that the sum is 
# closest to a given number, target.
# Return the difference between the sum of the two integers and the target.  

# Example
# Given array nums = [-1, 2, 1, -4], and target = 4.
# The minimum difference is 1. (4 - (2 + 1) = 1).

# Challenge
# Do it in O(nlogn) time complexity.

# 思路：相向双指针

class Solution:
	"""
	@param nums: an integer array
	@param target: An integer
	@return: the difference between the sum and the target
	"""
	def twoSumClosest(self, nums, target):
		
		nums.sort()
		length = len(nums)

		start = 0
		end = length - 1
		min_diff = abs(nums[start] + nums[end] - target)
		while start < end:
			diff = nums[start] + nums[end] - target			
			if abs(diff) < min_diff:
				min_diff = abs(diff)

			if nums[start] + nums[end] < target:
				start += 1
			elif nums[start] + nums[end] > target:
				end -= 1
			else:
				return 0

		return min_diff