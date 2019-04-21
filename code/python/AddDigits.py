'''
Title: 258. Add Digits (Easy) https://leetcode.com/problems/add-digits/

Runtime: 28 ms, faster than 59.54% of Python online submissions for Add Digits.
Memory Usage: 11.6 MB, less than 6.30% of Python online submissions for Add Digits.

Description:
        Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2 
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
                Since 2 has only one digit, return it. 

'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        
        output = 0
        for i in string:
            output += int(i)
        while output > 9:
            string = str(output)
            output = 0
            for i in string:
                output += int(i)
        
        return output