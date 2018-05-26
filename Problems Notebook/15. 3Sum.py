# 15. 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 不重复的理念不是找到结果后去重
# 而是找的时候就避免重复

class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()		
		result = []
		length = len(nums)

		# 用有自增功能的for循环
		for i in range(0, length - 2):
			# 跳过重复的
			if i and nums[i] == nums[i - 1]:	# 为什么这样写? 当i=0时?
				continue
			
			# 相向双指针 2Sum找target
			target = 0 - nums[i]
			left, right = i + 1, length - 1
			while left < right:
				if nums[left] + nums[right] < target:
					left += 1
				elif nums[left] + nums[right] > target:
					right -= 1
				elif nums[left] + nums[right] == target:
					result.append([nums[i], nums[left], nums[right]])
					left += 1
					right -= 1
					# 跳过重复的
					while left < right and nums[left] == nums[left - 1]:
						left += 1
					while left < right and nums[right] == nums[right + 1]:
						right -= 1

		return result