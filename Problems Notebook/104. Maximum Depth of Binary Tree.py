# 104. Maximum Depth of Binary Tree

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its depth = 3.

# 思路: 遍历或分治

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

	# Traverse
	def traverse(self, root, currDepth):
		# inorder dfs
		if not root:
			return

		self.depth = max(currDepth, self.depth)
		self.traverse(root.left, currDepth + 1)
		self.traverse(root.right, currDepth + 1)

	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.depth = 0
		self.traverse(root, 1)
		return self.depth



	# Divide and Conquer
	def maxDepth(self, root):
		if not root:
			return 0

		left = self.maxDepth(root.left)
		right = self.maxDepth(root.right)
		return max(left, right) + 1