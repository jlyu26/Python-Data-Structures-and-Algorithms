# 143. Sort Colors II

# Given an array of n objects with k different colors (numbered from 1 to k), 
# sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

# Example
# Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

# Challenge
# A rather straight forward solution is a two-pass algorithm using counting sort. 
# That will cost O(k) extra memory. 
# Can you do it without using extra memory?

# 思路：
# 用partition把k分成两个k/2 (0, k/2) (k/2 + 1, k), 再把两个k/2分别分成两个k/4...
# 直到每个k/n中只有一个颜色为止
# O(nlogk)

class Solution:
	"""
	@param colors: A list of integer
	@param k: An integer
	@return: nothing
	"""
	def sortColors2(self, colors, k):
		if colors is None or len(colors) == 0:
			return
		self.rainbowSort(colors, 0, len(colors) - 1, 1, k)

	def rainbowSort(self, colors, start, end, From, To):
		if start >= end or From >= To:
			return

		# partition
		pivot = (From + To) // 2
		i = start
		for j in range (start, end + 1):
			if colors[j] <= pivot:
				colors[i], colors[j] = colors[j], colors[i]
				i += 1

		self.rainbowSort(colors, start, i - 1, From, pivot)
		self.rainbowSort(colors, i, end, pivot + 1, To)
