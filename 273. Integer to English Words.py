'''
Title     : 273. Integer to English Words
Problem   : https://leetcode.com/problems/integer-to-english-words/
'''
'''
lookup dictionary + recursive helper function
Reference: https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = 'Thousand Million Billion'.split()

        def num2word(num, i=0):
            if num == 0: return []
            if num < 20: return [to19[num-1]]
            if num < 100: return [tens[num//10-2]] + num2word(num%10)
            if num < 1000: return [to19[num//100-1]] + ['Hundred'] + num2word(num%100)

            thousand, rem = num//1000, num%1000
            space = [thousands[i]] if thousand % 1000 != 0 else []
            return num2word(thousand,i+1) + space + num2word(rem)

        return ' '.join(num2word(num)) or 'Zero'