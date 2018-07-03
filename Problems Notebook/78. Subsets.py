# 78. Subsets (全子集问题)

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.
# lintcode: Elements in a subset must be in non-descending order. (需要先sort一下)

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# Follow up: 如果nums中有重复元素? (90. Subset II)

# 思路: 基于组合的DFS
# 1. 最简单的递归方式, 选or不选 (适用的情况比较少, 组合类搜索专用)
class Solution:
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.results = []
		# nums是None和len(nums) == 0不能放在同一个异常里cover
		# 因为后者有一个subset为空集, 该返回[[]]
		if nums is None:
			return self.results

		# nums.sort()
		self.dfs(nums, 0, [])
		return self.results

	# 1. 递归的定义
	def dfs(self, nums, idx, subset):
		# 3. 递归的出口(什么时候结束)
		if idx == len(nums):
			self.results.append(subset)
			return

		# 2. 递归的拆解
		# 加nums[idx]
		self.dfs(nums, idx + 1, subset + [nums[idx]])
		# 不加nums[idx]
		self.dfs(nums, idx + 1, subset)


# 2. 虽然这道题是基于组合的DFS, 但代码的递归方式(for loop)可以应用到排列类搜索
class Solution:
	def subsets(self, nums):
		self.results = []
		if nums is None:
			return self.results
		if len(nums) == 0:
			return [[]]

		# nums.sort()
		self.dfs(nums, 0, [])
		return self.results

	# 1. 递归的定义：在nums中找到所有以subset开头的的集合, 并放到results
	# idx: 可以从nums[idx]开始选数加到subset里, 去寻找以subset开头的所有子集
	def dfs(self, nums, idx, subset):
		# 2. 递归的拆解: deep copy, 因为每次调用都append subset, subset每次都不一样
		# 如果不deep copy而只是reference的话results会变成len(nums)个最后一个subset
		import copy
		self.results.append(copy.deepcopy(subset))
		
		for i in range(idx, len(nums)):
			# [1] -> [1, 2]
			subset.append(nums[i])
			# 寻找所有以[1, 2]开头的集合, 并扔到results
			self.dfs(nums, i + 1, subset)
			# [1, 2] -> [1] backtracking, i += 1循环进入下一层后寻找[1, 3]开头的集合
			subset.remove(nums[i])

		# 3. 递归的出口
		# return