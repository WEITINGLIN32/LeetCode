'''
Title: 191. Number of 1 Bits (Easy) https://leetcode.com/problems/number-of-1-bits/

Runtime: 24 ms, faster than 55.02% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.6 MB, less than 5.10% of Python online submissions for Number of 1 Bits.

Description:
        Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Example:
    Input: 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

    Input: 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

    Input: 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        
        while n > 0:
            if n%2==1:
                count+=1
            n/=2
        return count
        