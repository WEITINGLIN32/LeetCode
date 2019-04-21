'''
Title: 448. Find All Numbers Disappeared in an Array (Easy) https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Runtime: 328 ms, faster than 33.98% of Python online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.7 MB, less than 5.19% of Python online submissions for Find All Numbers Disappeared in an Array.

Description:
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements of [1, n] inclusive that do not appear in this array.
        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]

'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        num = set(nums)

        elements = [i for i in range(1,len(nums)+1)]
        
        return list(set(elements) - num)
        