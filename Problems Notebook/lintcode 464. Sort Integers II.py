# 464. Sort Integers II

# Given an integer array, sort it in ascending order. 
# Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

# Example
# Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

# 用quick sort (双指针partition类)
# 先选一个数为pivot, <=放左边, >=放右边
# 注意=的要尽量左右均分,否则容易出现最坏情况
# 怎么recursion ??

class Solution:
	"""
	@param A: an integer array
	@return: nothing
	"""
	def sortIntegers2(self, A):
		# write your code here
		self.quicksort(A, 0, len(A) - 1)

	def quicksort(self, A, start, end):
		if start >= end: # 结束递归判断
			return

		left, right = start, end
		# 要点1：pivot是value, 不是index
		pivot = A[(start + end) // 2]

		# 要点2：left <= right, 而不是left < right
		while left <= right:
			while left <= right and A[left] < pivot:	# 为什么要在内循环中加入left <= right ???
				left += 1
			while left <= right and A[right] > pivot:
				right -= 1

			if left <= right:
				A[left], A[right] = A[right], A[left]

				left += 1
				right -= 1

		self.quicksort(A, start, right)	# 结束while循环时left > right
		self.quicksort(A, left, end)