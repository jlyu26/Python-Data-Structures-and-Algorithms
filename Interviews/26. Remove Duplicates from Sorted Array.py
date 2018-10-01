# 26. Remove Duplicates from Sorted Array (lintcode 100)

# Given a sorted array nums, 
# remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# Example:
# Given input array nums = [1,1,2],
# Your function should return length = 2, and nums is now [1,2].

class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0

		temp = nums[0]
		idx = 1
		while idx != len(nums):
			if nums[idx] == temp:
				nums.pop(idx)
			else:
				temp = nums[idx]
				idx += 1

		return len(nums)

# 碰到这种需要删除元素的数组，进行遍历时尽量用while循环，通过下标和变动数组长度的关系来控制循环结束的条件
# 尽量不要使用以下这种循环:
# for i in A:
#     if i == temp:
#         A.remove(i)
# 这种写法容易出错