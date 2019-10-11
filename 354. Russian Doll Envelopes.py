'''
Title     : 354. Russian Doll Envelopes
Problem   : https://leetcode.com/problems/russian-doll-envelopes/description/
'''
'''
sort in ascending order of width to remove restriction on width, but descending order of height for the same width (since you can use only one of them)
then apply the 300. solution to heights since the length of the longest increasing subsequence in height = max number of rolled envelopes
Reference: https://leetcode.com/problems/russian-doll-envelopes/discuss/183277/Python-6-lines-bisect-solution
'''
import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        heights = []
        for w, h in sorted(envelopes, key=lambda x: (x[0],-x[1])):
            indx = bisect.bisect_left(heights, h)
            if indx == len(heights):
                heights.append(h)
            else:
                heights[indx] = h   # replace instead of insert, the same idea as in the 300. solution
        return len(heights)