# 611. Knight Shortest Path

# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, 
# find the shortest path to a destination position, return the length of the route.
# Return -1 if knight can not reached.

# Source and destination must be empty. Knight can not enter the barrier.

# Clarification

# If the knight is at (x, y), he can get to the following positions in one step:

# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)

# Example:

# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 2

# [[0,1,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 6

# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return -1

"""
Definition for a point.
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b
"""

class Solution:
	"""
	@param grid: a chessboard included 0 (false) and 1 (true)
	@param source: a point
	@param destination: a point
	@return: the shortest path 
	"""
	def shortestPath(self, grid, source, destination):
		# write your code here
		row = len(grid) # point里x表示row, y表示col
		col = len(grid[0])

		move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
		q = [source]
		step = 0
		while q:
			for size in range(len(q)):
				point = q.pop(0)
				if point.x == destination.x and point.y == destination.y:
					return step
				
				for dx, dy in move:
					newx = point.x + dx
					newy = point.y + dy
					if 0 <= newx < row and 0 <= newy < col and grid[newx][newy] == 0:
						grid[newx][newy] = 1	# 千万不要忘记把已经访问过的点标记, 否则会超时!!!
						q.append(Point(newx, newy))
			step += 1

		return -1

# 如果follow up需要优化, 用Bidirectional BFS 双向宽度优先搜索