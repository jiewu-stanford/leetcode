'''
Title     : 384. Shuffle an Array
Problem   : https://leetcode.com/problems/shuffle-an-array/
'''
''' Reference: https://leetcode.com/problems/shuffle-an-array/discuss/85957/easy-python-solution-based-on-generating-random-index-and-swapping '''
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums      

    def shuffle(self) -> List[int]:
        res = self.nums[:]
        for i in range(len(res)-1, 0, -1):
            j = random.randrange(0, i+1)
            res[i], res[j] = res[j], res[i]
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()