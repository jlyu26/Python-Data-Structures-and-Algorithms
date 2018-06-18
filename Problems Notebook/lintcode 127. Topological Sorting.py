# 127. Topological Sorting

# Given an directed graph, a topological order of the graph nodes is defined as follow:

# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.

# You can assume that there is at least one topological order in the graph.

# 算法流程:
# 拓扑排序的算法是典型的宽度优先搜索算法,

# 统计所有点的入度, 并初始化拓扑序列为空;
# 将所有入度为 0 的点, 也就是那些没有任何依赖的点, 放到宽度优先搜索的队列中, 将队列中的点一个一个的释放出来, 
# 放到拓扑序列中, 每次释放出某个点 A 的时候, 就访问 A 的相邻点 (所有A指向的点), 并把这些点的入度减去 1;
# 如果发现某个点的入度被减去 1 之后变成了 0, 则放入队列中;
# 直到队列为空时, 算法结束

# 注意Python的queue模块是block queue, 如果empty时去pop会造成线程阻塞
# 所以写bfs应该用list (OJ用list比queue.Queue快很多)
# 但list的pop操作效率较低, 工程中用collections.deque效率最好

# e.g. test data:
# {0,1,2,3,4#1,3,4#2,1,4#3,4#4}

"""
Definition for a Directed graph node
class DirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []
"""

class Solution:
	"""
	@param: graph: A list of Directed graph node
	@return: Any topological order for the given graph.
	"""
	def topSort(self, graph):
		
		# define indegree with dict
		indegree = dict((i, 0) for i in graph)
		for i in graph:
			for j in i.neighbors:
				indegree[j] += 1

		# define queue and initalize with 0 indegree nodes
		q = []
		for i in graph:
			if indegree[i] == 0:
				q.append(i)

		# result and bfs
		result = []
		while q:
			node = q.pop(0)
			result.append(node)
			for j in node.neighbors:
				indegree[j] -= 1
				if indegree[j] == 0:
					q.append(j)

		return result