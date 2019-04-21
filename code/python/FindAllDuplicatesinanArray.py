'''
Title: 442. Find All Duplicates in an Array (Medium) https://leetcode.com/problems/find-all-duplicates-in-an-array/

Runtime: 332 ms, faster than 36.99% of Python online submissions for Find All Duplicates in an Array.
Memory Usage: 22 MB, less than 5.00% of Python online submissions for Find All Duplicates in an Array.

Description:
        Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements that appear twice in this array.
        Could you do it without extra space and in O(n) runtime?

Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]

'''

class Solution(object):
    def findDuplicates(self, nums):
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
        
        return [i for i in dict if dict[i] > 1]
        