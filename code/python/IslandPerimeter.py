'''
Title: 463. Island Perimeter (Easy) https://leetcode.com/problems/island-perimeter/

Runtime: 492 ms, faster than 26.74% of Python online submissions for Island Perimeter.
Memory Usage: 12 MB, less than 12.04% of Python online submissions for Island Perimeter.

Description:
        You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

        Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
        and there is exactly one island (i.e., one or more connected land cells).

        The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
        One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
        Determine the perimeter of the island.

Example:
Input:
    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

    Output: 16

'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 4
                    if i-1 >= 0:
                        if grid[i-1][j] == 1:
                            cnt -=1
                    if j-1 >= 0:
                        if grid[i][j-1] == 1:
                            cnt -=1
                    if i+1 < len(grid):
                          if grid[i+1][j] == 1:
                            cnt -=1  
                    if j+1 < len(grid[0]):  
                        if grid[i][j+1] == 1:
                            cnt -=1

        return cnt
        