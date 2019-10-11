'''
Title     : 127. Word Ladder
Problem   : https://leetcode.com/problems/word-ladder/description/
'''
'''
BFS solution using deque()
Reference: https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
'''
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        chars = {c for word in wordList for c in word}
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in chars:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordList:
                        wordList.remove(nextWord)   # avoid going back
                        queue.append([nextWord, step+1])
        return 0
'''
preprocess word list by creating a dictionary of all combinations of words with missing letters (can be defined as its 'neighborhood')
mapped to all words in the list that match the pattern, e.g. hot -> {'_ot': ['hot'], 'h_t': ['hot'], 'ho_': ['hot']}
in this way the random walk type search for path from beginWord to endWord becomes traversing through neighborhood overlaps hence is more efficient
Reference: https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
'''
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        l = len(beginWord)
        wordIndx = zip(range(l), range(1, l+1))
        maskDict = self.maskWord(set(wordList), wordIndx)
        return self.helper(beginWord, endWord, wordIndx, maskDict)

    def maskWord(self, wList, wIndx):
        d = collections.defaultdict(list)
        for word in wList:
            for i, j in wIndx:
                mask = word[:i] + '_' + word[j:]
                d[mask].append(word)
        return d

    def helper(self, beginW, endW, wIndx, d):
        queue = collections.deque([(beginW, 1)])
        visited = set([beginW])
        while queue:
            word, step = queue.popleft()
            for i, j in wIndx:
                mask = word[:i] + '_' + word[j:]
                neighborWords = d[mask]
                for neighborW in neighborWords:
                    if neighborW not in visited:
                        if neighborW == endW:
                            return step + 1
                        visited.add(neighborW)
                        queue.append((neighborW, step+1))
        return 0