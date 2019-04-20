'''
Title: 118. Pascal's Triangle (Easy) https://leetcode.com/problems/pascals-triangle/

Runtime: 36 ms, faster than 78.83% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.1 MB, less than 5.83% of Python3 online submissions for Pascal's Triangle.

Description:
        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:
    Input: 5
    Output:
    [
        [1],
        [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
    ]

'''

if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            output = [[1],[1,1]]
            for i in range(2,numRows+1):
                tmp = []
                for j in range(i):
                    if j == 0 or j == i-1:
                        tmp.append(1)
                    else:
                        tmp.append(output[i-1][j-1]+output[i-1][j])
                output.append(tmp)
        del output[1]
        return output