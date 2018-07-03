# 90. k Sum II

# Given n unique integers, number k (1<=k<=n) and target.
# Find all possible k integers where their sum is target.

# Example:
# Given [1,2,3,4], k = 2, target = 5. Return:
# [
#   [1,4],
#   [2,3]
# ]

# 思路: 基于组合的DFS
# 1. 最简单的递归方式, 选or不选 (适用的情况比较少, 组合类搜索专用)
# 参见78. Subsets
class Solution:
	"""
	@param: A: an integer array
	@param: k: a postive integer <= length(A)
	@param: targer: an integer
	@return: A list of lists of integer
	"""
	def kSumII(self, A, k, target):
		# write your code here
		self.results = []
		self.dfs(A, k, target, 0, [])
		return self.results

	def dfs(self, A, k, target, idx, lst):
		# 找到一个解, 把这个解lst加到results
		if target == 0 and k == 0:
			self.results.append(lst)
			return

		# idx越界或没有解
		if idx == len(A) or target < 0 or k < 0:
			return

		# 不选, 直接跳到下一个数字
		self.dfs(A, k, target, idx + 1, lst)
		# 选
		self.dfs(A, k-1, target - A[idx], idx + 1, lst + [A[idx]])



# 2. 通用的递归方式, for loop回溯法
class Solution:
	def kSumII(self, A, k, target):
		self.results = []
		if not A or k == 0:
			return self.results

		A.sort()
		self.dfs(A, k, target, 0, [])
		return self.results

	def dfs(self, A, k, target, idx, lst):
		if target == 0 and k == 0:
			import copy
			self.results.append(copy.deepcopy(lst))
			return

		if k == 0:
			return

		for i in range(idx, len(A)):
			if A[idx] > target:
				break

			lst.append(A[i])
			self.dfs(A, k - 1, target - A[i], i + 1, lst)
			lst.remove(A[i])