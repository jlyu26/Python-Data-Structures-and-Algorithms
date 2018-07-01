# 173. Binary Search Tree Iterator

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with 
# the root node of a BST.
# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, 
# where h is the height of the tree.

# 思路: 其实就是iteration inorder traverse
# 判断stack是否为空是.hasNext(), stack.pop()是.next()

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.stack = []
		self.curr = root

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.curr or self.stack

	def next(self):
		"""
		:rtype: int
		"""
		while self.curr:
			self.stack.append(self.curr)
			self.curr = self.curr.left

		# move iterator to next node, which
		# 如果当前点存在右子树，那么就是右子树中“一路向西”最左边的那个点
		# 如果当前点不存在右子树，则是走到当前点的路径中，第一个左拐的点
		self.curr = self.stack.pop()
		nxt = self.curr
		self.curr = self.curr.right
		return nxt.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())