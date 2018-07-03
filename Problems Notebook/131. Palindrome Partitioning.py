# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example:

# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# 思路: 基于组合的DFS
# 组合的是两个字母间的缝隙, 切 or 不切, 一共n个缝隙则有2^(n-1)种组合
# aab
# a|ab
# aa|b
# a|a|b

class Solution:
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		self.results = []
		self.dfs(s, [])
		return self.results

	def isPalindrome(self, s):
		for i in range(len(s)):
			if s[i] != s[len(s) - 1 - i]:
				return False
		return True

	def dfs(self, s, lst):
		if len(s) == 0:
			self.results.append(lst)

		# 因为i代表缝隙所在位置所以+1
		for i in range(1, len(s) + 1):
			if self.isPalindrome(s[:i]):
				self.dfs(s[i:], lst + [s[:i]])