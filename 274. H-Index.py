'''
Title     : 274. H-Index
Problem   : https://leetcode.com/problems/h-index/
'''
'''
clever use of enumerate() to output index list, then compare based on the definition of H-index
Reference: https://leetcode.com/problems/h-index/discuss/71055/1-line-Python-solution
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))