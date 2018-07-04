# 268. Missing Number

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# Note:
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant extra space complexity?

# 这道题本意应该是用二进制

# Time Limit Exceeded
class Solution:
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		for i in range(0, len(nums) + 1):
			if i not in nums:
				return i

		return -1

# 等差数列求和(鸡贼)
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        length = len(nums)
        return sum(range(0, length + 1)) - sum(nums)