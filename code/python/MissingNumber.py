'''
Title: 268. Missing Number (Easy) https://leetcode.com/problems/missing-number/

Runtime: 128 ms, faster than 31.38% of Python online submissions for Missing Number.
Memory Usage: 13.3 MB, less than 5.05% of Python online submissions for Missing Number.

Description:
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example:
    Input: [3,0,1]
    Output: 2

    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = [i for i in range(len(nums)+1)]
        
        return list(set(x) - set(nums))[0]
        