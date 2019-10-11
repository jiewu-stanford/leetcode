'''
Title     : 370. Range Addition ($$$)
Problem   : https://leetcode.com/problems/range-addition/
          : https://www.lintcode.com/problem/range-addition/description
'''
'''
update only the start and end element is sufficient (think of step-up and step-down), since elements in the middle are updated the same way
Reference: https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/range-addition.py
'''
class Solution:
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for update in updates:
            res[update[0]] += update[2]
            if update[1] + 1 < length:
                res[update[1]+1] -= update[2]
        for i in range(1, length):
            res[i] += res[i-1]
        return res

''' step-by-step for loop implementation will produce TLE '''
class Solution:
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for update in updates:
            for i in range(update[0],update[1]+1):
                res[i] += update[2]
        return res