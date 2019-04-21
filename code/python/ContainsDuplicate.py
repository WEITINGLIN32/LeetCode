'''
Title: 217. Contains Duplicate (Easy) https://leetcode.com/problems/contains-duplicate/

Runtime: 108 ms, faster than 42.07% of Python online submissions for Contains Duplicate.
Memory Usage: 17.1 MB, less than 5.24% of Python online submissions for Contains Duplicate.

Description:
    Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in the array, 
    and it should return false if every element is distinct.

Example:
    Input: [1,2,3,1]
    Output: true

    Input: [1,2,3,4]
    Output: false

    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(nums) == len(list(set(nums)))
        