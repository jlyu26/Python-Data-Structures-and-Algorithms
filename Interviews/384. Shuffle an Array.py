# 384. Shuffle an Array

# Shuffle a set of numbers without duplicates.

# Example:

# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

# 思路: in place swap array, 超级慢 (???)
class Solution:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		self.ori = nums[:]	# reset需要一份深拷贝

	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		:rtype: List[int]
		"""
		return self.ori

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""
		idx = 0
		while idx < len(self.nums) - 1:
			rand = random.randint(idx, len(self.nums) - 1)
			self.nums[idx], self.nums[rand] = self.nums[rand], self.nums[idx]
			idx += 1
		return self.nums

	# Python random.sample() 也很慢 (???)
	def shuffle(self):
		return random.sample(self.nums, len(self.nums))

	# 能用Algorithm R写吗?



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()