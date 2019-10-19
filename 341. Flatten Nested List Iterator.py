'''
Title     : 341. Flatten Nested List Iterator
Problem   : https://leetcode.com/problems/flatten-nested-list-iterator/
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
''' Reference: https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80142/8-line-Python-Solution '''
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            prev = self.stack[-1]
            if prev.isInteger():
                return True
            else:
                self.stack = self.stack[:-1] + prev.getList()[::-1]
        return False
'''
flattern list all at once instead of on the fly
Reference: https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80387/Python-Solution-132-ms
'''
import collections
class NestedIterator(object):
    def __init__(self, nestedList):
        self.queue = collections.deque([])
        for lst in nestedList:
            if lst.isInteger():
                self.queue.append(lst.getInteger())
            else:
                newlst = NestedIterator(lst.getList())
                while newlst.hasNext():
                    self.queue.append(newlst.next())

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return self.queue