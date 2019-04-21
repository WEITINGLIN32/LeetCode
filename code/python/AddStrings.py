'''
Title: 415. Add Strings (Easy) https://leetcode.com/problems/add-strings/

Runtime: 24 ms, faster than 97.31% of Python online submissions for Add Strings.
Memory Usage: 11.9 MB, less than 5.69% of Python online submissions for Add Strings.

Description:
        Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Example:
    1. The length of both num1 and num2 is < 5100.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))