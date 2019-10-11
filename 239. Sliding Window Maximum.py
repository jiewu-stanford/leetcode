'''
Title     : 239. Sliding Window Maximum
Problem   : https://leetcode.com/problems/sliding-window-maximum/
'''
''' use deque() type for sliding window problems, because it offers the convenience of popleft() '''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        win, slidingmax = deque(), []
        for i in range(len(nums)):
            while win and nums[win[-1]] < nums[i]:
                win.pop()   # discard ALL (by while loop) that is smaller than nums[i]
            win.append(i)
            if win and i - k >= win[0]:
                win.popleft()
            if i - k >= -1:
                slidingmax.append(nums[win[0]])
        return slidingmax