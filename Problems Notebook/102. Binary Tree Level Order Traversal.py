# 102. Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Challenge
# Challenge 1: Using only 1 queue to implement it.
# Challenge 2: Use DFS algorithm to do it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		results = []
		if not root:
			return results

		# 思路：用bfs / queue
		# 需要回来看challenge的follow up
		q = [root]
		while q:
			level = []
			results.append([n.val for n in q])
			for node in q:
				if node.left:
					level.append(node.left)
				if node.right:
					level.append(node.right)
			q = level

		return results