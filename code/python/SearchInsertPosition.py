'''
Title: 35. Search Insert Position (Easy)    https://leetcode.com/problems/search-insert-position/

Runtime: 36 ms, faster than 93.09% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.6 MB, less than 5.11% of Python3 online submissions for Search Insert Position.

Description:
        Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        You may assume no duplicates in the array.

Example:
    Input: [1,3,5,6], 5
    Output: 2

    Input: [1,3,5,6], 2
    Output: 1

    Input: [1,3,5,6], 7
    Output: 4

    Input: [1,3,5,6], 0
    Output: 0

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for index,i in enumerate(nums):
            if target - i in dict:
                return [dict[target-i], index]
            else:
                dict[i] = index
        