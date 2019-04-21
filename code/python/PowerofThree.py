'''
Title: 326. Power of Three (Easy) https://leetcode.com/problems/power-of-three/

Runtime: 124 ms, faster than 91.61% of Python online submissions for Power of Three.
Memory Usage: 11.9 MB, less than 5.29% of Python online submissions for Power of Three.

Description:
        Given an integer, write a function to determine if it is a power of three.

Example:
    Input: 27
    Output: true

    Input: 0
    Output: false   

    Input: 9
    Output: true

    Input: 45
    Output: false   
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n == 1:
                return True
            if n % 3 == 0:
                n = n / 3
            else:
                return False
                break
        return False
        