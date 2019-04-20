'''
Title: 7. Reverse Integer (Easy)    https://leetcode.com/problems/reverse-integer/

Runtime: 40 ms, faster than 99.91% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.1 MB, less than 5.71% of Python3 online submissions for Reverse Integer.

Description:
       Given a 32-bit signed integer, reverse digits of an integer.

Example:
    Input: 123
    Output: 321

    Input: -123
    Output: -321

    Input: 120
    Output: 21

'''

class Solution:
    def reverse(self, x: int) -> int:       
        output = ""
        
        tmp = str(x)
        
        if x < 0:
            output += '-'
            if tmp[len(tmp)-1] != 0:
                for i in range(len(tmp)-1,0,-1):
                    output+=tmp[i]
            if int(output) < pow(-2,31):
                return 0
            return int(output)
                
        else:
            output = tmp[::-1]
            if int(output) > pow(2,31):
                return 0
            return int(output)