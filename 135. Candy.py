'''
Title     : 135. Candy
Problem   : https://leetcode.com/problems/candy/description/
'''
'''
two-pass solution: from left to right to add candy to right neighbor + from right to left to add candy to left neighbor
Reference: https://leetcode.com/problems/candy/discuss/172118/Python-simple-10-line-two-passes-solution-with-explanation
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        res = [1]*n
        for i in range(1, n):   # from left to right, add candy to higher rated neighbor on the right
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(n-1, 0, -1):   # from right to left, add candy to higher rated neighbor on the left
            if ratings[i-1] > ratings[i] and res[i-1] <= res[i]:   # for local maximum res[i-1] > res[i] already thus no need to add
                res[i-1] = res[i] + 1
        return sum(res)
'''
one-pass solution, record the `local altitude' measured by up from the previous local minimum and down from the previous local maximum
Reference: https://leetcode.com/problems/candy/discuss/42770/One-pass-constant-space-Java-solution
Reference: https://blog.csdn.net/xx_123_1_rj/article/details/86636718
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n, total = len(ratings), 1
        up = down = peak = 0
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                up += 1
                total += up + 1
                down, peak = 0, up   # reset to become new local maximum
            elif ratings[i-1] > ratings[i]:
                down += 1
                total += 1 + down - (1 if peak >= down else 0)   # no need to add candy to peak if peak is already higher or at least equal
                up = 0   # reset to become new local minimum
            else:
                peak = up = down = 0
                total += 1
        return total
'''
one-pass solution producing the candies given to each child using a buffer recording the descending sequence immediately preceding a child
Reference: https://stackoverflow.com/questions/58053944/leetcode-problem-135-candy-one-pass-solution-to-find-the-number-of-candies-given/58054132#58054132
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n, descbuff = len(ratings), []   # descbuff = descending sequence of immediately preceding ratings
        res = [1]*n
        pairs = list(zip(ratings[1:], ratings))
        for i, (curr, prev) in enumerate(pairs, start=1):
            if curr < prev:
                if not descbuff: descbuff = [i-1]
                descbuff.append(i)
                if i != n-1: continue
            if curr > prev:
                res[i] = res[i-1] + 1
            if descbuff:
                for extra, indx in enumerate(descbuff[::-1]):
                    res[indx] = max(res[indx], extra+1)
                del descbuff[:]
        return sum(res)