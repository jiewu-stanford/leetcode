'''
Title     : 223. Rectangle Area （XXX)
Problem   : https://leetcode.com/problems/rectangle-area/description/
'''
''' Reference: https://leetcode.com/problems/rectangle-area/discuss/62139/Python-concise-solution '''
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        A1 = abs(C - A) * abs(B - D)
        A2 = abs(G - E) * abs(H - F)
        w = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)
        if w <= 0 or h <= 0: return A1 + A2
        else: return A1 + A2 - w*h