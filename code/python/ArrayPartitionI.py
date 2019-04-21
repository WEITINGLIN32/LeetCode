'''
Title: 561. Array Partition I (Easy) https://leetcode.com/problems/array-partition-i/

Runtime: 268 ms, faster than 31.90% of Python online submissions for Array Partition I.
Memory Usage: 14.2 MB, less than 5.39% of Python online submissions for Array Partition I.

Description:
    Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., 
    (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example:
    Input: [1,4,3,2]

    Output: 4
    Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        
        for i in range(0,len(nums),2):
            total += min(nums[i],nums[i+1])
    
        return total