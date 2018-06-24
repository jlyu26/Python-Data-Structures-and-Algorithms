# 144. Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	
	# Recursion:
	def traverse(self, root, result):
		if not root:
			return result
		
		result.append(root.val)
		self.traverse(root.left, result)
		self.traverse(root.right, result)
		
		return result

	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result = []
		return self.traverse(root, result)



	# Non Recursion:
	def preorderTraversal(self, root):
		result = []
		if not root:
			return result

		stack = [root]
		while stack:
			node = stack.pop()
			result.append(node.val)
			# 因为stack先进后出, 前序遍历要right先进才能让left先出
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

		return result