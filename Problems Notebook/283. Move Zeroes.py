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
# 一个指向最前面的0，一个查找后面的非0

class Solution:
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if nums is None:
			return []
		
		zero = 0
		search = 0
		while zero < len(nums):
			if nums[zero] != 0:
				zero += 1
			else:	# 在后面找到一个非0与之交换
				search = zero + 1
				while search < len(nums):
					if nums[search] == 0:
						search += 1
					else:
						nums[zero] = nums[search]
						nums[search] = 0
						break
				zero += 1

		# return nums
		