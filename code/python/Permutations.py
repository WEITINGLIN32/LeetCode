'''
Title: 46. Permutations (Medium)    https://leetcode.com/problems/permutations/

Runtime: 48 ms, faster than 91.57% of Python3 online submissions for Permutations.
Memory Usage: 13.2 MB, less than 5.23% of Python3 online submissions for Permutations.

Description:
        Given a collection of distinct integers, return all possible permutations.

Example:
    Input: [1,2,3]
    Output:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]

'''

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
        
        