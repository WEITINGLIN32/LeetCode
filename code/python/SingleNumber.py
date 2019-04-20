'''
Title: 136. Single Number (Easy) https://leetcode.com/problems/single-number/

Runtime: 48 ms, faster than 45.15% of Python3 online submissions for Single Number.
Memory Usage: 15.1 MB, less than 5.05% of Python3 online submissions for Single Number.

Description:
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example:
    Input: [2,2,1]
    Output: 1

    Input: [4,1,2,1,2]
    Output: 4

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = {}
        
        for i in nums:
            if i in number:
                number[i] += 1
            else:
                number[i] = 1

        for i in nums:
            if number[i] % 2 != 0:
                return i