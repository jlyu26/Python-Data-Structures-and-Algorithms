# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution:
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		# candidates = list(set(candidates))
		candidates.sort()
		self.results = []
		self.dfs(candidates, target, 0, [])
		return self.results

	def dfs(self, candidates, target, idx, valueList):
		if target == 0:
			import copy
			return self.results.append(copy.deepcopy(valueList))
		
		for i in range(idx, len(candidates)):
			if candidates[i] == candidates[i - 1] and i != idx:
				continue
			if target < candidates[i]:
				return

			valueList.append(candidates[i])
			self.dfs(candidates, target - candidates[i], i + 1, valueList)
			valueList.remove(candidates[i])