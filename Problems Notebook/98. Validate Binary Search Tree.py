# 98. Validate Binary Search Tree

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true

# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: 
# The input is: [5,1,4,null,null,3,6]. The root node's value
# is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: 

# Traverse: 按照题目中的定义, BFS inorder遍历是升序序列(充要条件),
# 而inorder是否升序只需要判断当前node是否比其上一个node大, 不必记录遍历过得所有node

# Divide and Conquer: root.val比左子树的max大, 比右子树的min小
# recursion既返回max又返回min, 需要用到class定义ResultType

# Traverse:
class Solution:
	isValid = True
	lastNode = None	

	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		
		self.inorderTraverse(root)
		return self.isValid

	def inorderTraverse(self, root):
		if root is None:
			return

		self.inorderTraverse(root.left)
		if (self.lastNode != None and self.lastNode.val >= root.val):
			self.isValid = False
			return
		self.lastNode = root
		self.inorderTraverse(root.right)
		