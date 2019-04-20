'''
Runtime: 36 ms
Memory: 7.9 MB
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

       
        dict = {}
        
        for index,i in enumerate(nums):
            if target - i in dict:
                return [dict[target-i], index]
            else:
                dict[i] = index
        
