# 127. Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, 
# find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution:
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		wordList.append(endWord)
		wordSet = set([])
		for word in wordList:
			wordSet.add(word)

		wordLen = len(beginWord)
		q = [(beginWord, 1)]

		while q:
			currWord, currLen = q.pop(0)
			if currWord == endWord:
				return currLen
			for i in range(wordLen):
				part1 = currWord[:i]
				part2 = currWord[i+1:]
				for j in 'abcdefghijklmnopqrstuvwxyz':
					if currWord[i] != j:
						nextWord  = part1 + j + part2
						if nextWord in wordSet:
							q.append((nextWord, currLen + 1))
							wordSet.remove(nextWord)

		return 0