# 257. Binary Tree Paths

# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	
	# Divide Conquer
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		paths = []
		if not root:
			return paths

		left_path = self.binaryTreePaths(root.left)
		right_path = self.binaryTreePaths(root.right)
		
		for node in left_path:
			paths.append(str(root.val) + '->' + path)
		for node in right_path:
			paths.append(str(root.val) + '->' + path)

		if root.left is None and root.right is None:	# 该root是叶子节点
			paths.append(str(root.val))

		return paths