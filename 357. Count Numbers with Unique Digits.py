'''
Title     : 357. Count Numbers with Unique Digits
Problem   : https://leetcode.com/problems/count-numbers-with-unique-digits/description/
'''
''' Reference: https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83040/Simple-Python-solution-90 '''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        res = 10      # res initially stores number 1,2,...,9 and 10^n
        choices = 9   # number of choices for the leading digit (which is 1,2,...,9)
        for i in range(1, n):
            choices = choices * (10 - i)    # number of choices remaining for the ith digit after fixing the digits preceding it and the last digit
                                            # e.g. for i = 2, fixing the first and last digit leaves 8 choices for the second digit
            res += choices
        return res