'''
Title: 476. Number Complement (Easy) https://leetcode.com/problems/number-complement/

Runtime: 20 ms, faster than 72.78% of Python online submissions for Number Complement.
Memory Usage: 11.7 MB, less than 5.19% of Python online submissions for Number Complement.

Description:
        Given a positive integer, output its complement number. 
        The complement strategy is to flip the bits of its binary representation.

Example:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), 
    and its complement is 010. So you need to output 2.

    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

'''

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = ""
        
        i = num
        
        while i > 0:
            tmp += str(i%2)
            i = int(i/2)
        
        total = 0
        for i in range(len(tmp)):
            if tmp[i] == '0':
                total += pow(2,i)
        
        return total