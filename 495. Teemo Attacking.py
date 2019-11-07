'''
Title     : 495. Teemo Attacking
Problem   : https://leetcode.com/problems/teemo-attacking/
'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            res -= max(0, duration - (timeSeries[i]-timeSeries[i-1]))
        return res