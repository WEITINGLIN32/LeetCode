'''
Title: 50. Pow(x, n) (Medium)    https://leetcode.com/problems/powx-n/

Runtime: 36 ms, faster than 99.73% of Python3 online submissions for Pow(x, n).
Memory Usage: 13 MB, less than 5.53% of Python3 online submissions for Pow(x, n).

Description:
        Implement pow(x, n), which calculates x raised to the power n (xn).

Example:
    Input: 2.00000, 10
    Output: 1024.00000

    Input: 2.10000, 3
    Output: 9.26100

    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
    
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
        