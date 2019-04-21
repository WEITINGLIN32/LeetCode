'''
Title: 540. Single Element in a Sorted Array (Medium) https://leetcode.com/problems/single-element-in-a-sorted-array/

Runtime: 52 ms, faster than 29.61% of Python online submissions for Single Element in a Sorted Array.
Memory Usage: 13.5 MB, less than 5.00% of Python online submissions for Single Element in a Sorted Array.

Description:
        Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. 
        Find this single element that appears only once.

Example:
    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2

    Input: [3,3,7,7,10,11,11]
    Output: 10

'''

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for i in dict:
            if dict[i] == 1:
                return i
        