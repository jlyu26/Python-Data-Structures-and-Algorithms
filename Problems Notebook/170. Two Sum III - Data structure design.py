# 170. Two Sum III - Data structure design

# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example
# add(1); add(3); add(5);
# find(4) // return true
# find(7) // return false

class TwoSum:
	"""
	@param: number: An integer
	@return: nothing
	"""
	List = []
	def add(self, number):
		# write your code here
		self.List.append(number)
		

	"""
	@param: value: An integer
	@return: Find if there exists any pair of numbers which sum is equal to the value.
	"""
	def find(self, value):
		# write your code here
		Hash = {}
		index = 0
		while index < len(self.List):
			diff = value - self.List[index]
			if diff in Hash:
				return True
			else:
				Hash[self.List[index]] = True
				index += 1
		return False