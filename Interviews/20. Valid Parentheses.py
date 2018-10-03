# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Input: "()"
# Output: true

# Input: "()[]{}"
# Output: true

# Input: "(]"
# Output: false

# Input: "([)]"
# Output: false

# Input: "{[]}"
# Output: true

# Input: "([)]"
# Output: false

# 思路1: 模拟堆栈, 读到左括号压栈, 读到右括号判断栈顶括号是否匹配
class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		for x in s:
			if x == '{' or x == '[' or x == '(':	# 左括号压栈
				stack.append(x)
			else:
				if not stack:
					return False
				if (x == ']' and stack[-1] != '[') or (x == ')' and stack[-1] != '(') or (x == '}' and stack[-1] != '{'):
					return False
				# 匹配: 弹栈
				stack.pop()
		# 都弹出来了就True, 还有剩下的就False
		return not stack

# 思路1不写长判断版:
class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		dict = {"]":"[", "}":"{", ")":"("}
		for x in s:
			if x in dict.values():	# 左括号压栈
				stack.append(x)
			elif x in dict.keys():
				if stack == [] or dict[x] != stack.pop():
					return False
		
		return stack == []


# 思路2: python的replace() -- 特别慢! 时间复杂度是???
# valid的string中一定有子字符串'()'或'[]'或'{}'
# 替换掉()[]{}最后string为空就true, 否则false
class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		while '()' in s or '[]' in s or '{}' in s:
			s = s.replace('()','').replace('[]','').replace('{}','')

		if s == '':
			return True
		else:
			return False