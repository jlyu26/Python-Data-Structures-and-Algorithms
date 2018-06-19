# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence 
# of bits so that it can be stored in a file or memory buffer, or transmitted across a 
# network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and this string 
# can be deserialized to the original tree structure.

# Example: 

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"

# Clarification: The above format is the same as how LeetCode serializes a binary tree. 
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. 
# Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		if root is None:
			return '{}'
		
		q = [root]
		result = []

		while q:
			node = q.pop(0)
			result.append(node)

			if node != None:
				q.append(node.left)
				q.append(node.right)
		
		s = ''
		for x in range(len(result)):
			s += '#' if result[x] is None else str(result[x].val)
			if x != len(result) - 1:
				s += ','

		return '{' + s + '}'

		

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		if data == '{}':
			return None

		data = data[1:-1].split(',')
		root = TreeNode(data[0])
		q = []	# 保存所有deseialized的node
		q.append(root)
		
		idx = 0
		is_left = True
		for i in range(1, len(data)):   # 注意range从1开始, 因为已经deserialize了一个root
			if data[i] != '#':
				node = TreeNode(data[i])
				if is_left:	# q[idx] 上一个刚刚deserialized的node
					q[idx].left = node
				else:
					q[idx].right = node
				q.append(node)
			if is_left == False:	# 如果q[idx]已经有了右子节点, 就处理下一个node
				idx += 1
			is_left = not is_left # 每读一个node变换一次左/右

		return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))