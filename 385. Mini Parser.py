'''
Title     : 385. Mini Parser
Problem   : https://leetcode.com/problems/mini-parser/description/
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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
'''
iterative solution using stack
Reference: https://leetcode.com/problems/mini-parser/discuss/156318/Python-O(N)-one-pass-iterative-solution
'''
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack, num, last = [], '', None
        for c in s:
            if c.isdigit() or c == '-':
                num += c
            elif c == ',' and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ''
            elif c == '[':
                elem = NestedInteger()
                if stack: stack[-1].add(elem)
                stack.append(elem)
            elif c == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                last = stack.pop()   # for the last ], it is possible that there is only one NestedInteger
        return last if last else NestedInteger(int(num))
'''
recursive solution, use number of brackets to check balance of brackets to identify the nested integer
Reference: https://leetcode.com/problems/mini-parser/discuss/86221/Easy-Python-recursive-solution-and-stack-solution-please-be-careful-about-time-complexity
'''
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        nested = NestedInteger()
        numbracket, startindex = 0, 1
        for i in range(1, len(s)):
            if (numbracket == 0 and s[i] == ',') or i == len(s)-1:
                if startindex < i:
                    nested.add(self.deserialize(s[startindex:i]))
                startindex = i + 1
            elif s[i] == '[':
                numbracket += 1
            elif s[i] == ']':
                numbracket -= 1
        return nested