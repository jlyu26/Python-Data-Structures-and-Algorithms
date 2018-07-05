# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		self.results = []
		self.dfs(n, k, 1, 0, [])
		return self.results

	# n个数, k个数组合, 从1开始(是数字而不是索引), 初始组合长度0, 初始组合为空[]
	def dfs(self, n, k, idx, length, lst):
		if k == length:
			import copy
			self.results.append(copy.deepcopy(lst))
			return

		for i in range(idx, n + 1):
			lst.append(i)
			self.dfs(n, k, i + 1, length + 1, lst)
			lst.pop()