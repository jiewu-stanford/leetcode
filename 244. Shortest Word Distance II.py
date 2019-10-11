'''
Title     : 244. Shortest Word Distance II ($$$)
Problem   : https://leetcode.com/problems/shortest-word-distance-ii/
'''
from collections import defaultdict
class WordDistance:
    def __init__(self, words):
        self.locations = defaultdict(list)
        for i, word in enumerate(words):   # a dictionary keeping all locations of a word to save time for multiple calls
            self.locations[word].append(i)
    
    def shortest(self, word1, word2):
        loc1, loc2 = self.locations[word1], self.locations[word2]
        i1, i2 = 0, 0
        minDiff = float('inf')
        while i1 < len(loc1) and i2 < len(loc2):
            minDiff = min(minDiff, abs(loc1[i1] - loc2[i2]))
            if loc1[i1] < loc2[i2]: i1 += 1
            else: i2 += 1
        return minDiff