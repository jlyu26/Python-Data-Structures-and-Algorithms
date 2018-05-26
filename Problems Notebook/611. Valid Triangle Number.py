# 611. Valid Triangle Number

# Given an array consists of non-negative integers, your task is to count the number of triplets chosen 
# from the array that can make triangles if we take them as side lengths of a triangle.

# Example 1:
# Input: [2,2,3,4]
# Output: 3

# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].

# 思路：三角形充要条件 a + b > c 两短边相加大于第三边

class Solution:
	def triangleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		length = len(nums)
		if length < 3:
			return 0

		nums.sort()

		count = 0
		# 在nums[:i]里找相加大于nums[i]的pairs
		for i in range(2, length):
			left = 0
			right = i - 1	# 从右往左循环第二大的边
			while left < right:
				if nums[left] + nums[right] > nums[i]:
					count += right - left
					right -= 1
				else:
					left += 1

		return count