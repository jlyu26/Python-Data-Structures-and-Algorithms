# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# LCA: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that 
# has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: 
# The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.

# 思路: Divide and Conquer
# 在以root为根的左右子树分别找LCA
# p, q分别位于左右返回root, 否则返回找到结果的一边, 都没有返回None
# Follow up: 如果p或q可能不存在? (lintcode 578)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		if root is None or root == p or root == q:
			return root

		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)
		
		if left and right:
			return root
		if left:
			return left
		if right:
			return right
		return None