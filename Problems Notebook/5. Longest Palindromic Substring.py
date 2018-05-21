# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

###########################################################################################################

# 思路：中心线枚举
# odd: a<b>a
# even: ab<c><c>ba

class Solution:

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if s is None or len(s) == 0:
			return ""

		# 每次调用该函数时left = right，为中轴线
		def findLongestPalindromePivot(s, left, right):
			length = 0
			while left >= 0 and right < len(s):
				if s[left] != s[right]:
					left -= 1
					right += 1
					break	# 退出整个循环
				
				if left == right:	# a<b>a
					length += 1
				else:	# a<b><b>a
					length += 2
				left -= 1
				right += 1

			return length

		start = 0
		longest = 0
		pivot = 0
		while pivot < len(s):
			length = findLongestPalindromePivot(s, pivot, pivot)	# a<b>a
			if length > longest:
				longest = length
				start = pivot - (length // 2)

			length = findLongestPalindromePivot(s, pivot, pivot + 1)	# a<b><b>a
			if length > longest:
				longest = length
				start = pivot - (length // 2) + 1
			pivot += 1

		return s[start: start + longest]