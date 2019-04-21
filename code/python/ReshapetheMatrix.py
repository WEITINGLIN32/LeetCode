'''
Title: 566. Reshape the Matrix (Easy) https://leetcode.com/problems/reshape-the-matrix/

Runtime: 92 ms, faster than 49.34% of Python online submissions for Reshape the Matrix.
Memory Usage: 13 MB, less than 13.70% of Python online submissions for Reshape the Matrix.

Description:
        In MATLAB, there is a very useful function called 'reshape', 
        which can reshape a matrix into a new one with different size but keep its original data.

        You're given a matrix represented by a two-dimensional array, and two positive integers r and c 
        representing the row number and column number of the wanted reshaped matrix, respectively.

        The reshaped matrix need to be filled with all the elements of the original matrix 
        in the same row-traversing order as they were.

        If the 'reshape' operation with given parameters is possible and legal, 
        output the new reshaped matrix; Otherwise, output the original matrix

Example:
    Input: 
    nums = 
    [[1,2],
    [3,4]]
    r = 1, c = 4
    Output: 
    [[1,2,3,4]]
    Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, 
    fill it row by row by using the previous list.

    Input: 
    nums = 
    [[1,2],
    [3,4]]
    r = 2, c = 4
    Output: 
    [[1,2],
    [3,4]]
    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

'''

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c > len(nums) * len(nums[0]):
            return nums
        
        output = [[0 for i in range(c)] for j in range(r)]
        
        tmp = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                tmp.append(nums[i][j])
        
        cnt = 0
        for i in range(len(output)):
            for j in range(len(output[0])):
                output[i][j] = tmp[cnt]
                cnt += 1
        
        return output