# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# 思路： two pointers
# 一个指向最前面过滤了0的，一个查找后面的非0往前挪

class Solution:
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if nums is None:
			return []
		
		left = 0
		right = 0
		while right < len(nums):
			if nums[right] == 0:
				right += 1
			else:
				nums[left] = nums[right]
				left += 1
				right += 1

		# 补全后面的0
		idx = left
		while left < len(nums):
			nums[left] = 0
			left += 1
		