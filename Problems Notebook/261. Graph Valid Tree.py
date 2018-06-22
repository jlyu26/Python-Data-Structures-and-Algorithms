# 261. Graph Valid Tree

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# 思路: 无向图

class Solution:
	"""
	@param n: An integer
	@param edges: a list of undirected edges
	@return: true if it's a valid tree, or false
	"""
	def validTree(self, n, edges):
		# write your code here
		if len(edges) != n - 1:
			return False

		from collections import defaultdict	# 用defaultdict方便初始化
		neighbors = collections.defaultdict(list)
		for u, v in edges:
			neighbors[u].append(v)
			neighbors[v].append(u)

		# 从0开始尝试访问所有node, 因为有visited记录，每个点都只进入q一次
		# 如果tree种有环的话会有node尝试多次进入q, 造成len(visited) < n (有node没有任何edge相连所以visit不到)
		visited = {}
		q = [0]

		visited[0] = True
		while q:
			cur = q.pop(0)
			visited[cur] = True
			for node in neighbors[cur]:
				if node not in visited:
					visited[node] = True
					q.append(node)

		return len(visited) == n