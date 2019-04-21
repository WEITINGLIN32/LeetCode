'''
Title: 922. Sort Array By Parity II (Easy) https://leetcode.com/problems/sort-array-by-parity-ii/

Runtime: 212 ms, faster than 32.03% of Python online submissions for Sort Array By Parity II.
Memory Usage: 14.2 MB, less than 5.79% of Python online submissions for Sort Array By Parity II.

Description:
        Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

        Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

        You may return any answer array that satisfies this condition.

Example:
    Input: [4,2,5,7]
    Output: [4,5,2,7]
    Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted

'''

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        result = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        for i in range(len(A)):
            if i%2 == 0:
                result.append(even.pop())
            else:
                result.append(odd.pop())
        return result
        