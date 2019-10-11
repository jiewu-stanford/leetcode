'''
Title     : 281. Zigzag Iterator ($$$)
Problem   : https://leetcode.com/problems/zigzag-iterator/
          : https://www.lintcode.com/problem/zigzag-iterator/description
'''
''' Reference: https://github.com/criszhou/LeetCode-Python/blob/master/281.%20Zigzag%20Iterator.py '''

class ZigzagIterator:
    def __init__(self, v1, v2):
        if len(v1) == 0: v1, v2 = v2, v1
        self.currVec = v1
        self.nextVec = v2
        self.currIndx = 0
        self.nextIndx = 0

    def next(self):
        res = self.currVec[self.currIndx]
        self.currIndx += 1
        if self.nextIndx < len(self.nextVec):
            self.currVec, self.nextVec = self.nextVec, self.currVec
            self.currIndx, self.nextIndx = self.nextIndx, self.currIndx
        return res

    def hasNext(self):
        return self.currIndx < len(self.currVec)

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result