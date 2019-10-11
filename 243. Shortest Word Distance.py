'''
Title     : 243. Shortest Word Distance ($$$)
Problem   : https://leetcode.com/problems/shortest-word-distance/
          : https://www.lintcode.com/problem/shortest-word-distance/description
'''
''' Reference: http://www.voidcn.com/article/p-epmviyav-qp.html '''
class Solution:
    def shortestDistance(self, words, word1, word2):
        w1 = [i for i in range(len(words)) if words[i]==word1]
        w2 = [i for i in range(len(words)) if words[i]==word2]
        return min([abs(i - j) for i in w1 for j in w2])