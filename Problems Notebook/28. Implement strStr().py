# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().

###########################################################################################################

# Corner Case:
# 1. len(needle) = 0
# 2. len(needle) > len(haystack)

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        hs_len = len(haystack)
        n_len = len(needle)
        idx = 0
        current = ''

        if n_len == 0:
        	return 0
        
        if n_len > hs_len:
        	return -1

        while idx <= hs_len - n_len:
        	current = haystack[idx:idx + n_len]
        	if current == needle:
        		return idx
        	idx += 1
        
        return -1	