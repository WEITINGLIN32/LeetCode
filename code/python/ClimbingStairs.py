'''
Title: 70. Climbing Stairs (Easy) https://leetcode.com/problems/climbing-stairs/

Runtime: 36 ms, faster than 76.32% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.3 MB, less than 5.18% of Python3 online submissions for Climbing Stairs.

Description:
        You are climbing a stair case. It takes n steps to reach to the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        Note: Given n will be a positive integer.

Example:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {}
        dict[1] = 1
        dict[2] = 2
        
        for i in range(3,n+1):
            dict[i] = dict[i-1] + dict[i-2]
        
        return dict[n]