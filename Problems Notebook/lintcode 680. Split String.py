# 680. Split String

# Give a string, you can choose to split the string after one character or two adjacent characters, 
# and make the string to be composed of only one character or two characters. Output all possible results.

# Example
# Given the string "123"
# return [["1","2","3"],["12","3"],["1","23"]]


class Solution:
	"""
	@param: : a string to be split
	@return: all possible split string array
	"""

	def splitString(self, s):
		# write your code here
		self.results = []
		self.dfs(s, 0, [])
		return self.results

	# 思路1: 回溯法每次切1 or 2个字符 (超级慢)
	def dfs(self, s, idx, lst):
		if idx >= len(s):
			import copy
			self.results.append(copy.deepcopy(lst))
			return

		# 切1个
		if idx + 1 <= len(s):
			lst.append(s[idx: idx + 1])
			self.dfs(s, idx + 1, lst)
			lst.pop()
		# 切2个
		if idx + 2 <= len(s):
			lst.append(s[idx: idx + 2])
			self.dfs(s, idx + 2, lst)
			lst.pop()

	# 思路2: 通用的for循环 (超级慢)
	def dfs(self, s, idx, lst):
		if idx >= len(s):
			import copy
			self.results.append(copy.deepcopy(lst))
			return

		for i in range(1, 3):
			if idx + i <= len(s):
				lst.append(s[idx: idx + i])
				self.dfs(s, idx + i, lst)
				lst.pop()