# 447. Search in a Big Sorted Array

# Given a big sorted array with positive integers sorted by ascending order. 
# The array is so big so that you can not get the length of the whole array directly, 
# and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). 
# Find the first index of a target number. Your algorithm should be in O(log k), 
# where k is the first index of the target number.

# Return -1, if the number does not exist in the array.

# If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.

# Example
# Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.
# Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

# Challenge
# O(log k), k is the first index of the given target number.

class Solution:
	"""
	@param: reader: An instance of ArrayReader.
	@param: target: An integer
	@return: An integer which is the first index of target.
	"""
	def searchBigSortedArray(self, reader, target):
		
		limit = 2147483647
		
		if reader.get(0) > target:
			return -1
		if reader.get(0) == target:
			return 0
		if reader.get(1) == target:
			return 1

		idx = 2
		step = 1		
		while step >= 1:
			if reader.get(idx) == limit or reader.get(idx + 1) == limit:
				break
			elif reader.get(idx) < target:
				step = int(step * 2)
				idx = idx + step
			elif reader.get(idx) >= target:
				step = int(step / 2)
				idx = idx - step

		if reader.get(idx) == target:
			return idx
		elif reader.get(idx + 1) == target:
			return idx + 1
		elif reader.get(idx - 1) == target:
			return idx - 1
		
		return -1