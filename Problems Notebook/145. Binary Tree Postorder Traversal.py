# 145. Binary Tree Postorder Traversal

# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]

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

		self.traverse(root.left, result)
		self.traverse(root.right, result)
		result.append(root.val)

		return result

	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result = []
		if not root:
			return result

		return self.traverse(root, result)



	# Non Recursion
	def postorderTraversal(self, root):
		result = []
		if not root:
			return result

		stack = []
		while root or stack:
			# Step 1.
			# 与出栈顺序(right, left, root)相反地:
			# 先把root压入栈, 然后能往左就往左，否则向右一步
			# 循环结束时走到最深的某个left或right leaf node
			while root:
				stack.append(root)
				root = root.left if root.left else root.right

			# Step 2. 把最后进入stack的node添加到result
			root = stack.pop()
			result.append(root.val)

			# Step 3.
			# 如果当前节点是栈顶节点的左子节点, 转到其右兄弟, 重复步骤1
			# 否则退栈
			if stack and stack[-1].left == root:
				root = stack[-1].right
			else:
				root = None

		return result