'''
Title: 504. Base 7 (Easy) https://leetcode.com/problems/base-7/

Runtime: 20 ms, faster than 84.24% of Python online submissions for Base 7.
Memory Usage: 11.9 MB, less than 5.45% of Python online submissions for Base 7

Description:
        Given an integer, return its base 7 string representation.

Example:
    Input: 100
    Output: "202"

    Input: -7
    Output: "-10"

'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        arr = [pow(7,8), pow(7,7), pow(7,6), pow(7,5), pow(7,4), pow(7,3), pow(7,2), pow(7,1), pow(7,0)]
        
        output = ""
        if num > 0:
            for i in arr:
                tmp = int(num/i)
                if tmp > 0:
                    output += str(tmp)
                    num -= i*tmp
                else:
                    output += str(0)
            return str(int(output))
        elif num < 0:
            output += "-"
            num = abs(num)
            for i in arr:
                tmp = int(num/i)
                if tmp > 0:
                    output += str(tmp)
                    num -= i*tmp
                else:
                    output += str(0)
            return str(int(output))
        else:
            return "0"