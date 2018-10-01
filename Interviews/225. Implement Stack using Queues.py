# 225. Implement Stack using Queues

# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false

# You may assume that all operations are valid 
# (for example, no pop or top operations will be called on an empty stack).

# 思路1:
# q1, q2
# pop: 把前面的都move到另一个empty queue里, pop仅剩的一个
# top: ..., return最后一个
# push: 有不empty的push到里面, 两个queue都empty随便push一个
# 有一个queue始终是empty的 (which one?)

class MyStack:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.q1, self.q2 = [], []
		self.size = 0

	def emptyQ(self):	# return empty queue
		if self.q1:
			return self.q2
		else:
			return self.q1

	def push(self, x):
		"""
		Push element x onto stack.
		:type x: int
		:rtype: void
		"""
		if self.q1 is self.emptyQ():
			self.q2.append(x)
		else:
			self.q1.append(x)
		self.size += 1		

	def pop(self):
		"""
		Removes the element on top of the stack and returns that element.
		:rtype: int
		"""
		if self.q1 is self.emptyQ():
			for i in range(0, self.size - 1):
				self.q1.append(self.q2.pop(0))
				i += 1
			self.size = 0
			return self.q2.pop()
		else:
			for i in range(0, self.size - 1):
				self.q2.append(self.q1.pop(0))
				i += 1
			self.size = 0
			return self.q1.pop()

	def top(self):
		"""
		Get the top element.
		:rtype: int
		"""
		if self.q1 is self.emptyQ():
			return self.q2[-1]
		else:
			return self.q1[-1]


	def empty(self):
		"""
		Returns whether the stack is empty.
		:rtype: bool
		"""
		return not (self.q1 or self.q2)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()