# 570. Find the Missing Number II

# Giving a string with number from 1 to n in random order, but miss 1 number.Find that number. (n <= 30)

# Example:
# Given n = 20, str = 19201234567891011121314151618
# return 17

# 思路1: 用DFS把str切出来, 参见lintcode 680. split string
class Solution:
	"""
	@param n: An integer
	@param str: a string with number from 1-n in random order and miss one number
	@return: An integer
	"""
	def findMissing2(self, n, str):
		# write your code here
		self.n = n
		self.stringlist = []
		self.dfs(str, 0, [])
		
		for i in range(1, n + 1):
			if i not in self.stringlist:
				return i
		
		return -1
	
	def validNumber(self, str, lst):
		if int(str) in lst or (len(str) == 2 and int(str) < 10) or int(str) < 1 or int(str) > 30:
			return False
		return True


	def dfs(self, str, idx, lst):
		# 要注意检查lst的长度必须为n或n-1, 否则有不止一种切割方法
		if idx >= len(str) and (len(lst) == self.n - 1 or len(lst) == self.n):
			self.stringlist.extend(lst)
			return

		for i in range(1, 3):
			if idx + i <= len(str):
				number = int(str[idx: idx + i])
				if self.validNumber(str[idx: idx + i], lst):
					lst.append(number)
					self.dfs(str, idx + i, lst)
					lst.pop()