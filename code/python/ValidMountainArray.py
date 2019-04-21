'''
Title: 941. Valid Mountain Array (Easy) https://leetcode.com/problems/valid-mountain-array/

Runtime: 188 ms, faster than 36.26% of Python online submissions for Valid Mountain Array.
Memory Usage: 12.8 MB, less than 6.06% of Python online submissions for Valid Mountain Array.

Description:
        Given an array A of integers, return true if and only if it is a valid mountain array.

        Recall that A is a mountain array if and only if:

        A.length >= 3
        There exists some i with 0 < i < A.length - 1 such that:
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[B.length - 1]

Example:
    Input: [2,1]
    Output: false

    Input: [3,5,5]
    Output: false

    Input: [0,3,2,1]
    Output: true

'''

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        else:
            MAX = max(A)
            b = 0
            for i in range(A.index(MAX)):
                if A[i+1] <= A[i]:
                    b = 1
                    break
            if b == 0 and A.index(MAX) != len(A)-1 and A.index(MAX) != 0:
                for i in range(A.index(MAX),len(A)):
                    if i+1 != len(A):
                        if A[i] <= A[i+1]:
                            b = 1
                            break
                if b == 0:
                    return True
                else:
                    return False
            else:
                return False
        