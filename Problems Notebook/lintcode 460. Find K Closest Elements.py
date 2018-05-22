# 460. Find K Closest Elements

# Given a target number, a non-negative integer target and an integer array A sorted in ascending order, 
# find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
# Otherwise, sorted in ascending order by number if the difference is same.


# Example
# Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].
# Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

# Challenge
# O(logn + k) time complexity.

class Solution:
	"""
	@param A: an integer array
	@param target: An integer
	@param k: An integer
	@return: an integer array
	"""
	def kClosestNumbers(self, A, target, k):

		if k == 0:
			return []

		# find target/hearest number's index in A
		idx = 0
		def findIndex(A, target, k):

			start = 0
			end = len(A) - 1
			idx = 0
			exist = False

			# 循环退出时找到target或者和target最接近的数的idx
			# logN
			while start + 1 < end:
				mid = start + (end - start) // 2
				if target == A[mid]:
					idx = mid
					exist = True
					break
				elif target < A[mid]:
					end = mid
				elif target > A[mid]:
					start = mid

			if exist is False:
				if abs(A[start] - target) <= abs(A[end] - target):
					idx = start
				if abs(A[start] - target) > abs(A[end] - target):
					idx = end

			return idx

		idx = findIndex(A, target, k)

		# print(f"idx: {idx}")
		
		# find nearest k numbers
		result = []
		def findNums(idx, A, k):
			result = [A[idx]]
			length = 1
			left = idx - 1
			right = idx + 1

			while left >= 0 and right < len(A) and length < k:
				if abs(A[left] - target) <= abs(A[right] - target):
					result.append(A[left])
					length += 1
					left -= 1
				elif abs(A[right] - target) < abs(A[left] - target):
					result.append(A[right])
					length += 1
					right += 1

			rest = []
			if left < 0 and length < k:
				rest = A[right:right + (k - length)]
			elif right >= len(A) and length < k:
				rest = A[left + 1 - (k - length):left + 1]
				rest = rest[::-1]

			result.extend(rest)
			# print(f"result: {result}")
			
			return result

		result = findNums(idx, A, k)
		return result