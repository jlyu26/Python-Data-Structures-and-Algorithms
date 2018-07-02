# 90. Subsets II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.results = []
		if nums is None:
			return self.results
		# if len(nums) == 0:
		# 	return [[]]

		nums.sort()
		self.dfs(nums, 0, [])
		return self.results

	def dfs(self, nums, idx, subset):
		import copy
		self.results.append(copy.deepcopy(subset))

		for i in range(idx, len(nums)):
			# 去重复
			if nums[i] == nums[i - 1] and i != idx:
				continue

			subset.append(nums[i])
			self.dfs(nums, i + 1, subset)
			subset.remove(nums[i])