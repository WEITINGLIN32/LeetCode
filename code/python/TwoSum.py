'''
Title: 1. Two Sum (Easy)

Runtime: 36 ms, faster than 99.41% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 5.08% of Python3 online submissions for Two Sum.

Description:
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1]. 
    
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for index,i in enumerate(nums):
            if target - i in dict:
                return [dict[target-i], index]
            else:
                dict[i] = index
        