# 94. Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	
	# Non Recursion	
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result = []
		if not root:
			return result

		stack = []
		# 1. 添加所有左节点到stack
		while root:
			stack.append(root)
			root = root.left

		while stack:
			# 2. 把最后进入stack的node(最深的左节点)添加到result
			node = stack.pop()
			result.append(node.val)
			# 3. 如果该node右节点不为空, 重复步骤1
			if node.right:
				node = node.right
				while node:
					stack.append(node)
					node = node.left

		return result

	

	# Recursion:
	def traverse(self, root, result):
		if not root:
			return result

		self.traverse(root.left, result)
		result.append(root.val)
		self.traverse(root.right, result)

		return result

	def inorderTraversal(self, root):
		result = []
		return self.traverse(root, result)