'''
Title: 509. Fibonacci Number (Easy) https://leetcode.com/problems/fibonacci-number/

Runtime: 20 ms, faster than 78.99% of Python online submissions for Fibonacci Number.
Memory Usage: 11.8 MB, less than 5.25% of Python online submissions for Fibonacci Number.

Description:
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
        such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), for N > 1.
        Given N, calculate F(N).

Example:
    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

'''

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fib = {}
        
        fib[0] = 0
        fib[1] = 1
        output = 0
        
        
        for i in range(2,31):
            fib[i] = fib[i-1] + fib[i-2]
        
        return fib[N]