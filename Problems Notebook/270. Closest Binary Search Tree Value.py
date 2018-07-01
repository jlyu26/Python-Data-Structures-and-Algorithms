# 270. Closest Binary Search Tree Value

# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# Example
# Given root = {1}, target = 4.428571, return 1.

# 思路: 分别用upperBound() lowerBound()求出比target大的最小值和比target小的最大值
# 然后两者比较一下返回diff更小的
# 注意root.val等于target的情况, 因为BST中等于放在左子树, 所以分成<=和>

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
	@return: the value in the BST that is closest to the target
	"""
	def closestValue(self, root, target):
		# write your code here
		if not root:
			return 0

		self.lowerNode = self.lowerBound(root, target)
		self.upperNode = self.upperBound(root, target)

		if not self.lowerNode:
			return self.upperNode.val

		if not self.upperNode:
			return self.lowerNode.val

		if target - self.lowerNode.val > self.upperNode.val - target:
			return self.upperNode.val

		return self.lowerNode.val

	def lowerBound(self, root, target):
		if not root:
			return None

		if target <= root.val:
			return self.lowerBound(root.left, target)

		# target > root.val
		self.lowerNode = self.lowerBound(root.right, target)

		if self.lowerNode:
			return self.lowerNode

		return root

	def upperBound(self, root, target):
		if not root:
			return None

		if target > root.val:
			return self.upperBound(root.right, target)

		# target <= root.val
		self.upperNode = self.upperBound(root.left, target)

		if self.upperNode:
			return self.upperNode

		return root