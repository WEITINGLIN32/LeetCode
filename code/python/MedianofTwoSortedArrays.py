'''
Title: 4. Median of Two Sorted Arrays (Hard)    https://leetcode.com/problems/median-of-two-sorted-arrays/

Runtime: 60 ms, faster than 97.10% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.

Description:
        There are two sorted arrays nums1 and nums2 of size m and n respectively.
        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
        You may assume nums1 and nums2 cannot be both empty.

Example:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0

    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:   
        x = nums1 + nums2
        x.sort()
        if len(x)%2 == 1:
            return float(x[int(len(x)/2)])
        else:
            return float((x[int(len(x)/2)]+x[int(len(x)/2-1)])/2.0)
        
      
        
