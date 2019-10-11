'''
Title     : 358. Rearrange String k Distance Apart ($$$)
Problem   : https://leetcode.com/problems/rearrange-string-k-distance-apart/
'''
''' Reference: https://blog.csdn.net/fuxuemingzhu/article/details/83039098 '''
''' Reference: https://www.cnblogs.com/lightwindy/p/8547310.html '''
import collections, heapq
class Solution:
    def rearrangeString(self, words, k):
        if k < 2: return words
        n = len(words)
        wordCount = collections.Counter(words)
        heap = heapq.heapify([])
        for word, count in wordCount.items():
            heapq.heappush(heap, (-count, word))

        res = ''
        while heap:
            used = []
            for i in range(min(n, k)):
                if not heap: return ''   # not enough character to fill in the k spaces
                nc, w = heapq.heappop(heap)   # always start from the most frequent character since it is most difficult to separate them by k spaces apart
                res += w
                if -nc > 1:
                    used.append((nc + 1, w))
                n -= 1
            for w in used:
                heapq.heappush(heap, w)
        return res