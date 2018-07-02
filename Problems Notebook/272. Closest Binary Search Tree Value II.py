# 272. Closest Binary Search Tree Value II

# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

# Example
# Given root = {1}, target = 0.000000, k = 1, return [1].

# Challenge
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# 思路:
# 1. 暴力解 (Time和Space都是O(n)): 
# inorder traverse从小到大排列的list, 剩下的和Binary Search的find k closet elements一样 

# 2. 类似BST上的two pointers, Time O(k + logn), Space O(logn)
# 实现如下的子函数：
# getStack() -- 在假装插入target的时候, 看看一路走过的节点都是哪些, 放到 stack 里用于 iterate
# moveUpper(stack) -- 根据stack, 挪动到next node
# moveLower(stack) -- 根据stack, 挪动到prev node
# 有了这些函数之后，就可以把整个树当作一个数组一样来处理，只不过每次 i++ 的时候要用 moveUpper，i--的时候要用 moveLower

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
		values = []
		if k == 0 or not root:
			return values

		lowerStack = self.getStack(root, target)
		upperStack = []
		upperStack.extend(lowerStack)

		if lowerStack[-1].val > target:
			self.moveLower(lowerStack)
		else:
			self.moveUpper(upperStack)

		for i in range(k):
			if (not lowerStack) or (upperStack and target - lowerStack[-1].val > upperStack[-1].val - target):
				values.append(upperStack[-1].val)
				self.moveUpper(upperStack)
			else:
				values.append(lowerStack[-1].val)
				self.moveLower(lowerStack)

		return values
	
	def getStack(self, root, target):
		stack = []
		while root:
			stack.append(root)
			if root.val > target:
				root = root.left
			else:	# 怎么处理root.val等于target?
				root = root.right

		return stack

	def moveUpper(self, stack):
		# 如果当前node没有右兄弟
		# 它的upper就是走到该node的path中第一个左拐的点
		node = stack[-1]
		if not node.right:
			node = stack.pop()
			while stack and stack[-1].right == node:
				node = stack.pop()
			return

		# 当前node有右兄弟, 它的upper就是它的父节点
		node = node.right
		while node:
			stack.append(node)
			node = node.left

	def moveLower(self, stack):	# 是moveUpper代码的right/left镜像
		node = stack[-1]
		if not node.left:
			node = stack.pop()
			while stack and stack[-1].left == node:
				node = stack.pop()
			return

		node = node.left
		while node:
			stack.append(node)
			node = node.right