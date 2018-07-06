# 44. Wildcard Matching 通配符比较

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.

# Example 1:
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Example 4:
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

# Example 5:
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

class Solution:
	def isMatch(self, s, p):
		"""
		:type s: str (纯字符串)
		:type p: str (带通配符的)
		:rtype: bool
		"""
		m, n = len(p), len(s)
		memo = [[False for j in range(m)] for i in range(n)]
		visited = [[False for j in range(m)] for i in range(n)]
		return self.isMatchHelper(s, 0, p, 0, memo, visited)

	def isMatchHelper(self, s, sIndex, p, pIndex, memo, visited):
		# 如果p从pIdex开始是空字符串了, 那么s也必须从sIndex是空才能匹配上
		if pIndex == len(p):
			return sIndex == len(s)

		# 如果s从sIndex是空, 那么p必须全是*
		if sIndex == len(s):
			return self.allStar(p, pIndex)

		if visited[sIndex][pIndex]:
			return memo[sIndex][pIndex]

		sChar = s[sIndex]
		pChar = p[pIndex]
		match = False

		if pChar is '*':
			match = self.isMatchHelper(s, sIndex, p, pIndex + 1, memo, visited) or self.isMatchHelper(s, sIndex + 1, p, pIndex, memo, visited)
		else:
			match = self.charMatch(sChar, pChar) and self.isMatchHelper(s, sIndex + 1, p, pIndex + 1, memo, visited)

		visited[sIndex][pIndex] = True
		memo[sIndex][pIndex] = match
		return match

	def allStar(self, p, pIndex):
		for i in range(pIndex, len(p)):
			if p[i] != '*':
				return False
		return True

	def charMatch(self, sChar, pChar):
		return sChar == pChar or pChar == '?'