'''
Title     : 364. Nested List Weight Sum II ($$$)
Problem   : https://leetcode.com/problems/nested-list-weight-sum-ii/
          : https://www.lintcode.com/problem/nested-list-weight-sum-ii/description
'''
'''
recursive helper function
Reference: https://github.com/criszhou/LeetCode-Python/blob/master/364.%20Nested%20List%20Weight%20Sum%20II.py
'''
class Solution(object):
    def depthSumInverse(self, nestedList):
        levelSums = []
        self.helper(nestedList, 0, levelSums)
        return sum((level+1)*summ for level, summ in enumerate(reversed(levelSums)))

    def helper(self, nestedList, currLevel, levelSums):
        for i in nestedList:
            if i.isInteger():
                while currLevel >= len(levelSums):
                    levelSums.append(0)
                levelSums[currLevel] += i.getInteger()
            else:
                self.helper(i.getList(), currLevel+1, levelSums)