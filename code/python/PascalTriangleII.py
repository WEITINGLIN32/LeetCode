'''
Title: 119. Pascal's Triangle II (Easy) https://leetcode.com/problems/pascals-triangle-ii/

Runtime: 40 ms, faster than 35.70% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13 MB, less than 5.12% of Python3 online submissions for Pascal's Triangle II.

Description:
        Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
        Note that the row index starts from 0.

Example:
    Input: 3
    Output: [1,3,3,1]

'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dict = {}
        
        dict[1] = [1]
        dict[2] = [1,1]
        
        for i in range(3,rowIndex+2):
            dict[i] = []
            for j in range(i):
                if j == 0 or j == i-1:
                    dict[i].append(1)
                else:
                    dict[i].append(dict[i-1][j-1]+dict[i-1][j])
            
        return dict[rowIndex+1]