# 114. Flatten Binary Tree to Linked List

# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Pre-order Traverse:
class Solution:
	
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		self.lastNode = None
		self.preorderTraverse(root)

	def preorderTraverse(self, root):
		if not root:
			return

		if self.lastNode:
			self.lastNode.left = None
			self.lastNode.right = root

		# pre-order traverse
		# root.right快照, 否则root.right会在preorderTraverse(root.left)时改变
		right = root.right
		self.lastNode = root
		self.preorderTraverse(root.left)
		self.preorderTraverse(right)


# Divide and Conquer
class Solution:
	
	def flatten(self, root):
		self.helper(root)

	def helper(self, root):
		if not root:
			return

		leftLast = self.helper(root.left)
		rightLast = self.helper(root.right)

		# connect leftLast to root.right
		if leftLast:
			leftLast.right = root.right
			root.right = root.left
			root.left = None

		if rightLast:
			return rightLast

		if leftLast:
			return leftLast

		return root