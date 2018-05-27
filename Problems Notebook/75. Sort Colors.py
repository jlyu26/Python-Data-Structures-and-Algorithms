# 75. Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that objects 
# of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort. 
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total 
# number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

# 如果可以两次遍历, 先用partition把0和12分开, 再在右边把1和2分开
# 如果只能1次遍历就用3指针, 中间的指针遍历, 0丢到start前面, 2丢到end后面, 1跳过

class Solution:
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if not nums or len(nums) == 0:
			return
		
		
		# start前面全是0
		# end后面全是2
		start = 0
		i = 0
		end = len(nums) - 1

		while i <= end:
			if nums[i] == 0:
				nums[i], nums[start] = nums[start], nums[i]
				start += 1
				i += 1
			elif nums[i] == 1:
				i += 1
			else:
				nums[i], nums[end] = nums[end], nums[i]
				end -= 1
				# 因为有可能把0换给i需要重新判断, 所以i不自增