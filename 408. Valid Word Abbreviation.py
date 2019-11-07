'''
Title     : 408. Valid Word Abbreviation
Problem   : https://leetcode.com/problems/valid-word-abbreviation
          : https://www.lintcode.com/problem/valid-word-abbreviation/description
'''
''' Reference: http://bookshadow.com/weblog/2016/10/02/leetcode-valid-word-abbreviation/ '''
class Solution:
    def validWordAbbreviation(self, word, abbr):
        length = len(word)
        count = indx = 0
        for w in abbr:
            if w.isdigit():
                if w == '0' and count == 0:
                    return False
                count = count*10 + int(w)
            else:
                indx += count
                count = 0
                if indx >= length or word[indx] != w:
                    return False
                indx += 1
        return indx + count == length