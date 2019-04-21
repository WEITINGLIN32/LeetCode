'''
Title: 905. Sort Array By Parity (Easy) https://leetcode.com/problems/sort-array-by-parity/

Runtime: 68 ms, faster than 49.45% of Python online submissions for Sort Array By Parity.
Memory Usage: 12.5 MB, less than 5.22% of Python online submissions for Sort Array By Parity.

Description:
        Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
        followed by all the odd elements of A.

        You may return any answer array that satisfies this condition.

Example:
    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

'''

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd
        