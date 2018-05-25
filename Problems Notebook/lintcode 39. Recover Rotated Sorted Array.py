# 39. Recover Rotated Sorted Array

# Given a rotated sorted array, recover it to sorted array in-place.

# Example
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

# Challenge
# In-place, O(1) extra space and O(n) time.

# 思路：先遍历找到断点，再用三步翻转法
# P.S. Python也可以直接return sorted(nums)...

class Solution:
	"""
	@param nums: An integer array
	@return: nothing
	"""
	def recoverRotatedSortedArray(self, nums):
		# find last number that >= nums[0]
		start = 0
		end = start + 1
		break_idx = -1

		while end < len(nums):
			if nums[start] <= nums[end]:
				start += 1
				end += 1
			else:
				break_idx = end
				break

		if break_idx == -1:
			return
		else:
			nums[:break_idx] = nums[:break_idx][::-1]
			nums[break_idx:] = nums[break_idx:][::-1]
			nums.reverse()