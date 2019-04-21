'''
Title: 674. Longest Continuous Increasing Subsequence (Easy) https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Runtime: 64 ms, faster than 34.32% of Python online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 12.8 MB, less than 6.17% of Python online submissions for Longest Continuous Increasing Subsequence.

Description:
        Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example:
    Input: [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
    Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

    Input: [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        
        cnt = []
        tmp = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] > tmp:
                count += 1
                tmp = nums[i]
            else:
                cnt.append(count)
                count = 1
                tmp = nums[i]
            
            if i == len(nums) - 1:
                cnt.append(count)
        
        return max(cnt)