# 140. Fast Power

# Calculate the a^n % b where a, b and n are all 32bit integers.

# Example:
# For 2^31 % 3 = 2
# For 1001000 % 1000 = 0

# Challenge:
# O(logn)

# 掌握得不好需要重新看！

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        result = 1
        while n > 0:
        	if n % 2 == 1:
        		result = result * a % b
        	a = a * a % b
        	n = n / 2
        return result % b