# 398. Random Pick Index

# Given an array of integers with possible duplicates, randomly output the index of a given target number. 
# You can assume that the given target number must exist in the array.

# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.

# Example:
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);

# pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);

# pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);

# 需要return index所以不能变nums
# print k个numbers in order也不能改变nums
# 思路: Reservoir Sampling ??? How???
class Solution:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums

	def pick(self, target):	# ???
		"""
		:type target: int
		:rtype: int
		"""
		result = -1
		count = 0
		for i in range(0, len(self.nums)):
			if self.nums[i] == target:
				if random.randint(0, count) == 0:
					result = i
				count += 1
		return result


# 如果要求不能用除Array之外的数据结构就不行, 而且特别慢
class Solution:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.Hash = {}
		for i in range(0, len(nums)):
			if nums[i] in self.Hash:
				self.Hash[nums[i]].append(i)
			else:
				self.Hash[nums[i]] = [i]

	def pick(self, target):
		"""
		:type target: int
		:rtype: int
		"""
		idx = random.randint(0, len(self.Hash[target]) - 1)
		return self.Hash[target][idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)