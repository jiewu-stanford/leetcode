'''
Title     : 398. Random Pick Index
Problem   : https://leetcode.com/problems/random-pick-index/
'''
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        return random.choice([k for k, v in enumerate(self.nums) if v == target])
'''
same but use randomint() and by reservior sampling definition
Definition: https://leetcode.com/problems/linked-list-random-node/discuss/85659/brief-explanation-for-reservoir-sampling
Reference: https://leetcode.com/problems/random-pick-index/discuss/211622/Python-solution
'''
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        for k, v in enumerate(self.nums):
            if v == target:
                num = random.randint(0, count)
                if num == 0:
                    res = k
                count += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)