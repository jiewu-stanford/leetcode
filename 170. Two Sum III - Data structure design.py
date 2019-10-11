'''
Title     : 170. Two Sum III - Data structure design ($$$)
Problem   : https://leetcode.com/problems/two-sum-iii-data-structure-design/
          : https://www.lintcode.com/problem/two-sum-iii-data-structure-design/description
'''
''' Reference: http://www.voidcn.com/article/p-qhmcmxvf-qp.html '''

class TwoSum(object):
    def __init__(self):
        self.d = {}

    def add(self, number):
        if number not in self.d:
            self.d[number] = 1
        else:
            self.d[number] += 1

    def find(self, value):
        d = self.d
        for num in d:
            if (value - num in d) and (value - num != num or d[num] > 1):   # value - num = num requires d[num] > 1
                return True
        return False