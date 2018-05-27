# 215. Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# 先用quick sort排序的话时间复杂度O(nlogn)
# 如果不允许排序：
# 未排序数组第k大/小的数/中位数：quick select
# quick select用python在OJ里会RecursionError: maximum recursion depth exceeded in comparison

class Solution:
	# @param k & A a integer and an array
	# @return ans a integer
	def findKthLargest(self, nums, k):
		length = len(nums)
		
		def partitionHelper(start, end):
			p, q = start + 1, end
			while p <= q:
				# 把nums[start]立为flag, 大的丢到p前面, <=丢到后面
				if (nums[p] > nums[start]):
					p += 1
				else:
					nums[p], nums[q] = nums[q], nums[p]
					q -= 1
			
			nums[start], nums[q] = nums[q], nums[start]
			# 退出循环时p > q, nums[q]是第q + 1大的数
			
			m = q
			if m + 1 == k:
				return nums[m]
			elif m + 1 < k:
				return partitionHelper(m + 1, end)
			else:
				return partitionHelper(start, m - 1)

		return partitionHelper(0, length - 1)