# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		m = len(grid)
		if m == 0:
			return 0

		n = len(grid[0])
		visit = [[False for i in range(n)] for j in range(m)]
		# 如果是陆地且从未访问过, 则返回True
		def check(x, y):
			if 0 <= x < m and 0 <= y < n and grid[x][y] and visit[x][y] == False:
				return True

		# 广度优先搜索所有(x,y)相邻的点
		# 直到所有跟(x,y)在同一个岛上的点都被标记为 visit = True
		def bfs(x, y):
			# nearby row, col的组合分别对应上下左右相邻的点
			nbrow = [1, 0, -1, 0]
			nbcol = [0, 1, 0, -1]
			# q 用队列记录岛屿的边界, 坐标用tuple表示
			q = [(x, y)]
			while len(q) > 0:
				# 元组可以通过下标访问
				x = q[0][0]
				y = q[0][1]
				q.pop(0)
				for k in range(4):
					newx = x + nbrow[k]
					newy = y + nbcol[k]
					if check(newx, newy):
						visit[newx][newy] = True
						q.append((newx, newy))

		count = 0
		for row in range(m):
			for col in range(n):
				if check(row, col):
					visit[row][col] = True
					bfs(row, col)
					count += 1
		return count