'''
Title     : 126. Word Ladder II
Problem   : https://leetcode.com/problems/word-ladder-ii/description/
'''
'''
first use BFS to build a search tree from beginWord to endWord, then use DFS to backtracking along the search tree to produce ALL shortest paths
Reference: https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-directional-BFS
note that BFS produces shortest path in a graph if (1) there are no loops (2) all edges have the same weight or no weight
Reference: https://stackoverflow.com/questions/8379785/how-does-a-breadth-first-search-work-when-looking-for-shortest-path
'''
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):        
        if endWord not in wordList: return []
        neighborhood, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        found, seq, newseq = False, {beginWord}, set()
        while seq and not found:
            words -= seq
            for word in seq:
                for w in [word[:i]+c+word[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if w in words:
                        if w == endWord:
                            found = True
                        else:
                            newseq.add(w)
                        neighborhood[word].add(w)
            seq, newseq = newseq, set()
        return self.helper(beginWord, endWord, neighborhood)

    def helper(self, word, endW, neighbors):   # recursive DFS generating ALL shortest paths
        return [[word]] if word == endW else [[word] + rest for w in neighbors[word] for rest in self.helper(w, endW, neighbors)]

''' use bidireactional (from both beginWord and endWord) BFS to speed up the search tree construction, ibid. '''
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList: return []
        neighborhood, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        found, endfound, seq, endseq, newseq = False, False, {beginWord}, {endWord}, set()
        while seq and not found:
            words -= seq
            for word in seq:
                for w in [word[:i]+c+word[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if w in words:
                        if w in endseq:   # if w == endWord:
                            found = True
                        else:
                            newseq.add(w)
                        neighborhood[word].add(w) if not endfound else neighborhood[w].add(word)
            seq, newseq = newseq, set()
            if len(seq) > len(endseq):   # swap to work on the direction that needs more progress---'bidirectional'
                seq, endseq = endseq, seq
                endfound = not endfound
        return self.helper(beginWord, endWord, neighborhood)
    
    def helper(self, word, endW, neighbors):
        return [[word]] if word == endW else [[word]+rest for w in neighbors[word] for rest in self.helper(w, endW, neighbors)]
'''
iterative solution recording paths during BFS instead of DFS construction after BFS completion
Reference: https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
'''
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList: return []
        words, seq = set(wordList), {}
        seq[beginWord] = [[beginWord]]  # key = destination, val = all paths to the destination
        while seq:
            newseq = collections.defaultdict(list)
            for word in seq:
                if word == endWord:
                    return seq[word]
                else:
                    for w in [word[:i]+c+word[i+1:] for i in range(len(word)) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                        if w in words:
                            newseq[w] += [path + [w] for path in seq[word]]
            words -= set(newseq.keys())
            seq = newseq