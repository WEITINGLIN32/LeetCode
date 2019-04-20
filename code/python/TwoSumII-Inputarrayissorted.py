'''
Title: 167. Two Sum II - Input array is sorted (Easy) https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Runtime: 40 ms, faster than 83.47% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.2 MB, less than 5.14% of Python3 online submissions for Two Sum II - Input array is sorted.

Description:
        Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
        The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Example:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for index,i in enumerate(numbers) :
            if i in dict:
                dict[i].append(index)
            else:
                dict[i] = []
                dict[i].append(index)
        
        for i in dict:
            if target - i in dict and target-i != i:
                if dict[i][0] > dict[target-i][0]:
                    return [dict[target-i][0]+1,dict[i][0]+1]
                else:
                    return [dict[i][0]+1,dict[target-i][0]+1]
                break
            elif target - i in dict and target-i == i:
                return [dict[i][0]+1, dict[i][1]+1]
                break
        