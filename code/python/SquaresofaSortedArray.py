'''
Title: 977. Squares of a Sorted Array (Easy) https://leetcode.com/problems/squares-of-a-sorted-array/

Runtime: 196 ms, faster than 40.59% of Python online submissions for Squares of a Sorted Array.
Memory Usage: 13.7 MB, less than 5.04% of Python online submissions for Squares of a Sorted Array.

Description:
        Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
        also in sorted non-decreasing order.

Example:
    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        x = [i ** 2 for i in A]
        
        return sorted(x)