# 230. Kth Smallest Element in a BST

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
# How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路: BST中序遍历结果为非降序
# 暴力解: 先中序遍历记录在list里再返回list[k-1], 缺点是比如就返回1st还要遍历整个tree
# 所以可以用index记录第kth个

# Recursion
class Solution:
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		self.kth = None
		self.index = 0
		self.inorderTraverse(root, k)
		return self.kth

	def inorderTraverse(self, root, k):
		if not root:
			return

		self.inorderTraverse(root.left, k)
		self.index += 1
		if self.index == k:
			self.kth = root.val
			return
		
		self.inorderTraverse(root.right, k)



# Non-Recursion
class Solution:
	def kthSmallest(self, root, k):
		if not root:
			return -1

		index = 0
		stack = []
		curr = root

		while curr or stack:
			while curr:
				stack.append(curr)
				curr = curr.left
			
			curr = stack.pop()
			index += 1
			if index == k:
				return curr.val
			curr = curr.right

		return root.val