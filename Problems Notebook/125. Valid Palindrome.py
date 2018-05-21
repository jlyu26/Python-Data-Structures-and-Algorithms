# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None: return False

        str_lnum = ''

        # filter
        for char in s:
        	if char.isalnum():
        		str_lnum = str_lnum + char.lower()

        half_length = 0
        length = len(str_lnum)

        if length <= 1: return True
        
        if length % 2 == 0:
        	half_length = length / 2	# even
        else:
        	half_length = (length - 1) / 2	# odd

        start = 0
        end = length - 1

        while start < half_length:
        	if str_lnum[start] != str_lnum[end]:
        		return False
        	else:
        		start += 1
        		end -= 1

        return True
