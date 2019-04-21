'''
Title: 693. Binary Number with Alternating Bits (Easy) https://leetcode.com/problems/binary-number-with-alternating-bits/

Runtime: 20 ms, faster than 77.32% of Python online submissions for Binary Number with Alternating Bits.
Memory Usage: 11.7 MB, less than 6.82% of Python online submissions for Binary Number with Alternating Bits.

Description:
        Given a positive integer, check whether it has alternating bits: namely, 
        if two adjacent bits will always have different values.

Example:
    Input: 5
    Output: True
    Explanation:
    The binary representation of 5 is: 101

    Input: 7
    Output: False
    Explanation:
    The binary representation of 7 is: 111.

    Input: 11
    Output: False
    Explanation:
    The binary representation of 11 is: 1011.

    Input: 10
    Output: True
    Explanation:
    The binary representation of 10 is: 1010.

'''

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]
        
        lock = 1
        if binary[0] == '1':
            for i in range(1,len(binary)):
                if i % 2 == 0 and binary[i] != '1':
                    return False
                if i % 2 == 1 and binary[i] != '0':
                    return False         
        else:
            for i in range(1,len(binary)):
                if i % 2 == 0 and binary[i] != '0':
                    return False
                if i % 2 == 1 and binary[i] != '1':
                    return False       
        
        return True