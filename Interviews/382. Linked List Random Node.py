# 382. Linked List Random Node

# Given a singly linked list, return a random node's value from the linked list. 
# Each node must have the same probability of being chosen.

# Follow up:
# What if the linked list is extremely large and its length is unknown to you? 
# Could you solve this efficiently without using extra space?

# Example:

# Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);

# getRandom() should return either 1, 2, or 3 randomly. 
# Each element should have equal probability of returning.
# solution.getRandom();

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 下面这种写法有的跑过有的跑不过, why???
class Solution:

	def __init__(self, head):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		:type head: ListNode
		"""
		self.count = 0
		self.node = head
		while self.node:
			self.count += 1
			self.node = self.node.next
		self.node = head

	def getRandom(self):
		"""
		Returns a random node's value.
		:rtype: int
		"""
		rand = random.randint(1, self.count)
		while rand > 1:
			self.node = self.node.next
			rand -= 1
		return self.node.val # AttributeError: 'NoneType' object has no attribute 'val'


# 思路同398 ???
class Solution:

	def __init__(self, head):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		:type head: ListNode
		"""
		self.head = head

	def getRandom(self):
		"""
		Returns a random node's value.
		:rtype: int
		"""
		result, node, index = self.head, self.head.next, 1
		while node:
			if random.randint(0, index) == 0:
				result = node
			node = node.next
			index += 1
		return result.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()