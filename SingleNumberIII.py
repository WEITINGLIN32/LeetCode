'''
Title: 260. Single Number III (Medium) https://leetcode.com/problems/single-number-iii/

Runtime: 48 ms, faster than 43.86% of Python online submissions for Single Number III.
Memory Usage: 14 MB, less than 6.67% of Python online submissions for Single Number III.

Description:
        Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
        Find the two elements that appear only once.

Example:
    Input:  [1,2,1,3,2,5]
    Output: [3,5]

'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        output = []
        
        for i in dict:
            if dict[i] == 1:
                output.append(i)
        
        return output