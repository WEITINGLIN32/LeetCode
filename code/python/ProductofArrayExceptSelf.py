'''
Title: 238. Product of Array Except Self (Medium) https://leetcode.com/problems/product-of-array-except-self/

Runtime: 120 ms, faster than 33.02% of Python online submissions for Product of Array Except Self.
Memory Usage: 21.1 MB, less than 5.09% of Python online submissions for Product of Array Except Self.

Description:
        Given an array nums of n integers where n > 1,  
        return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        
        num1 = [1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            num1[i] = num1[i-1]*nums[i-1]
        
        num2 = [1 for i in range(len(nums))]
        
        for i in range(len(nums)-2, -1, -1):
            num2[i] = num2[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            output.append(num1[i]*num2[i])
            
        return output
        