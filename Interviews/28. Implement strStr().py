# 28. Implement strStr()

# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? 
# This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().

# 注意时间复杂度是O(m * n)
class Solution:
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		nlen = len(needle)
		hlen = len(haystack)
		if nlen == 0:
			return 0
		if nlen > hlen:
			return -1

		idx = 0
		while idx <= hlen - nlen:	# 注意idx
			if haystack[idx: idx + nlen] == needle:
				return idx
			idx += 1
		
		return -1