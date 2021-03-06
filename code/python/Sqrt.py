'''
Title: 69. Sqrt(x) (Easy) https://leetcode.com/problems/sqrtx/

Runtime: 40 ms, faster than 99.84% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.2 MB, less than 5.75% of Python3 online submissions for Sqrt(x).

Description:
        Implement int sqrt(int x).
        Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
        Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example:
    Input: 4
    Output: 2

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(pow(x,0.5))
        