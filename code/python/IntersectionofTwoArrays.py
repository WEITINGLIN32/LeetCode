'''
Title: 349. Intersection of Two Arrays (Easy) https://leetcode.com/problems/intersection-of-two-arrays/

Runtime: 56 ms, faster than 25.58% of Python online submissions for Intersection of Two Arrays.
Memory Usage: 11.9 MB, less than 5.86% of Python online submissions for Intersection of Two Arrays.

Description:
        Given two arrays, write a function to compute their intersection.

Example:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1 and i not in output:
                    output.append(i)
        
        else:
            for i in nums1:
                if i in nums2 and i not in output:
                    output.append(i)
        
        return output
        