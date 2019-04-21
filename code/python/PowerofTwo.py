'''
Title: 231. Power of Two (Easy) https://leetcode.com/problems/power-of-two/

Runtime: 28 ms, faster than 41.32% of Python online submissions for Power of Two.
Memory Usage: 11.8 MB, less than 5.23% of Python online submissions for Power of Two.

Description:
        Given an integer, write a function to determine if it is a power of two.

Example:
    Input: 1
    Output: true 
    Explanation: 20 = 1

    Input: 16
    Output: true
    Explanation: 24 = 16

    Input: 218
    Output: false

'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        
        while pow(2, cnt) <= n:
            if pow(2, cnt) == n:
                return True
                break
            cnt += 1
        
        return False
        
        