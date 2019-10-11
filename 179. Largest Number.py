'''
Title     : 179. Largest Number
Problem   : https://leetcode.com/problems/largest-number/
'''
'''
bubble sort (https://www.youtube.com/watch?v=xli_FI7CuzA&t=2s)
Reference: https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts).
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int(''.join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

''' selection sort (https://www.youtube.com/watch?v=g-PGLbMth_g), ibid. '''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
                nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return str(int(''.join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

''' insertion sort (https://www.youtube.com/watch?v=JU767SDMDvA), ibid. '''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            pos, curr = i, nums[i]
            while pos > 0 and not self.compare(nums[pos-1], curr):
                nums[pos] = nums[pos-1]
                pos -= 1
            nums[pos] = curr
        return str(int(''.join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
'''
sort via pairwise comparison of string concatenation e.g. '2' + '11' vs. '11' + '2'
Reference: https://leetcode.com/problems/largest-number/discuss/53270/Python-simple-solution-in-4-lines
'''
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        key = functools.cmp_to_key(lambda x, y: (y+x > x+y) - (y+x < x+y))
        return str(int(''.join(sorted(map(str, nums), key=key))))   # e.g. sorted(['11','2','13']) = ['2','13','11']