# 521. Remove Duplicate Numbers in Array

# Given an array of integers, remove the duplicate numbers in it.

# You should:
# Do it in place in the array.
# Move the unique numbers to the front of the array.
# Return the total number of the unique numbers.
# You don't need to keep the original order of the integers.

# Example
# Given nums = [1,3,1,4,4,2], you should:
# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.

# Actually we don't care about what you place in '?', 
# we only care about the part which has no duplicate integers.

# Challenge
# Do it in O(n) time complexity.
# Do it in O(nlogn) time without extra space.

# 思路：把已经出现过的都丢到后面去

class Solution:
	"""
	@param: nums: an array of integers
	@return: the number of unique integers
	"""
	def deduplication(self, nums):
		# write your code here
		if nums is None:
			return []

		start = 0
		end = len(nums) - 1
		Hash = {}
		while start <= end:
			if nums[start] in Hash:
				nums[start] = nums[end]
				end -= 1
			else:
				Hash[nums[start]] = start
				start += 1

		# end后面的全是重复的，所以不重复的部分长度是end+1
		return end + 1