# 585. Maximum Number in Mountain Sequence

# Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

# Example
# Given nums = [1, 2, 4, 8, 6, 3] return 8
# Given nums = [10, 9, 8, 7], return 10

class Solution:
	"""
	@param nums: a mountain sequence which increase firstly and then decrease
	@return: then mountain top
	"""
	def mountainSequence(self, nums):
		# write your code here
		if len(nums) == 1:
			return nums[0]

		start = 0
		end = len(nums) -1

		while start + 1 < end:
			mid = start + (end - start) // 2
			if nums[mid] > nums[mid + 1]:
				end = mid
			elif nums[mid] < nums[mid + 1]:
				start = mid


		if nums[start] >= nums[end]:
			return nums[start]
		else:
			return nums[end]
