# 658. Find K Closest Elements

# Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
# The result should also be sorted in ascending order. 
# If there is a tie, the smaller elements are always preferred.

# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]

# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]

# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104

# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers). 
# Please reload the code definition to get the latest changes.

class Solution:
	def findClosestElements(self, arr, k, x):
		"""
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""
		if k == len(arr):
			# print(f"result: {arr}")
			return arr

		# find target/nearest number's index in arr
		idx = 0
		start = 0
		end = len(arr) - 1

		while start + 1 < end:
			mid = start + (end - start) // 2
			if arr[mid] == x:
				end = mid	# smaller prefered
			elif arr[mid] < x:
				start = mid
			elif arr[mid] > x:
				end = mid

		if abs(arr[start] - x) <= abs(arr[end] - x):
			idx = start
		elif abs(arr[start] - x) > abs(arr[end] - x):
			idx = end

		# print(f"idx: {idx}")

		# find nearest k numbers
		result = [arr[idx]]
		length = 1
		left = idx - 1
		right = idx + 1

		while left >= 0 and right < len(arr) and length < k:
			if abs(arr[left] - x) <= abs(arr[right] - x):
				result.append(arr[left])
				length += 1
				left -= 1
			elif abs(arr[left] - x) > abs(arr[right] - x):
				result.append(arr[right])
				length += 1
				right += 1

		rest = []
		if left < 0 and length < k:
			rest = arr[right: right + (k - length)]
		elif right >= len(arr) - 1 and length < k:
			rest = arr[left + 1 - (k - length): left + 1]

		result.extend(rest)
		result.sort()

		# print(f"result: {result}")
		return result