# 139. Word Break

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

# 思路1: DFS + Python的字符串方法startswith()
# leetcode AC beats 100% python, lintcode超时...
class Solution:
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if not wordDict:
			return len(s) == 0

		start = 0
		stack = [start]
		visited = set()
		while stack:
			start = stack.pop()
			if start in visited:
				continue
			visited.add(start)
			for word in wordDict:
				if s[start:].startswith(word):
					step = len(word)
					if step == len(s[start:]):
						return True
					stack.append(start + step)

		return False



# 思路2: DP: 往前切(?)
class Solution:
	def wordBreak(self, s, wordDict):
		if len(wordDict) == 0:
			return len(s) == 0
		# 长度为n的string有n + 1个切割点: _a_b_c_
		n = len(s)
		# canbreak[n]: 长度为n的string是否breakable
		canbreak = [False] * (n + 1)
		canbreak[0] = True

		# maxlen: 两个可切割点之间的最大间距
		maxlen = max([len(word) for word in wordDict])
		for i in range(1, n + 1):	# i: string的所有可切割点的位置
			for j in range(1, min(i, maxlen) + 1):	# j: 往前切的str的长度, j <= maxlen and j <= i
				# 如果新切出来的str在dict中, 且截止到当前循环时长度为i - j的string已经有合法切分
				if not canbreak[i - j]:
					continue
				if s[i - j: i] in wordDict:
					canbreak[i] = True
					break

		return canbreak[n]



# 思路3: BFS求能否抵达

# 思路4: 纯DFS
class Solution:
	def wordBreak(self, s, wordDict):
		self.stringlength = len(s)
		if len(wordDict) == 0:
			return self.stringlength == 0	