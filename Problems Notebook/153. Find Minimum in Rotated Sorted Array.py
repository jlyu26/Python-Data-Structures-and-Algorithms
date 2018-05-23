# 153. Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# Example 1:
# Input: [3,4,5,1,2] 
# Output: 1

# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 1:
			return nums[0]

		# find first number that smaller than nums[0]
		start = 0
		end = len(nums) - 1
		
		if nums[start] < nums[end]:
			return nums[start]
		
		while start + 1 < end:
			mid = start + (end - start) // 2
			# because no duplicated numbers so no mid == nums[0]
			if nums[mid] < nums[0]:
				end = mid
			elif nums[mid] > nums[0]:
				start = mid

		if nums[start] < nums[end]:
			return nums[start]
		if nums[start] > nums[end]:
			return nums[end]