# Given a string which consists of lowercase or uppercase letters, 
# find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

###########################################################################################################

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        odd = {}

        for c in s:
        	if c in odd:
        		del odd[c]
        	else:
        		odd[c] = True
        
        if len(odd) > 0:
            return len(s) - (len(odd) - 1)

        return len(s)
