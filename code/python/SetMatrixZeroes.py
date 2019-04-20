'''
Title: 73. Set Matrix Zeroes (Medium) https://leetcode.com/problems/set-matrix-zeroes/

Runtime: 132 ms, faster than 5.70% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 13.5 MB, less than 5.26% of Python3 online submissions for Set Matrix Zeroes.

Description:
        Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example:
Input: 
    [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    Output: 
    [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]

    Input: 
    [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    Output: 
    [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ii = []
        jj = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ii.append(i)
                    jj.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in ii or j in jj:
                    matrix[i][j] = 0
        
        