# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example:
# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]

# Given target = 5, return true.
# Given target = 20, return false.

# 思路：从左下角或右上角开始用排除法
# 以右上角为例：比target小则排除所在行, 比target大则排除所在列

class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if len(matrix) == 0:
			return False
		if len(matrix[0]) == 0:
			return False
		
		row, col = 0, len(matrix[0]) - 1
		while row < len(matrix) and col >= 0:
			if matrix[row][col] == target:
				return True
			elif matrix[row][col] < target:
				row += 1
			elif matrix[row][col] > target:
				col -= 1

		return False