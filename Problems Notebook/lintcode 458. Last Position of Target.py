# 458. Last Position of Target
# Find the last position of a target number in a sorted array. Return -1 if target does not exist.

# Example
# Given [1, 2, 2, 4, 5, 5].
# For target = 2, return 2.
# For target = 5, return 5.
# For target = 6, return -1.

###########################################################################################################

# 思路: while循环的目的不是为了直接找到答案
# 而是不断缩小区间, 缩小到能通过两个if语句判断
# 在退出时的start和end一定有一个是答案

class Solution:
	"""
	@param nums: An integer array sorted in ascending order
	@param target: An integer
	@return: An integer
	"""
	def lastPosition(self, nums, target):
		if not nums or target is None:
			return -1
		
		start = 0
		end = len(nums) - 1
		
		# 要点1: start + 1 < end
		# 循环退出时start = end 或start + 1 = end 避免死循环
		while start + 1 < end:
			# 要点2：start + (end - start) / 2 避免溢出
			mid = start + (end - start) // 2
			
			# 要点3：=, <, > 分开讨论, mid 不+1也不-1
			# 因为while循环一定会退出
			if nums[mid] > target:
				end = mid
			elif nums[mid] < target:
				start = mid
			else:	# return LAST position, 如果随便什么位置直接return
				start = mid

		# 判断start和end哪个是想要的
		# 本题要求last position 所以先判断end
		if nums[end] == target:
			return end
		if nums[start] == target:
			return start

		return -1