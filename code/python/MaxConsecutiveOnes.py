'''
Title: 485. Max Consecutive Ones (Easy) https://leetcode.com/problems/max-consecutive-ones/

Runtime: 348 ms, faster than 27.22% of Python online submissions for Max Consecutive Ones.
Memory Usage: 12 MB, less than 5.47% of Python online submissions for Max Consecutive Ones.

Description:
        Given a binary array, find the maximum number of consecutive 1s in this array.

Example:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.

'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 and nums[0] == 1:
            return 1
        elif len(nums) == 1 and nums[0] == 0:
            return 0
        else:
            if 1 not in nums:
                return 0
            else:
                pos = nums.index(1)
                cnt = 1
                arr.append(cnt)
                for i in range(pos+1, len(nums)):
                    if nums[i] == 1:
                        cnt += 1
                    else:
                        arr.append(cnt)
                        cnt = 0
                    if i == len(nums) -1 and nums[i] == 1:
                        arr.append(cnt)
                return max(arr)