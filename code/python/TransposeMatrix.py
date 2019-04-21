'''
Title: 867. Transpose Matrix (Easy) https://leetcode.com/problems/transpose-matrix/

Runtime: 80 ms, faster than 22.96% of Python online submissions for Transpose Matrix.
Memory Usage: 12.2 MB, less than 6.17% of Python online submissions for Transpose Matrix.

Description:
        Given a matrix A, return the transpose of A
        The transpose of a matrix is the matrix flipped over it's main diagonal, 
        switching the row and column indices of the matrix.

Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]

'''

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        
        if len(A) == 1:
            if len(A[0]) == 1:
                return A
           
            for i in range(len(A[0])):
                tmp = []
                tmp.append(A[0][i])
                output.append(tmp)
            
            return output
        
        
        for i in range(len(A[1])):
            tmp = []
            for j in range(len(A)):
                tmp.append(A[j][i])
            output.append(tmp)
        return output
 