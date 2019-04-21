'''
Title: 852. Peak Index in a Mountain Array (Easy) https://leetcode.com/problems/peak-index-in-a-mountain-array/

Runtime: 80 ms, faster than 22.24% of Python online submissions for Peak Index in a Mountain Array.
Memory Usage: 12.8 MB, less than 6.31% of Python online submissions for Peak Index in a Mountain Array.

Description:
        Let's call an array A a mountain if the following properties hold:

        A.length >= 3
        There exists some 0 < i < A.length - 1 
        such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
        Given an array that is definitely a mountain, 
        return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example:
    Input: [0,1,0]
    Output: 1

    Input: [0,2,1,0]
    Output: 1

'''

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
        