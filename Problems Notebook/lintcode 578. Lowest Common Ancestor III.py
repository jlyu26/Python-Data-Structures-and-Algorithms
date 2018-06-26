# 578. Lowest Common Ancestor III

# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
# Return null if LCA does not exist.

# node A or node B may not exist in tree.

# Example
# For the following binary tree:

#   4
#  / \
# 3   7
#    / \
#   5   6

# LCA(3, 5) = 4
# LCA(5, 6) = 7
# LCA(6, 7) = 7

"""
Definition of TreeNode:
class TreeNode:
	def __init__(self, val):
		this.val = val
		this.left, this.right = None, None
"""

class Solution:
	"""
	@param: root: The root of the binary tree.
	@param: A: A TreeNode
	@param: B: A TreeNode
	@return: Return the LCA of the two nodes.
	"""
	def lowestCommonAncestor3(self, root, A, B):
		# write your code here
		a_exist, b_exist, lca = self.helper(root, A, B)
		if a_exist and b_exist:
			return lca
		else:
			return None

	def helper(self, root, A, B):
		if not root:
			return False, False, None

		# left_node, right_node: lca
		# if A and B, return root
		# else if A return A; if B return B
		# else return None
		left_A, left_B, left_node = self.helper(root.left, A, B)
		right_A, right_B, right_node = self.helper(root.right, A, B)

		a_exist = left_A or right_A or root == A
		b_exist = left_B or right_B or root == B

		if root == A or root == B:
			return a_exist, b_exist, root
		
		if left_node and right_node:
			return a_exist, b_exist, root
		if left_node:
			return a_exist, b_exist, left_node
		if right_node:
			return a_exist, b_exist, right_node
		return a_exist, b_exist, None