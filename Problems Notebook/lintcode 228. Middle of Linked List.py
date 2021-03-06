# 228. Middle of Linked List

# Description
# Find the middle node of a linked list.
 
# Example
# Given 1->2->3, return the node with value 2.
# Given 1->2, return the node with value 1.

# Challenge:
# If the linked list is in a data stream, can you find the middle without iterating the linked list again?

"""
Definition of ListNode
class ListNode(object):

	def __init__(self, val, next=None):
		self.val = val
		self.next = next
"""
# 思路：快慢指针

class Solution:
	"""
	@param: head: the head of linked list.
	@return: a middle node of the linked list
	"""
	def middleNode(self, head):
		# write your code here
		if head is None:
			return None
		slow = head
		fast = head.next
		while fast is not None and fast.next is not None:
			slow = slow.next	# step is one
			fast = fast.next.next	# step is two

		return slow