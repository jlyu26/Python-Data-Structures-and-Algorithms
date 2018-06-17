# 74. Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Example 1:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true

# Example 2:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

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
		
		n, m = len(matrix), len(matrix[0])
		start, end = 0, n * m - 1

		# 循环退出时start or end有一个为target, or target不存在
		while start + 1 < end:
			mid = (start + end) // 2
			x, y = mid // m, mid % m
			if matrix[x][y] < target:
				start = mid
			else:
				end = mid

		# 分别判断start和end是不是target
		x, y = start // m, start % m
		if matrix[x][y] == target:
			return True

		x, y = end // m, end % m
		if matrix[x][y] == target:
			return True

		return False