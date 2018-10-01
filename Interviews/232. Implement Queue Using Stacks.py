# 232. Implement Queue Using Stacks.py

# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

# Example:

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false

# You may assume that all operations are valid 
# (for example, no pop or peek operations will be called on an empty queue).

# 思路1:
# inStack, outStack
# push: 都往inStack里压
# pop：1. while outStack: pop outStack; 2. move inStack到outStack; 3. pop outStack
# peek: 1. while outStack: outStack[-1]; 2. move inStack到outStack; 3. outStack[-1]
# Time:

class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.inStack, self.outStack = [], []

	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: void
		"""
		self.inStack.append(x)

	def pop(self):
		"""
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		if self.outStack:
			return self.outStack.pop()
		else:
			self.move()
			return self.outStack.pop()

	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		if self.outStack:
			return self.outStack[-1]
		else:
			self.move()
			return self.outStack[-1]

	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return not (self.inStack or self.outStack)

	def move(self):
		while self.inStack:
			self.outStack.append(self.inStack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()