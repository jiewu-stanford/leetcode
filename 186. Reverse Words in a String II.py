'''
Title     : 186. Reverse Words in a String II ($$$)
Problem   : https://leetcode.com/problems/reverse-words-in-a-string-ii/
          : https://www.lintcode.com/problem/reverse-words-in-a-string-ii/description
'''
class Solution:
    def reverseWords(self, str):
        str_list = ''.join(str).split(' ')
        str_list.reverse()
        return ' '.join(str_list)