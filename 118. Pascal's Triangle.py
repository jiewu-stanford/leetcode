'''
Title     : 118. Pascal's Triangle
Problem   : https://leetcode.com/problems/pascals-triangle/
'''
''' for loop + step-by-step construction '''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lists = []
        for i in range(numRows):
            lists.append([1]*(i+1))
            if i > 1:
                for j in range(1,i):
                    lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
        return lists

''' shorter code with list comprehension '''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n, row, res = 0, [1], []
        while n < numRows:
            res.append(row)
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
            n += 1
        return res