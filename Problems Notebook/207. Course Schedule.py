# 207. Course Schedule

# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, 
# is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: 
# There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: 
# There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
# You may assume that there are no duplicate edges in the input prerequisites.

# 思路：拓扑排序

class Solution:
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		edges = {c: [] for c in range(numCourses)}	# 需要c为先修课的课程
		degrees = [0 for c in range(numCourses)]	# 课程c需要的先修课数目

		for i, j in prerequisites:
			edges[j].append(i)	# 选i需要先修j
			degrees[i] += 1
		
		q, count = [], 0	# count: 入度(degree)为0, 即不需要先修课的课

		for i in range(numCourses):
			if degrees[i] == 0:
				q.append(i)

		while q:
			node = q.pop(0)
			count += 1

			for x in edges[node]:
				degrees[x] -= 1
				if degrees[x] == 0:
					q.append(x)

		return count == numCourses