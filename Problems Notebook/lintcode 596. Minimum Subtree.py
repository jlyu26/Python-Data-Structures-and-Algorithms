# 596. Minimum Subtree

# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

# Example
# Given a binary tree:

#      1
#    /   \
#  -5     2
#  / \   /  \
# 0   2 -4  -5 
# return the node 1.

# 思路: divide and conquer + traverse
# divide and conquer: 一个root的sum为左右子树的sum (类似于postorder)
# traverse: 对所有root求sum, 每次recursion都把当前root的sum和全局min打擂台

"""
Definition of TreeNode:
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
"""

class Solution:
	"""
	@param root: the root of binary tree
	@return: the root of the minimum subtree
	"""
	import sys
	minSum = sys.maxsize
	result = None

	def findSubtree(self, root):
		# write your code here
		self.traverse(root)
		return self.result

	def traverse(self, root):
		if not root:
			return 0

		# divide and conquer
		right = self.traverse(root.right)
		left = self.traverse(root.left)
		rootSum = right + left + root.val
		
		# traverse
		if rootSum < self.minSum:
			self.minSum = rootSum
			self.result = root

		return rootSum