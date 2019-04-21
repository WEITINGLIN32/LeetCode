'''
Title: 724. Find Pivot Index (Easy) https://leetcode.com/problems/find-pivot-index/

Runtime: 136 ms, faster than 42.15% of Python online submissions for Find Pivot Index.
Memory Usage: 12.5 MB, less than 5.13% of Python online submissions for Find Pivot Index.

Description:
        Given an array of integers nums, write a method that returns the "pivot" index of this array.

        We define the pivot index as the index where the sum of the numbers to the left of the index 
        is equal to the sum of the numbers to the right of the index.

        If no such index exists, we should return -1. 
        If there are multiple pivot indexes, you should return the left-most pivot index.

Example:
    Input: 
    nums = [1, 7, 3, 6, 5, 6]
    Output: 3
    Explanation: 
    The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
    Also, 3 is the first index where this occurs.

    Input: 
    nums = [1, 2, 3]
    Output: -1
    Explanation: 
    There is no index that satisfies the conditions in the problem statement.

'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        total = sum(nums)
        left = 0
        
        for index,i in enumerate(nums):
            if left == total - i - left:
                return index
                break
            left += i
        
        return -1
        