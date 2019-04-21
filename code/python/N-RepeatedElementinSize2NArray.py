'''
Title: 961. N-Repeated Element in Size 2N Array (Easy) https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

Runtime: 228 ms, faster than 28.05% of Python online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 13.1 MB, less than 5.26% of Python online submissions for N-Repeated Element in Size 2N Array.

Description:
        In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

        Return the element repeated N times.

Example:
    Input: [1,2,3,3]
    Output: 3

    Input: [2,1,2,5,3,2]
    Output: 2

    Input: [5,1,5,2,5,3,5,4]
    Output: 5

'''

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dict = {}
        
        for i in A:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for i in dict:
            if dict[i] == len(A)/2:
                return i
                break
        