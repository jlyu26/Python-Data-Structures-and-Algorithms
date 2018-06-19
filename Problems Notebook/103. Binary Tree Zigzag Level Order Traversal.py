# 103. Binary Tree Zigzag Level Order Traversal

# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# 思路跟102 107一样, 结果判断奇偶reverse一下就好

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		results = []
		if root is None:
			return results

		q = [root]
		while q:
			level = []
			results.append([node.val for node in q])
			for node in q:
				if node.left:
					level.append(node.left)
				if node.right:
					level.append(node.right)
			q = level

		for i in range(len(results)):
			if i % 2 == 1:
				results[i] = results[i][::-1]

		return results
