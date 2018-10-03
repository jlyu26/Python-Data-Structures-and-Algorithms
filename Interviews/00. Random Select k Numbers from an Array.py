# Random Select k Numbers from an Array

# 是给个n个数的array数组, 随机挑出k个数
# 不能用除array之外的数据结构

# 思路1：允许改动当前数组 
class Solution:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums

	def pick(self, k):	# ???
		"""
		:type k: int
		:rtype: List[int]
		"""
		for i in range(0, k):
			randIdx = random.randint(i, len(nums))
			self.nums[i], self.nums[randIdx] = self.nums[randIdx], self.nums[i]
			i += 1
		return self.nums[:k]

# 思路2: 不允许改变当前数组