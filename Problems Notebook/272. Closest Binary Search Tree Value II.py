# 272. Closest Binary Search Tree Value II

# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

# Example
# Given root = {1}, target = 0.000000, k = 1, return [1].

# Challenge
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

"""
Definition of TreeNode:
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
"""

class Solution:
	"""
	@param root: the given BST
	@param target: the given target
	@param k: the given k
	@return: k values in the BST that are closest to the target
	"""
	def closestKValues(self, root, target, k):
		# write your code here
