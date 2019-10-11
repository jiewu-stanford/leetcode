'''
Title     : 284. Peeking Iterator
Problem   : https://leetcode.com/problems/peeking-iterator/
'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator:
    def __init__(self, iterator):
        self.iter, self.buff = iterator, []
        
    def peek(self):
        if len(self.buff) == 0:
            self.buff.append(self.iter.next())
        return self.buff[0]

    def next(self):
        if len(self.buff) > 0:
            return self.buff.pop(0)
        else:
            return self.iter.next()

    def hasNext(self):
        return len(self.buff) != 0 or self.iter.hasNext()
        
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].