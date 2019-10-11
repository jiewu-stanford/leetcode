'''
Title     : 245. Shortest Word Distance III ($$$) (XXX)
Problem   : https://leetcode.com/problems/shortest-word-distance-iii/
'''
''' slight modification from 243. solution to account for word1 = word2 case '''
class Solution:
    def shortestDistance(self, words, word1, word2):
        w1 = [i for i in range(len(words)) if words[i]==word1]
        w2 = [i for i in range(len(words)) if words[i]==word2]
        return min(set([abs(i - j) for i in w1 for j in w2]) - set(0))

''' use dict() instead of list comprehension '''
class Solution:
    def shortestDistance(self, words, word1, word2):
        locations = {}
        for i, word in enumerate(words):
            if word not in locations:
                locations[word] = [i]
            else:
                locations[word] += i
        return min(set(abs(i - j) for i in locations[word1] for j in locations[word2]) - set(0))