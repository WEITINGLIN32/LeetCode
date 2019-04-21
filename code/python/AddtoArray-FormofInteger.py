'''
Title: 989. Add to Array-Form of Integer (Easy) https://leetcode.com/problems/add-to-array-form-of-integer/

Runtime: 312 ms, faster than 41.14% of Python online submissions for Add to Array-Form of Integer.
Memory Usage: 12 MB, less than 10.84% of Python online submissions for Add to Array-Form of Integer.

Description:
        For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
        For example, if X = 1231, then the array form is [1,2,3,1].

        Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example:
    Input: A = [1,2,0,0], K = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

    Input: A = [2,7,4], K = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

    Input: A = [2,1,5], K = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

    Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
    Output: [1,0,0,0,0,0,0,0,0,0,0]
    Explanation: 9999999999 + 1 = 10000000000

'''

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        X = ""
        
        for i in A:
            X += str(i)
        
        num = int(X) + K
        
        output = [int(i) for i in str(num)]
        
        return output
        