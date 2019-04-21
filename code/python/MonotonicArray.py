'''
Title: 896. Monotonic Array (Easy) https://leetcode.com/problems/monotonic-array/

Runtime: 444 ms, faster than 33.36% of Python online submissions for Monotonic Array.
Memory Usage: 17.1 MB, less than 5.21% of Python online submissions for Monotonic Array.

Description:
        An array is monotonic if it is either monotone increasing or monotone decreasing.

        An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
        An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

        Return true if and only if the given array A is monotonic.

Example:
    Input: [1,2,2,3]
    Output: true

    Input: [6,5,4,4]
    Output: true

    Input: [1,3,2]
    Output: false

    Input: [1,2,4,5]
    Output: true

    Input: [1,1,1]
    Output: true

'''

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        max_index = A.index(max(A))
        if max(A) == A[-1]:
            max_index = len(A) - 1
        if max_index == len(A) - 1:
            now = A[0]
            for i in range(1,len(A)):
                if now <= A[i]:
                    now = A[i]
                    continue
                else:
                    return False
            return True
        elif max_index == 0:
            now = A[0]
            for i in range(1,len(A)):
                if now >= A[i]:
                    now = A[i]
                    continue
                else:
                    return False
            return True
        else:
            return False
        