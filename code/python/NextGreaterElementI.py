'''
Title: 496. Next Greater Element I (Easy) https://leetcode.com/problems/next-greater-element-i/

Runtime: 80 ms, faster than 21.69% of Python online submissions for Next Greater Element I.
Memory Usage: 11.7 MB, less than 5.94% of Python online submissions for Next Greater Element I.

Description:
        You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
        Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
        Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
        If it does not exist, output -1 for this number.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]
    Explanation:
        For number 2 in the first array, the next greater number for it in the second array is 3.
        For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        for index,i in enumerate(nums1):
            flag = 0
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j] > i:
                    flag = 1
                    nums1[index] = nums2[j]
                    break
            if flag == 0:
                nums1[index] = -1
        
        return nums1
        