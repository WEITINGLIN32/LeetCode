'''
Title: 796. Rotate String (Easy) https://leetcode.com/problems/rotate-string/

Runtime: 20 ms, faster than 75.88% of Python online submissions for Rotate String.
Memory Usage: 11.6 MB, less than 6.67% of Python online submissions for Rotate String.

Description:
        We are given two strings, A and B.

        A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
        For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
        Return True if and only if A can become B after some number of shifts on A.

Example:
        Input: A = 'abcde', B = 'cdeab'
        Output: true

        Input: A = 'abcde', B = 'abced'
        Output: false

'''

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        
        for i in range(len(A)):
            if B == A:
                return True
                break
            tmp = ""
            tmp += A[1:] + A[0]
            A = tmp
        
        return False
        