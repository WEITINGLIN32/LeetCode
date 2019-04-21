'''
Title: 507. Perfect Number (Easy) https://leetcode.com/problems/perfect-number/

Runtime: 40 ms, faster than 21.86% of Python online submissions for Perfect Number.
Memory Usage: 11.7 MB, less than 7.32% of Python online submissions for Perfect Number.

Description:
        We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
        Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14

'''

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = 0
        if num <= 0:
            return False
        i = 1
        while pow(i,2) <= num:
            if num % i == 0:
                x += i
                if pow(i,2) != num:
                    x += num / i
            i += 1
        
        if x - 2*num == 0:
            return True
        else:
            return False
        