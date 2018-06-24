# 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X

# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X

# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board 
# are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the 
# border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected 
# horizontally or vertically.

class Solution:

	# fill(): 对于点(x,y)如果没被访问过且为'O', 将其标记为W, 再把其相邻的'O'也标记为'W'
	def fill(self, board, x, y):
		
		if board[x][y] != 'O':
			return

		nbx = [0, 1, 0, -1]
		nby = [1, 0, -1, 0]

		q = [(x, y)]
		board[x][y] = 'W'

		while len(q) > 0:
			x = q[0][0]
			y = q[0][1]
			q.pop(0)

			for i in range(4):
				nx = x + nbx[i]
				ny = y + nby[i]
				if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'O':
					board[nx][ny] = 'W'
					q.append((nx, ny))

	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if not board:
			return

		m = len(board)
		n = len(board[0])

		# 从board的左/右两条边出发, 把'O'标记为'W'
		for i in range(m):
			self.fill(board, i, 0)
			self.fill(board, i, n - 1)

		# 从board的上/下两条边出发, 把'O'标记为'W'
		for j in range(n):
			self.fill(board, 0, j)
			self.fill(board, m - 1, j)

		# 上面两个for循环把所有位于边上的联通'O'都标记成了'W'
		# 遍历所有的点, 除了跟边联通的'O'之外全都标记成'X'
		for i in range(m):
			for j in range(n):
				if board[i][j] == 'W':
					board[i][j] = 'O'
				else:
					board[i][j] = 'X'