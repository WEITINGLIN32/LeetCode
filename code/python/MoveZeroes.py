'''
Title: 283. Move Zeroes (Easy) https://leetcode.com/problems/move-zeroes/

Runtime: 40 ms, faster than 56.79% of Python online submissions for Move Zeroes.
Memory Usage: 12.8 MB, less than 5.06% of Python online submissions for Move Zeroes.

Description:
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        output = [0 for i in range(len(nums))]
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                output[pos] = nums[i]
                pos += 1
        
        for i in range(len(nums)):
            nums[i] = output[i]