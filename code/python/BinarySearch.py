'''
Title: 704. Binary Search (Easy) https://leetcode.com/problems/binary-search/

Runtime: 232 ms, faster than 25.42% of Python online submissions for Binary Search.
Memory Usage: 12.7 MB, less than 6.04% of Python online submissions for Binary Search.

Description:
        Given a sorted (in ascending order) integer array nums of n elements and a target value, 
        write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1