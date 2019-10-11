'''
Title     : 45. Jump Game II
Problem   : https://leetcode.com/problems/jump-game-ii/
'''
'''
use two pointers to record the starting position (start) and the furthest reachable position (end)
Reference: https://leetcode.com/problems/jump-game-ii/discuss/18019/10-lines-C%2B%2B-(16ms)-Python-BFS-Solutions-with-Explanations
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, nsteps = len(nums), 0, 0, 0
        while end < n - 1:
            nsteps += 1
            start, end = end, max([i+nums[i] for i in range(start,end+1)])   # range(start,end+1) is the positions within reach from current position
        return nsteps