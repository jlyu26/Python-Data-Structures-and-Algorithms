# 133. Clone Graph

# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

# OJ's undirected graph serialization:
# Nodes are labeled uniquely.

# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.

# The graph has a total of three nodes, and therefore contains three parts as separated by #.

# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:

# 	     1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# 用3个步骤：

# 1. 从1个点找到所有点
# 2. 复制所有的点
# 3. 复制所有的边

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node

	# use bfs to traverse the graph and get all nodes
	# 从一个node开始，把neighbor逐一加到result里从而找到所有node
	# set: A set is an unordered collection with **no duplicate** elements
	def getNodes(self, node):
		q = [node]
		result = set([node])
		while q:
			head = q.pop(0)
			for neighbor in head.neighbors:
				if neighbor not in result:
					result.add(neighbor)
					q.append(neighbor)
		return result

	def cloneGraph(self, node):
		
		root = node
		if node is None:
			return node

		# copy nodes, store the old->new mapping information in a hash map
		# 因为如果只有label的话, 在第三部复制边的时候并不知道该把哪两个node连接起来
		nodes = self.getNodes(node)

		mapping = {}
		for node in nodes:
			mapping[node] = UndirectedGraphNode(node.label)

		# copy neighbors
		for node in nodes:
			new_node = mapping[node]
			for neighbor in node.neighbors:
				new_neighbor = mapping[neighbor]
				new_node.neighbors.append(new_neighbor)

		return mapping[root]