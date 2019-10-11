'''
Title     : 339. Nested List Weight Sum ($$$)
Problem   : https://leetcode.com/problems/nested-list-weight-sum/
          : https://www.lintcode.com/problem/nested-list-weight-sum/description
'''
'''
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
'''
class NestedInteger(object):
    def isInteger(self): pass
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self): pass
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self): pass
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
'''
straightforward step-by-step implemented BFS iterative solution
Reference: https://blog.csdn.net/danspace1/article/details/87645153
'''
class Solution(object):
    def depthSum(self, nestedList):
        depth, res = 1, 0
        while nestedList:
            res += depth * sum([i.getInteger() for i in nestedList if i.isInteger()])
            tmp = []
            for i in nestedList:
                if not i.isInteger(): tmp += i.getList()
            nestedList = tmp
            depth += 1
        return res