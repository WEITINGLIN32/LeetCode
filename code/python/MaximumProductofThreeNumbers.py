'''
Title: 628. Maximum Product of Three Numbers (Easy) https://leetcode.com/problems/maximum-product-of-three-numbers/

Runtime: 248 ms, faster than 32.47% of Python online submissions for Maximum Product of Three Numbers.
Memory Usage: 12.4 MB, less than 5.94% of Python online submissions for Maximum Product of Three Numbers.

Description:
        Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example:
    Input: [1,2,3]
    Output: 6

    Input: [1,2,3,4]
    Output: 24

'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        output = []
        
        num1 = 1
        num2 = 1
        tmp = nums[-3:]
        tmp1 = nums[0:2]
        
        for i in tmp:
            num1 *= i
        output.append(num1)
        
        for j in tmp1:
            num2*=j
        
        num2 *= nums[-1]
        output.append(num2)

        return max(output)
        