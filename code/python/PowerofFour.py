'''
Title: 342. Power of Four (Easy) https://leetcode.com/problems/power-of-four/

Runtime: 24 ms, faster than 99.72% of Python online submissions for Power of Four.
Memory Usage: 11.9 MB, less than 6.41% of Python online submissions for Power of Four.

Description:
        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
    Input: 16
    Output: true 

    Input: 5
    Output: false
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        tmp = num
        cnt = 0
        if num == 0:
            return False

        while num % 4 == 0:
            if num % 4 == 0:
                num /= 4
                cnt += 1

        if pow(4, cnt) == tmp:
            return True
        else:
            return False