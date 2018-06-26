# 474. Lowest Common Ancestor II

# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
# The node has an extra attribute parent which point to the father of itself. The root's parent is null.

# For the following binary tree:

#   4
#  / \
# 3   7
#    / \
#   5   6

# LCA(3, 5) = 4
# LCA(5, 6) = 7
# LCA(6, 7) = 7

# 思路: 用dict存放节点A到root的path, 遍历B节点的parent, 第一个出现在set中的就是LCA

"""
Definition of ParentTreeNode:
class ParentTreeNode:
	def __init__(self, val):
		self.val = val
		self.parent, self.left, self.right = None, None, None
"""

class Solution:
	"""
	@param: root: The root of the tree
	@param: A: node in the tree
	@param: B: node in the tree
	@return: The lowest common ancestor of A and B
	"""
	def lowestCommonAncestorII(self, root, A, B):
		# write your code here
		Hash = {}
		while A:
			Hash[A] = True
			A = A.parent

		while B:
			if B in Hash:
				return B
			B = B.parent

		return root